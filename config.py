"""
RSSフィード設定
必要に応じてフィードの追加・削除を行ってください。

keywords フィールド（オプション）:
  指定した場合、記事タイトルにいずれかのキーワードが含まれるものだけを対象にします。
  PR Times のように全プレスリリースが流れるフィードで AI 関連だけを拾うのに使います。
"""

# PR Times 競合フィード用の共通キーワード
AI_KEYWORDS = [
    "AI", "人工知能", "機械学習", "深層学習", "ディープラーニング",
    "生成AI", "ChatGPT", "GPT", "LLM", "大規模言語モデル",
    "自然言語処理", "画像認識", "音声認識", "データ分析",
    "DX", "自動化", "ロボット", "チャットボット",
]

RSS_FEEDS = [
    # ─── 海外AIニュース ─────────────────────────────────────────
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
    # ─── 国内AIニュース ─────────────────────────────────────────
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
    # ─── PR Times（総合AI） ──────────────────────────────────────
    {
        "name": "PR Times",
        "url": "https://prtimes.jp/index.rdf",
        "category": "国内AI",
        "keywords": AI_KEYWORDS,
    },
    # ─── AIリサーチ / ラボ ──────────────────────────────────────
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
    # ─── 競合動向：飲食 ──────────────────────────────────────
    {
        "name": "カカクコム (食べログ)",
        "url": "https://prtimes.jp/companyrdf.php?company_id=1455",
        "category": "競合：飲食",
        "keywords": AI_KEYWORDS,
    },
    {
        "name": "ぐるなび",
        "url": "https://prtimes.jp/companyrdf.php?company_id=1511",
        "category": "競合：飲食",
        "keywords": AI_KEYWORDS,
    },
    {
        "name": "Retty",
        "url": "https://prtimes.jp/companyrdf.php?company_id=4025",
        "category": "競合：飲食",
        "keywords": AI_KEYWORDS,
    },
    {
        "name": "出前館",
        "url": "https://prtimes.jp/companyrdf.php?company_id=29254",
        "category": "競合：飲食",
        "keywords": AI_KEYWORDS,
    },
    # ─── 競合動向：住まい ────────────────────────────────────
    {
        "name": "LIFULL (HOME'S)",
        "url": "https://prtimes.jp/companyrdf.php?company_id=33058",
        "category": "競合：住まい",
        "keywords": AI_KEYWORDS,
    },
    {
        "name": "アットホーム",
        "url": "https://prtimes.jp/companyrdf.php?company_id=51123",
        "category": "競合：住まい",
        "keywords": AI_KEYWORDS,
    },
    {
        "name": "オープンハウスグループ",
        "url": "https://prtimes.jp/companyrdf.php?company_id=24241",
        "category": "競合：住まい",
        "keywords": AI_KEYWORDS,
    },
    # ─── 競合動向：美容 ──────────────────────────────────────
    {
        "name": "MIXI (minimo)",
        "url": "https://prtimes.jp/companyrdf.php?company_id=25121",
        "category": "競合：美容",
        "keywords": AI_KEYWORDS,
    },
    # ─── 競合動向：自動車 ────────────────────────────────────
    {
        "name": "IDOM (ガリバー)",
        "url": "https://prtimes.jp/companyrdf.php?company_id=20448",
        "category": "競合：自動車",
        "keywords": AI_KEYWORDS,
    },
    {
        "name": "ネクステージ",
        "url": "https://prtimes.jp/companyrdf.php?company_id=10893",
        "category": "競合：自動車",
        "keywords": AI_KEYWORDS,
    },
    {
        "name": "プロトコーポレーション (goo-net)",
        "url": "https://prtimes.jp/companyrdf.php?company_id=17791",
        "category": "競合：自動車",
        "keywords": AI_KEYWORDS,
    },
]

