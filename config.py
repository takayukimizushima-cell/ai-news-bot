"""
RSSフィード設定
必要に応じてフィードの追加・削除を行ってください。

keywords フィールド（オプション）:
  指定した場合、記事タイトルにいずれかのキーワードが含まれるものだけを対象にします。
  PR Times のように全プレスリリースが流れるフィードで関連記事だけを拾うのに使います。
"""

# ── キーワード定義 ──────────────────────────────────────────────────────

# 競合企業フィード用: サービスへのAI組み込み・機能リリース観点
AI_SERVICE_KEYWORDS = [
    # AI活用・導入
    "AI搭載", "AI機能", "AI活用", "AI導入", "AI対応", "AI連携",
    "AI実装", "AIを活用", "AIによる",
    # 生成AI / LLM 具体名
    "生成AI", "ChatGPT", "GPT", "Claude", "Gemini", "Copilot",
    "LLM", "大規模言語モデル",
    # 機能系
    "AIアシスタント", "AIエージェント", "AIチャット", "チャットボット",
    "AI検索", "AIレコメンド", "AI分析", "AI予測", "AI翻訳",
    "AI査定", "AI接客", "AI提案", "AIマッチング",
    "自動生成", "自動応答", "自動翻訳",
    "パーソナライズ", "レコメンデーション",
    # 技術系
    "画像認識", "音声認識", "自然言語処理", "機械学習",
    "OCR", "ディープラーニング",
]

# 一般AIニュースフィード用: プロダクト・機能寄りのキーワード
AI_PRODUCT_KEYWORDS = [
    # 機能リリース系
    "launch", "release", "feature", "update", "announce",
    "tool", "API", "plugin", "integration",
    # AI プロダクト
    "ChatGPT", "GPT-4", "GPT-5", "Claude", "Gemini", "Copilot",
    "Sora", "DALL-E", "Midjourney", "Stable Diffusion",
    "agent", "assistant", "search", "coding",
    # 日本語キーワード（国内ニュース用）
    "新機能", "提供開始", "リリース", "アップデート",
    "AI搭載", "AI活用", "AI機能", "生成AI",
    "AIエージェント", "AIアシスタント",
]

RSS_FEEDS = [
    # ─── 海外AIニュース ─────────────────────────────────────────
    {
        "name": "TechCrunch AI",
        "url": "https://techcrunch.com/category/artificial-intelligence/feed/",
        "category": "海外AI",
        "keywords": AI_PRODUCT_KEYWORDS,
    },
    {
        "name": "The Verge AI",
        "url": "https://www.theverge.com/ai-artificial-intelligence/rss/index.xml",
        "category": "海外AI",
        "keywords": AI_PRODUCT_KEYWORDS,
    },
    {
        "name": "VentureBeat AI",
        "url": "https://venturebeat.com/category/ai/feed/",
        "category": "海外AI",
        "keywords": AI_PRODUCT_KEYWORDS,
    },
    {
        "name": "WIRED AI",
        "url": "https://www.wired.com/feed/tag/ai/latest/rss",
        "category": "海外AI",
        "keywords": AI_PRODUCT_KEYWORDS,
    },
    # ─── 国内AIニュース ─────────────────────────────────────────
    {
        "name": "ITmedia AI+",
        "url": "https://rss.itmedia.co.jp/rss/2.0/aiplus.xml",
        "category": "国内AI",
        "keywords": AI_PRODUCT_KEYWORDS,
    },
    {
        "name": "Ledge.ai",
        "url": "https://ledge.ai/feed/",
        "category": "国内AI",
        "keywords": AI_PRODUCT_KEYWORDS,
    },
    {
        "name": "AINOW",
        "url": "https://ainow.ai/feed/",
        "category": "国内AI",
        "keywords": AI_PRODUCT_KEYWORDS,
    },
    {
        "name": "Impress Watch",
        "url": "https://www.watch.impress.co.jp/data/rss/1.0/ipw/feed.rdf",
        "category": "国内AI",
        "keywords": AI_PRODUCT_KEYWORDS,
    },
    # ─── Horizontal AI（ラボ / プラットフォーム） ────────────────
    {
        "name": "OpenAI Blog",
        "url": "https://openai.com/blog/rss/",
        "category": "Horizontal AI",
    },
    {
        "name": "Anthropic Blog",
        "url": "https://www.anthropic.com/rss.xml",
        "category": "Horizontal AI",
    },
    {
        "name": "Google DeepMind Blog",
        "url": "https://deepmind.google/blog/rss.xml",
        "category": "Horizontal AI",
    },
    # ─── 競合動向：飲食 ──────────────────────────────────────
    {
        "name": "カカクコム (食べログ)",
        "url": "https://prtimes.jp/companyrdf.php?company_id=1455",
        "category": "競合：飲食",
        "keywords": AI_SERVICE_KEYWORDS,
    },
    {
        "name": "ぐるなび",
        "url": "https://prtimes.jp/companyrdf.php?company_id=1511",
        "category": "競合：飲食",
        "keywords": AI_SERVICE_KEYWORDS,
    },
    {
        "name": "Retty",
        "url": "https://prtimes.jp/companyrdf.php?company_id=4025",
        "category": "競合：飲食",
        "keywords": AI_SERVICE_KEYWORDS,
    },
    {
        "name": "トレタ",
        "url": "https://prtimes.jp/companyrdf.php?company_id=38464",
        "category": "競合：飲食",
        "keywords": AI_SERVICE_KEYWORDS,
    },
    {
        "name": "ダイニー",
        "url": "https://prtimes.jp/companyrdf.php?company_id=43056",
        "category": "競合：飲食",
        "keywords": AI_SERVICE_KEYWORDS,
    },
    # ─── 競合動向：住まい ────────────────────────────────────
    {
        "name": "LIFULL (HOME'S)",
        "url": "https://prtimes.jp/companyrdf.php?company_id=33058",
        "category": "競合：住まい",
        "keywords": AI_SERVICE_KEYWORDS,
    },
    {
        "name": "アットホーム",
        "url": "https://prtimes.jp/companyrdf.php?company_id=51123",
        "category": "競合：住まい",
        "keywords": AI_SERVICE_KEYWORDS,
    },
    {
        "name": "カナリー",
        "url": "https://prtimes.jp/companyrdf.php?company_id=46040",
        "category": "競合：住まい",
        "keywords": AI_SERVICE_KEYWORDS,
    },
    {
        "name": "イタンジ",
        "url": "https://prtimes.jp/companyrdf.php?company_id=14691",
        "category": "競合：住まい",
        "keywords": AI_SERVICE_KEYWORDS,
    },
    # ─── 競合動向：美容 ──────────────────────────────────────
    {
        "name": "MIXI (minimo)",
        "url": "https://prtimes.jp/companyrdf.php?company_id=25121",
        "category": "競合：美容",
        "keywords": AI_SERVICE_KEYWORDS,
    },
    {
        "name": "楽天グループ (楽天ビューティー)",
        "url": "https://prtimes.jp/companyrdf.php?company_id=5889",
        "category": "競合：美容",
        "keywords": AI_SERVICE_KEYWORDS,
    },
    # ─── 競合動向：自動車 ────────────────────────────────────
    {
        "name": "プロトコーポレーション (goo-net)",
        "url": "https://prtimes.jp/companyrdf.php?company_id=17791",
        "category": "競合：自動車",
        "keywords": AI_SERVICE_KEYWORDS,
    },
    # ─── 競合動向：旅行 ──────────────────────────────────────
    {
        "name": "楽天グループ (楽天トラベル)",
        "url": "https://prtimes.jp/companyrdf.php?company_id=5889",
        "category": "競合：旅行",
        "keywords": AI_SERVICE_KEYWORDS,
    },
    {
        "name": "Booking.com Japan",
        "url": "https://prtimes.jp/companyrdf.php?company_id=15916",
        "category": "競合：旅行",
        "keywords": AI_SERVICE_KEYWORDS,
    },
    {
        "name": "エクスペディア",
        "url": "https://prtimes.jp/companyrdf.php?company_id=3373",
        "category": "競合：旅行",
        "keywords": AI_SERVICE_KEYWORDS,
    },
    {
        "name": "Agoda",
        "url": "https://prtimes.jp/companyrdf.php?company_id=152576",
        "category": "競合：旅行",
        "keywords": AI_SERVICE_KEYWORDS,
    },
]

