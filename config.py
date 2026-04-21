"""
RSSフィード設定
必要に応じてフィードの追加・削除を行ってください。
"""

RSS_FEEDS = [
      # --- 海外AIニュース ---
    {
              "name": "MITテクノロジーレビュー",
              "url": "https://www.technologyreview.com/feed/",
              "category": "海外AI",
    },
      {
                "name": "TechCrunch AI",
                "url": "https://techcrunch.com/category/artificial-intelligence/feed/",
                "category": "海外AI",
      },
      {
                "name": "The Verge AI",
                "url": "https://www.theverge.com/ai-artificial-intelligence/rss/index.xml",
                "category": "海外AI",
      },
      {
                "name": "VentureBeat AI",
                "url": "https://venturebeat.com/category/ai/feed/",
                "category": "海外AI",
      },
      {
                "name": "WIRED AI",
                "url": "https://www.wired.com/feed/tag/ai/latest/rss",
                "category": "海外AI",
      },
      # --- 国内AIニュース ---
      {
                "name": "ITmedia AI+",
                "url": "https://rss.itmedia.co.jp/rss/2.0/aiplus.xml",
                "category": "国内AI",
      },
      {
                "name": "Ledge.ai",
                "url": "https://ledge.ai/feed/",
                "category": "国内AI",
      },
      {
                "name": "AINOW",
                "url": "https://ainow.ai/feed/",
                "category": "国内AI",
      },
      {
                "name": "Impress Watch",
                "url": "https://www.watch.impress.co.jp/data/rss/1.0/ipw/feed.rdf",
                "category": "国内AI",
      },
      # --- AIリサーチ / ラボ ---
      {
                "name": "OpenAI Blog",
                "url": "https://openai.com/blog/rss/",
                "category": "AIリサーチ",
      },
      {
                "name": "Anthropic Blog",
                "url": "https://www.anthropic.com/rss.xml",
                "category": "AIリサーチ",
      },
      {
                "name": "Google DeepMind Blog",
                "url": "https://deepmind.google/blog/rss.xml",
                "category": "AIリサーチ",
      },
      {
                "name": "arXiv (cs.AI)",
                "url": "https://rss.arxiv.org/rss/cs.AI",
                "category": "AIリサーチ",
      },
]
