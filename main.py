"""
AI News RSS Collector â Slack Poster
æ¯æ GitHub Actions ããå®è¡ããéå»24æéä»¥åã®è¨äºã Slack ã«æç¨¿ããã
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

# ââ è¨­å® ââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââ
SLACK_WEBHOOK_URL = os.environ.get("SLACK_WEBHOOK_URL", "")
HOURS_LOOKBACK = int(os.environ.get("HOURS_LOOKBACK", "24"))
MAX_ARTICLES_PER_FEED = int(os.environ.get("MAX_ARTICLES_PER_FEED", "5"))

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)
logger = logging.getLogger(__name__)

JST = timezone(timedelta(hours=9))


# ââ RSS åå¾ ââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââ
def fetch_articles(feed: dict, cutoff: datetime) -> list[dict]:
    """æå®ãã£ã¼ããã cutoff ä»¥éã®è¨äºãåå¾ããã"""
    url = feed["url"]
    name = feed["name"]
    logger.info(f"Fetching: {name} ({url})")

    try:
        d = feedparser.parse(url)
    except Exception as e:
        logger.warning(f"  â  ãã¼ã¹å¤±æ: {name} - {e}")
        return []

    if d.bozo and not d.entries:
        logger.warning(f"  â  ãã£ã¼ãåå¾ã¨ã©ã¼: {name}")
        return []

    articles = []
    keywords = feed.get("keywords", [])

    for entry in d.entries[:20]:  # ææ°20ä»¶ããã§ãã¯
        # å¬éæ¥æã®åå¾
        published = None
        for attr in ("published_parsed", "updated_parsed"):
            if hasattr(entry, attr) and getattr(entry, attr):
                published = datetime.fromtimestamp(
                    mktime(getattr(entry, attr)), tz=timezone.utc
                )
                break

        # æ¥æãåå¾ã§ããªãå ´åã¯ã¹ã­ãã
        if published is None:
            continue

        # éå» N æéä»¥åã®è¨äºã®ã¿
        if published < cutoff:
            continue

        title = entry.get("title", "(ã¿ã¤ãã«ãªã)")

        # ã­ã¼ã¯ã¼ããã£ã«ã¿: æå®ãããå ´åãã¿ã¤ãã«ã«å«ã¾ãããã®ã®ã¿
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
    logger.info(f"  â {len(articles)} ä»¶ã®æ°çè¨äº")
    return articles


# ââ Slack ã¡ãã»ã¼ã¸çµã¿ç«ã¦ âââââââââââââââââââââââââââââââââââââââââââââ
def build_slack_blocks(articles: list[dict]) -> dict:
    """Slack Block Kit å½¢å¼ã®ã¡ãã»ã¼ã¸ãçµã¿ç«ã¦ãã"""
    now_jst = datetime.now(JST).strftime("%Yå¹´%mæ%dæ¥ %H:%M")

    blocks = [
        {
            "type": "header",
            "text": {
                "type": "plain_text",
                "text": f"ð° AI News Digest ({now_jst})",
                "emoji": True,
            },
        },
        {"type": "divider"},
    ]

    # ã«ãã´ãªãã¨ã«ã°ã«ã¼ãã³ã°
    by_category: dict[str, list[dict]] = {}
    for a in articles:
        by_category.setdefault(a["category"], []).append(a)

    category_emojis = {
        "æµ·å¤AI": "ð",
        "å½åAI": "ð¯ðµ",
        "Horizontal AI": "ð§ª",
        "ç«¶åï¼é£²é£": "ð½ï¸",
        "ç«¶åï¼ä½ã¾ã": "ð ",
        "ç«¶åï¼ç¾å®¹": "ð",
        "ç«¶åï¼èªåè»": "ð",
        "ç«¶åï¼æè¡": "âï¸",
        "ã«ã¹ã¿ãã¼AIåå": "ð",
        "AIæè³ã»ãã¼ã±ãã": "ð°",
    }

    for category, items in by_category.items():
        emoji = category_emojis.get(category, "ð")
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
                            f"_{item['source']}_ ã» {item['published']}"
                        ),
                    },
                }
            )

        blocks.append({"type": "divider"})

    return {
        "blocks": blocks,
        "text": f"AI News Digest - {len(articles)} ä»¶ã®æ°çè¨äº",  # fallback
    }


def build_no_news_message() -> dict:
    """æ°çè¨äºãç¡ãå ´åã®ã¡ãã»ã¼ã¸ã"""
    now_jst = datetime.now(JST).strftime("%Yå¹´%mæ%dæ¥ %H:%M")
    return {
        "blocks": [
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f"ð° *AI News Digest* ({now_jst})\n\néå» {HOURS_LOOKBACK} æéä»¥åã®æ°çè¨äºã¯ããã¾ããã§ããã",
                },
            }
        ],
        "text": "AI News Digest - æ°çè¨äºãªã",
    }


# ââ Slack éä¿¡ ââââââââââââââââââââââââââââââââââââââââââââââââââââââââââ
def post_to_slack(payload: dict) -> None:
    """Incoming Webhook ã§ Slack ã«æç¨¿ããã"""
    if not SLACK_WEBHOOK_URL:
        logger.error("SLACK_WEBHOOK_URL ãè¨­å®ããã¦ãã¾ããã")
        # ãããã°ç¨: stdout ã«åºå
        print(json.dumps(payload, ensure_ascii=False, indent=2))
        sys.exit(1)

    resp = requests.post(
        SLACK_WEBHOOK_URL,
        data=json.dumps(payload, ensure_ascii=False).encode("utf-8"),
        headers={"Content-Type": "application/json; charset=utf-8"},
        timeout=30,
    )

    if resp.status_code != 200:
        logger.error(f"Slack éä¿¡å¤±æ: {resp.status_code} {resp.text}")
        sys.exit(1)

    logger.info("â Slack ã«æç¨¿ãã¾ãã")


# ââ ã¡ã¤ã³ ââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââ
def main():
    cutoff = datetime.now(timezone.utc) - timedelta(hours=HOURS_LOOKBACK)
    logger.info(f"å¯¾è±¡æé: {cutoff.isoformat()} ä»¥é")

    all_articles: list[dict] = []
    for feed in RSS_FEEDS:
        articles = fetch_articles(feed, cutoff)
        all_articles.extend(articles)

    logger.info(f"åè¨: {len(all_articles)} ä»¶ã®æ°çè¨äº")

    if all_articles:
        # å¬éæ¥æã§æ°ããé ã«ã½ã¼ã
        all_articles.sort(key=lambda a: a["published"], reverse=True)
        payload = build_slack_blocks(all_articles)
    else:
        payload = build_no_news_message()

    post_to_slack(payload)


if __name__ == "__main__":
    main()
