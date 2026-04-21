"""
AI News RSS Collector → Slack Poster
毎朝 GitHub Actions から実行し、過去24時間以内の記事を Slack に投稿する。
"""

import os
import sys
import json
import logging
from datetime import datetime, timedelta, timezone
from time import mktime

import feedparser
import requests

from config import RSS_FEEDS

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


# ── RSS 取得 ──────────────────────────────────────────────────────────────
def fetch_articles(feed: dict, cutoff: datetime) -> list[dict]:
    """指定フィードから cutoff 以降の記事を取得する。"""
    url = feed["url"]
    name = feed["name"]
    logger.info(f"Fetching: {name} ({url})")

    try:
        d = feedparser.parse(url)
    except Exception as e:
        logger.warning(f"  ⚠ パース失敗: {name} - {e}")
        return []

    if d.bozo and not d.entries:
        logger.warning(f"  ⚠ フィード取得エラー: {name}")
        return []

    articles = []
    keywords = feed.get("keywords", [])

    for entry in d.entries[:20]:  # 最新20件をチェック
        # 公開日時の取得
        published = None
        for attr in ("published_parsed", "updated_parsed"):
            if hasattr(entry, attr) and getattr(entry, attr):
                published = datetime.fromtimestamp(
                    mktime(getattr(entry, attr)), tz=timezone.utc
                )
                break

        # 日時が取得できない場合はスキップ
        if published is None:
            continue

        # 過去 N 時間以内の記事のみ
        if published < cutoff:
            continue

        title = entry.get("title", "(タイトルなし)")

        # キーワードフィルタ: 指定がある場合、タイトルに含まれるもののみ
        if keywords and not any(kw.lower() in title.lower() for kw in keywords):
            continue

        articles.append(
            {
                "title": title,
                "link": entry.get("link", ""),
                "published": published.astimezone(JST).strftime("%Y-%m-%d %H:%M"),
                "source": name,
                "category": feed.get("category", ""),
            }
        )

    articles = articles[:MAX_ARTICLES_PER_FEED]
    logger.info(f"  → {len(articles)} 件の新着記事")
    return articles


# ── Slack メッセージ組み立て ───────────────────────────────────────────────
def build_slack_blocks(articles: list[dict]) -> dict:
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

    # カテゴリごとにグルーピング
    by_category: dict[str, list[dict]] = {}
    for a in articles:
        by_category.setdefault(a["category"], []).append(a)

    category_emojis = {
        "海外AI": "🌏",
        "国内AI": "🇯🇵",
        "AIリサーチ": "🔬",
        "競合：飲食": "🍽️",
        "競合：住まい": "🏠",
        "競合：美容": "💇",
        "競合：自動車": "🚗",
    }

    for category, items in by_category.items():
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
            blocks.append(
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": (
                            f"<{item['link']}|{item['title']}>\n"
                            f"_{item['source']}_・{item['published']}"
                        ),
                    },
                }
            )

        blocks.append({"type": "divider"})

    return {
        "blocks": blocks,
        "text": f"AI News Digest - {len(articles)} 件の新着記事",  # fallback
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


# ── Slack 送信 ──────────────────────────────────────────────────────────────
def post_to_slack(payload: dict) -> None:
    """Incoming Webhook で Slack に投稿する。"""
    if not SLACK_WEBHOOK_URL:
        logger.error("SLACK_WEBHOOK_URL が設定されていません。")
        # デバッグ用: stdout に出力
        print(json.dumps(payload, ensure_ascii=False, indent=2))
        sys.exit(1)

    resp = requests.post(
        SLACK_WEBHOOK_URL,
        json=payload,
        headers={"Content-Type": "application/json"},
        timeout=30,
    )

    if resp.status_code != 200:
        logger.error(f"Slack 送信失敗: {resp.status_code} {resp.text}")
        sys.exit(1)

    logger.info("✅ Slack に投稿しました")


# ── メイン ────────────────────────────────────────────────────────────────
def main():
    cutoff = datetime.now(timezone.utc) - timedelta(hours=HOURS_LOOKBACK)
    logger.info(f"対象期間: {cutoff.isoformat()} 以降")

    all_articles: list[dict] = []
    for feed in RSS_FEEDS:
        articles = fetch_articles(feed, cutoff)
        all_articles.extend(articles)

    logger.info(f"合計: {len(all_articles)} 件の新着記事")

    if all_articles:
        # 公開日時で新しい順にソート
        all_articles.sort(key=lambda a: a["published"], reverse=True)
        payload = build_slack_blocks(all_articles)
    else:
        payload = build_no_news_message()

    post_to_slack(payload)


if __name__ == "__main__":
    main()

