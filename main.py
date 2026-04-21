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

SLACK_WEBHOOK_URL = os.environ.get("SLACK_WEBHOOK_URL", "")
HOURS_LOOKBACK = int(os.environ.get("HOURS_LOOKBACK", "24"))
MAX_ARTICLES_PER_FEED = int(os.environ.get("MAX_ARTICLES_PER_FEED", "5"))

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)
logger = logging.getLogger(__name__)

JST = timezone(timedelta(hours=9))

def fetch_articles(feed, cutoff):
    url = feed["url"]
    name = feed["name"]
    logger.info(f"Fetching: {name} ({url})")

    try:
        d = feedparser.parse(url)
    except Exception as e:
        logger.warning(f"Parse error: {name} - {e}")
        return []

    if d.bozo and not d.entries:
        logger.warning(f"Feed error: {name}")
        return []

    articles = []
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

        articles.append({
            "title": entry.get("title", "(No title)"),
            "link": entry.get("link", ""),
            "published": published.astimezone(JST).strftime("%Y-%m-%d %H:%M"),
            "source": name,
            "category": feed.get("category", ""),
        })

    articles = articles[:MAX_ARTICLES_PER_FEED]
    logger.info(f"  -> {len(articles)} new articles")
    return articles

def build_slack_blocks(articles):
    now_jst = datetime.now(JST).strftime("%Y/%m/%d %H:%M")

    blocks = [
        {
            "type": "header",
            "text": {
                "type": "plain_text",
                "text": f"AI News Digest ({now_jst})",
                "emoji": True,
            },
        },
        {"type": "divider"},
    ]

    by_category = {}
    for a in articles:
        by_category.setdefault(a["category"], []).append(a)

    for category, items in by_category.items():
        blocks.append({
            "type": "section",
            "text": {"type": "mrkdwn", "text": f"*{category}*"},
        })

        for item in items:
            blocks.append({
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": (
                        f"<{item['link']}|{item['title']}>\n"
                        f"_{item['source']}_ / {item['published']}"
                    ),
                },
            })

        blocks.append({"type": "divider"})

    return {
        "blocks": blocks,
        "text": f"AI News Digest - {len(articles)} articles",
      }

def build_no_news_message():
    now_jst = datetime.now(JST).strftime("%Y/%m/%d %H:%M")
    return {
        "blocks": [{
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": f"AI News Digest ({now_jst})\n\nNo new articles in the past {HOURS_LOOKBACK} hours.",
            },
        }],
        "text": "AI News Digest - No new articles",
    }


def post_to_slack(payload):
    if not SLACK_WEBHOOK_URL:
        logger.error("SLACK_WEBHOOK_URL is not set.")
        print(json.dumps(payload, ensure_ascii=False, indent=2))
        sys.exit(1)

    resp = requests.post(
        SLACK_WEBHOOK_URL,
        json=payload,
        headers={"Content-Type": "application/json"},
        timeout=30,
    )

    if resp.status_code != 200:
        logger.error(f"Slack post failed: {resp.status_code} {resp.text}")
        sys.exit(1)

    logger.info("Posted to Slack successfully")


def main():
    cutoff = datetime.now(timezone.utc) - timedelta(hours=HOURS_LOOKBACK)
    logger.info(f"Looking back from: {cutoff.isoformat()}")

    all_articles = []
    for feed in RSS_FEEDS:
        all_articles.extend(fetch_articles(feed, cutoff))

    logger.info(f"Total: {len(all_articles)} new articles")

    if all_articles:
        all_articles.sort(key=lambda a: a["published"], reverse=True)
        payload = build_slack_blocks(all_articles)
    else:
        payload = build_no_news_message()

    post_to_slack(payload)


if __name__ == "__main__":
    main()
