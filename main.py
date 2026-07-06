"""
AI News RSS Collector → Slack Poster
毎朝 GitHub Actions から実行し、過去24時間以内の記事を Slack に投稿する。
"""

import os
import sys
import json
import logging
import time as _time
from datetime import datetime, timedelta, timezone
from time import mktime

import feedparser
import requests
from deep_translator import GoogleTranslator

from config import RSS_FEEDS
from filters import filter_articles

# ── 設定 ────────────────────────────────────────────────────────────────
SLACK_WEBHOOK_URL = os.environ.get("SLACK_WEBHOOK_URL", "")
HOURS_LOOKBACK = int(os.environ.get("HOURS_LOOKBACK", "24"))
MAX_ARTICLES_PER_FEED = int(os.environ.get("MAX_ARTICLES_PER_FEED", "5"))

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)
logger = logging.getLogger(__name__)

JST = timezone(timedelta(hours=9))

_translator = GoogleTranslator(source="en", target="ja")


def translate_title(title: str) -> str:
    """英語タイトルを日本語に翻訳する。日本語の場合はそのまま返す。"""
    ascii_ratio = sum(1 for c in title if ord(c) < 128) / max(len(title), 1)
    if ascii_ratio < 0.8:
        return title
    try:
        translated = _translator.translate(title)
        return translated if translated else title
    except Exception:
        return title


# ── 株価取得 ────────────────────────────────────────────────────────────
def fetch_stock_changes(tickers: list[str]) -> dict[str, dict]:
    """複数の銘柄の前日比（%）を一括取得する。"""
    if not tickers:
        return {}

    try:
        import yfinance as yf
    except ImportError:
        logger.warning("yfinance がインストールされていません。株価情報をスキップします。")
        return {}

    result = {}
    unique_tickers = list(set(tickers))
    logger.info(f"株価取得中: {len(unique_tickers)} 銘柄")

    try:
        # 一括ダウンロード（5日分で週末/祝日をカバー）
        data = yf.download(unique_tickers, period="5d", progress=False, threads=True)

        if data.empty:
            logger.warning("株価データが空です")
            return {}

        for ticker in unique_tickers:
            try:
                if len(unique_tickers) == 1:
                    closes = data["Close"]
                else:
                    closes = data["Close"][ticker]

                closes = closes.dropna()
                if len(closes) >= 2:
                    prev_close = closes.iloc[-2]
                    curr_close = closes.iloc[-1]
                    change_pct = ((curr_close - prev_close) / prev_close) * 100
                    result[ticker] = {
                        "price": round(float(curr_close), 2),
                        "change_pct": round(float(change_pct), 2),
                    }
            except Exception as e:
                logger.warning(f"  株価解析失敗 {ticker}: {e}")
    except Exception as e:
        logger.warning(f"株価一括取得失敗: {e}")
        # フォールバック: 個別取得
        for ticker in unique_tickers:
            try:
                stock = yf.Ticker(ticker)
                hist = stock.history(period="5d")
                closes = hist["Close"].dropna()
                if len(closes) >= 2:
                    prev_close = closes.iloc[-2]
                    curr_close = closes.iloc[-1]
                    change_pct = ((curr_close - prev_close) / prev_close) * 100
                    result[ticker] = {
                        "price": round(float(curr_close), 2),
                        "change_pct": round(float(change_pct), 2),
                    }
            except Exception:
                pass

    logger.info(f"株価取得完了: {len(result)}/{len(unique_tickers)} 銘柄")
    return result


def format_stock_change(ticker: str, stock_data: dict) -> str:
    """株価変動率を Slack 用にフォーマットする。"""
    info = stock_data.get(ticker)
    if not info:
        return ""
    pct = info["change_pct"]
    if pct >= 0:
        arrow = "📈"
        sign = "+"
    else:
        arrow = "📉"
        sign = ""
    # 日本株 (.T) は通貨表示なし、米国株はドル表示
    if ticker.endswith(".T"):
        price_str = f"¥{info['price']:,.0f}"
    else:
        price_str = f"${info['price']:,.2f}"
    return f"  |  {arrow} {ticker.replace('.T', '')} {sign}{pct:.1f}% ({price_str})"

# ── RSS 取得 ────────────────────────────────────────────────────────────
def fetch_articles(feed: dict, cutoff: datetime) -> list[dict]:
    """指定フィードから cutoff 以降の記事を取得する。"""
    url = feed["url"]
    name = feed["name"]
    logger.info(f"Fetching: {name} ({url})")

    max_retries = 2
    d = None
    for attempt in range(1, max_retries + 1):
        try:
            resp = requests.get(url, timeout=10, headers={"User-Agent": "AI-News-Bot/1.0"})
            resp.raise_for_status()
            d = feedparser.parse(resp.content)
            if d.bozo and not d.entries:
                raise Exception(f"bozo error: {getattr(d, 'bozo_exception', 'unknown')}")
            break
        except Exception as e:
            if attempt < max_retries:
                logger.info(f"  ↻ リトライ {attempt}/{max_retries} (2秒後): {name}")
                _time.sleep(2)
            else:
                logger.warning(f"  ⚠ 取得失敗: {name} - {e}")
                return []

    if d is None or (d.bozo and not d.entries):
        return []

    articles = []
    keywords = feed.get("keywords", [])
    ticker = feed.get("ticker", "")

    for entry in d.entries[:20]:
        published = None
        for attr in ("published_parsed", "updated_parsed"):
            if hasattr(entry, attr) and getattr(entry, attr):
                published = datetime.fromtimestamp(
                    mktime(getattr(entry, attr)), tz=timezone.utc
                )
                break

        if published is None:
            continue

        if published < cutoff:
            continue

        title = entry.get("title", "(タイトルなし)")

        if keywords and not any(kw.lower() in title.lower() for kw in keywords):
            continue

        articles.append(
            {
                "title": translate_title(title),
                "link": entry.get("link", ""),
                "published": published.astimezone(JST).strftime("%Y-%m-%d %H:%M"),
                "source": name,
                "category": feed.get("category", ""),
                "ticker": ticker,
            }
        )

    articles = articles[:MAX_ARTICLES_PER_FEED]
    logger.info(f"  → {len(articles)} 件の新着記事")
    return articles

# ── Slack メッセージ組み立て ─────────────────────────────────────────────
def build_slack_blocks(articles: list[dict], stock_data: dict) -> dict:
    """Slack Block Kit 形式のメッセージを組み立てる。"""
    now_jst = datetime.now(JST).strftime("%Y年%m月%d日 %H:%M")

    blocks = [
        {
            "type": "header",
            "text": {
                "type": "plain_text",
                "text": f"📰 AI News Digest ({now_jst})",
                "emoji": True,
            },
        },
        {"type": "divider"},
    ]

    by_category: dict[str, list[dict]] = {}
    for a in articles:
        by_category.setdefault(a["category"], []).append(a)

    category_emojis = {
        "海外AI": "🌏",
        "国内AI": "🇯🇵",
        "Horizontal AI": "🧪",
        "競合：飲食": "🍽️",
        "競合：住まい": "🏠",
        "競合：美容": "💇",
        "競合：自動車": "🚗",
        "競合：旅行": "✈️",
        "カスタマーAI動向": "📊",
        "国内競合ニュース": "🏢",
        "海外競合ニュース": "🌐",
    }

    # カテゴリ表示順を定義
    category_order = [
        "国内競合ニュース", "海外競合ニュース",
        "海外AI", "国内AI", "Horizontal AI",
        "競合：飲食", "競合：住まい", "競合：美容", "競合：自動車", "競合：旅行",
        "カスタマーAI動向",
    ]

    # 定義順 → 未定義カテゴリの順で表示
    sorted_categories = []
    for cat in category_order:
        if cat in by_category:
            sorted_categories.append(cat)
    for cat in by_category:
        if cat not in sorted_categories:
            sorted_categories.append(cat)

    for category in sorted_categories:
        items = by_category[category]
        emoji = category_emojis.get(category, "📌")
        blocks.append(
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f"*{emoji} {category}*",
                },
            }
        )

        for item in items:
            # 株価情報を付与
            stock_str = ""
            if item.get("ticker") and stock_data:
                stock_str = format_stock_change(item["ticker"], stock_data)

            blocks.append(
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": (
                            f"<{item['link']}|{item['title']}>\n"
                            f"_{item['source']}_ ・ {item['published']}{stock_str}"
                        ),
                    },
                }
            )

        blocks.append({"type": "divider"})

    # Slack Block Kit の上限は 50 ブロック。超過分を切り詰める
    if len(blocks) > 49:
        blocks = blocks[:49]
        blocks.append(
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f"_（他にも記事があります。上限のため省略）_",
                },
            }
        )

    return {
        "blocks": blocks,
        "text": f"AI News Digest - {len(articles)} 件の新着記事",
    }

def build_no_news_message() -> dict:
    """新着記事が無い場合のメッセージ。"""
    now_jst = datetime.now(JST).strftime("%Y年%m月%d日 %H:%M")
    return {
        "blocks": [
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f"📰 *AI News Digest* ({now_jst})\n\n過去 {HOURS_LOOKBACK} 時間以内の新着記事はありませんでした。",
                },
            }
        ],
        "text": "AI News Digest - 新着記事なし",
    }


# ── Slack 送信 ──────────────────────────────────────────────────────────
def post_to_slack(payload: dict) -> None:
    """Incoming Webhook で Slack に投稿する。"""
    if not SLACK_WEBHOOK_URL:
        logger.error("SLACK_WEBHOOK_URL が設定されていません。")
        print(json.dumps(payload, ensure_ascii=False, indent=2))
        sys.exit(1)

    resp = requests.post(
        SLACK_WEBHOOK_URL,
        data=json.dumps(payload, ensure_ascii=False).encode("utf-8"),
        headers={"Content-Type": "application/json; charset=utf-8"},
        timeout=30,
    )

    if resp.status_code != 200:
        logger.error(f"Slack 送信失敗: {resp.status_code} {resp.text}")
        sys.exit(1)

    logger.info("✅ Slack に投稿しました")


# ── メイン ──────────────────────────────────────────────────────────────
def main():
    cutoff = datetime.now(timezone.utc) - timedelta(hours=HOURS_LOOKBACK)
    logger.info(f"対象期間: {cutoff.isoformat()} 以降")

    all_articles: list[dict] = []
    all_tickers: list[str] = []

    for feed in RSS_FEEDS:
        articles = fetch_articles(feed, cutoff)
        all_articles.extend(articles)
        # ティッカー収集
        if feed.get("ticker"):
            all_tickers.append(feed["ticker"])

    logger.info(f"合計: {len(all_articles)} 件の新着記事")

    # 国内/海外競合ニュースは Claude で関連度フィルタをかける
    all_articles = filter_articles(all_articles)
    logger.info(f"フィルタ後: {len(all_articles)} 件")

    # 株価データ取得
    stock_data = {}
    if all_tickers:
        stock_data = fetch_stock_changes(all_tickers)

    if all_articles:
        all_articles.sort(key=lambda a: a["published"], reverse=True)
        payload = build_slack_blocks(all_articles, stock_data)
    else:
        payload = build_no_news_message()

    post_to_slack(payload)


if __name__ == "__main__":
    main()
