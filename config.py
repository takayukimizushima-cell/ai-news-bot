"""
RSSãã£ã¼ãè¨­å®
å¿è¦ã«å¿ãã¦ãã£ã¼ãã®è¿½å ã»åé¤ãè¡ã£ã¦ãã ããã

keywords ãã£ã¼ã«ãï¼ãªãã·ã§ã³ï¼:
  æå®ããå ´åãè¨äºã¿ã¤ãã«ã«ããããã®ã­ã¼ã¯ã¼ããå«ã¾ãããã®ã ããå¯¾è±¡ã«ãã¾ãã
  PR Times ã®ããã«å¨ãã¬ã¹ãªãªã¼ã¹ãæµãããã£ã¼ãã§é¢é£è¨äºã ããæ¾ãã®ã«ä½¿ãã¾ãã
"""

# ââ ã­ã¼ã¯ã¼ãå®ç¾© ââââââââââââââââââââââââââââââââââââââââââââââââââââââ

# ç«¶åä¼æ¥­ãã£ã¼ãç¨: ãµã¼ãã¹ã¸ã®AIçµã¿è¾¼ã¿ã»æ©è½ãªãªã¼ã¹è¦³ç¹
AI_SERVICE_KEYWORDS = [
    # AIæ´»ç¨ã»å°å¥
    "AIæ­è¼", "AIæ©è½", "AIæ´»ç¨", "AIå°å¥", "AIå¯¾å¿", "AIé£æº",
    "AIå®è£", "AIãæ´»ç¨", "AIã«ãã",
    # çæAI / LLM å·ä½å
    "çæAI", "ChatGPT", "GPT", "Claude", "Gemini", "Copilot",
    "LLM", "å¤§è¦æ¨¡è¨èªã¢ãã«",
    # æ©è½ç³»
    "AIã¢ã·ã¹ã¿ã³ã", "AIã¨ã¼ã¸ã§ã³ã", "AIãã£ãã", "ãã£ããããã",
    "AIæ¤ç´¢", "AIã¬ã³ã¡ã³ã", "AIåæ", "AIäºæ¸¬", "AIç¿»è¨³",
    "AIæ»å®", "AIæ¥å®¢", "AIææ¡", "AIãããã³ã°",
    "èªåçæ", "èªåå¿ç­", "èªåç¿»è¨³",
    "ãã¼ã½ãã©ã¤ãº", "ã¬ã³ã¡ã³ãã¼ã·ã§ã³",
    # æè¡ç³»
    "ç»åèªè­", "é³å£°èªè­", "èªç¶è¨èªå¦ç", "æ©æ¢°å­¦ç¿",
    "OCR", "ãã£ã¼ãã©ã¼ãã³ã°",
]

# ä¸è¬AIãã¥ã¼ã¹ãã£ã¼ãç¨: ãã­ãã¯ãã»æ©è½å¯ãã®ã­ã¼ã¯ã¼ã
AI_PRODUCT_KEYWORDS = [
    # æ©è½ãªãªã¼ã¹ç³»
    "launch", "release", "feature", "update", "announce",
    "tool", "API", "plugin", "integration",
    # AI ãã­ãã¯ã
    "ChatGPT", "GPT-4", "GPT-5", "Claude", "Gemini", "Copilot",
    "Sora", "DALL-E", "Midjourney", "Stable Diffusion",
    "agent", "assistant", "search", "coding",
    # æ¥æ¬èªã­ã¼ã¯ã¼ãï¼å½åãã¥ã¼ã¹ç¨ï¼
    "æ°æ©è½", "æä¾éå§", "ãªãªã¼ã¹", "ã¢ãããã¼ã",
    "AIæ­è¼", "AIæ´»ç¨", "AIæ©è½", "çæAI",
    "AIã¨ã¼ã¸ã§ã³ã", "AIã¢ã·ã¹ã¿ã³ã",
]

# ã«ã¹ã¿ãã¼AIååç¨: èª¿æ»ã¬ãã¼ãã»å©ç¨å®æç³»ã­ã¼ã¯ã¼ã
AI_CONSUMER_KEYWORDS = [
    # èª¿æ»ã»ã¬ãã¼ãç³»
    "èª¿æ»", "ã¬ãã¼ã", "ç½æ¸", "å®æèª¿æ»", "æè­èª¿æ»", "ã¢ã³ã±ã¼ã",
    "èª¿æ»çµæ", "èª¿æ»ã¬ãã¼ã", "å©ç¨ååèª¿æ»",
    # AIå©ç¨ã»åå
    "AIå©ç¨", "AIæ´»ç¨", "AIåå", "AIæ®å", "AIæµ¸é",
    "å©ç¨ç", "å©ç¨åå", "å©ç¨å®æ", "å©ç¨æå",
    "çæAIå©ç¨", "çæAIæ´»ç¨", "ChatGPTå©ç¨",
    # ã¦ã¼ã¶ã¼ã»æ¶è²»è
    "æ¶è²»è", "ã¦ã¼ã¶ã¼", "çæ´»è", "åäººå©ç¨",
    # ãã¬ã³ã
    "AI adoption", "AI survey", "AI usage", "AI trend",
    # æµ·å¤ã¬ãã¼ãç¨ã­ã¼ã¯ã¼ã
    "report", "survey", "research", "study", "forecast",
    "consumer", "adoption", "workforce", "enterprise",
    "generative AI", "gen AI", "AI index",
]

# AIæè³ã»ãã¼ã±ããååç¨: VCã»ã¢ããªã¹ãã»ã³ã³ãµã«ç³»ã­ã¼ã¯ã¼ã
AI_MARKET_KEYWORDS = [
    # æè³ã»è³éèª¿é
    "AI investment", "AI funding", "AI startup", "AI venture",
    "fundraise", "Series A", "Series B", "valuation",
    "æè³", "è³éèª¿é", "åºè³", "AIå¸å ´",
    # ãã¼ã±ããåæ
    "market", "trend", "forecast", "outlook", "prediction",
    "landscape", "ecosystem", "disruption",
    "AI market", "AI industry", "AI sector",
    # ãã¬ã³ãã»æ¦ç¥
    "AI strategy", "AI transformation", "AI roadmap",
    "AI infrastructure", "AI platform", "AI stack",
    "frontier model", "foundation model", "AI agent",
    "generative AI", "gen AI", "LLM",
    # æ¥æ¬èªã­ã¼ã¯ã¼ã
    "AIæ¦ç¥", "AIæè³", "AIå¸å ´", "AIãã¬ã³ã",
    "çæAI", "AIã¨ã¼ã¸ã§ã³ã", "AIã¹ã¿ã¼ãã¢ãã",
]

RSS_FEEDS = [
    # âââ æµ·å¤AIãã¥ã¼ã¹ âââââââââââââââââââââââââââââââââââââââââââââââââ
    {
        "name": "TechCrunch AI",
        "url": "https://techcrunch.com/category/artificial-intelligence/feed/",
        "category": "æµ·å¤AI",
        "keywords": AI_PRODUCT_KEYWORDS,
    },
    {
        "name": "The Verge AI",
        "url": "https://www.theverge.com/ai-artificial-intelligence/rss/index.xml",
        "category": "æµ·å¤AI",
        "keywords": AI_PRODUCT_KEYWORDS,
    },
    {
        "name": "VentureBeat AI",
        "url": "https://venturebeat.com/category/ai/feed/",
        "category": "æµ·å¤AI",
        "keywords": AI_PRODUCT_KEYWORDS,
    },
    {
        "name": "WIRED AI",
        "url": "https://www.wired.com/feed/tag/ai/latest/rss",
        "category": "æµ·å¤AI",
        "keywords": AI_PRODUCT_KEYWORDS,
    },
    # âââ å½åAIãã¥ã¼ã¹ âââââââââââââââââââââââââââââââââââââââââââââââââ
    {
        "name": "ITmedia AI+",
        "url": "https://rss.itmedia.co.jp/rss/2.0/aiplus.xml",
        "category": "å½åAI",
        "keywords": AI_PRODUCT_KEYWORDS,
    },
    {
        "name": "Ledge.ai",
        "url": "https://ledge.ai/feed/",
        "category": "å½åAI",
        "keywords": AI_PRODUCT_KEYWORDS,
    },
    {
        "name": "AINOW",
        "url": "https://ainow.ai/feed/",
        "category": "å½åAI",
        "keywords": AI_PRODUCT_KEYWORDS,
    },
    {
        "name": "Impress Watch",
        "url": "https://www.watch.impress.co.jp/data/rss/1.0/ipw/feed.rdf",
        "category": "å½åAI",
        "keywords": AI_PRODUCT_KEYWORDS,
    },
    # âââ Horizontal AIï¼ã©ã / ãã©ãããã©ã¼ã ï¼ ââââââââââââââââââââââ
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
    # âââ ç«¶åååï¼é£²é£ ââââââââââââââââââââââââââââââââââââââââââââââââ
    {
        "name": "ã«ã«ã¯ã³ã  (é£ã¹ã­ã°)",
        "url": "https://prtimes.jp/companyrdf.php?company_id=1455",
        "category": "ç«¶åï¼é£²é£",
        "keywords": AI_SERVICE_KEYWORDS,
    },
    {
        "name": "ãããªã³",
        "url": "https://prtimes.jp/companyrdf.php?company_id=1511",
        "category": "ç«¶åï¼é£²é£",
        "keywords": AI_SERVICE_KEYWORDS,
    },
    {
        "name": "Retty",
        "url": "https://prtimes.jp/companyrdf.php?company_id=4025",
        "category": "ç«¶åï¼é£²é£",
        "keywords": AI_SERVICE_KEYWORDS,
    },
    {
        "name": "ãã¬ã¿",
        "url": "https://prtimes.jp/companyrdf.php?company_id=38464",
        "category": "ç«¶åï¼é£²é£",
        "keywords": AI_SERVICE_KEYWORDS,
    },
    {
        "name": "ãã¤ãã¼",
        "url": "https://prtimes.jp/companyrdf.php?company_id=43056",
        "category": "ç«¶åï¼é£²é£",
        "keywords": AI_SERVICE_KEYWORDS,
    },
    # âââ ç«¶åååï¼ä½ã¾ã ââââââââââââââââââââââââââââââââââââââââââââââ
    {
        "name": "LIFULL (HOME'S)",
        "url": "https://prtimes.jp/companyrdf.php?company_id=33058",
        "category": "ç«¶åï¼ä½ã¾ã",
        "keywords": AI_SERVICE_KEYWORDS,
    },
    {
        "name": "ã¢ãããã¼ã ",
        "url": "https://prtimes.jp/companyrdf.php?company_id=51123",
        "category": "ç«¶åï¼ä½ã¾ã",
        "keywords": AI_SERVICE_KEYWORDS,
    },
    {
        "name": "ã«ããªã¼",
        "url": "https://prtimes.jp/companyrdf.php?company_id=46040",
        "category": "ç«¶åï¼ä½ã¾ã",
        "keywords": AI_SERVICE_KEYWORDS,
    },
    {
        "name": "ã¤ã¿ã³ã¸",
        "url": "https://prtimes.jp/companyrdf.php?company_id=14691",
        "category": "ç«¶åï¼ä½ã¾ã",
        "keywords": AI_SERVICE_KEYWORDS,
    },
    # âââ ç«¶åååï¼ç¾å®¹ ââââââââââââââââââââââââââââââââââââââââââââââââ
    {
        "name": "MIXI (minimo)",
        "url": "https://prtimes.jp/companyrdf.php?company_id=25121",
        "category": "ç«¶åï¼ç¾å®¹",
        "keywords": AI_SERVICE_KEYWORDS,
    },
    {
        "name": "æ¥½å¤©ã°ã«ã¼ã (æ¥½å¤©ãã¥ã¼ãã£ã¼)",
        "url": "https://prtimes.jp/companyrdf.php?company_id=5889",
        "category": "ç«¶åï¼ç¾å®¹",
        "keywords": AI_SERVICE_KEYWORDS,
    },
    # âââ ç«¶åååï¼èªåè» ââââââââââââââââââââââââââââââââââââââââââââââ
    {
        "name": "ãã­ãã³ã¼ãã¬ã¼ã·ã§ã³ (goo-net)",
        "url": "https://prtimes.jp/companyrdf.php?company_id=17791",
        "category": "ç«¶åï¼èªåè»",
        "keywords": AI_SERVICE_KEYWORDS,
    },
    # âââ ç«¶åååï¼æè¡ ââââââââââââââââââââââââââââââââââââââââââââââââ
    {
        "name": "æ¥½å¤©ã°ã«ã¼ã (æ¥½å¤©ãã©ãã«)",
        "url": "https://prtimes.jp/companyrdf.php?company_id=5889",
        "category": "ç«¶åï¼æè¡",
        "keywords": AI_SERVICE_KEYWORDS,
    },
    {
        "name": "Booking.com Japan",
        "url": "https://prtimes.jp/companyrdf.php?company_id=15916",
        "category": "ç«¶åï¼æè¡",
        "keywords": AI_SERVICE_KEYWORDS,
    },
    {
        "name": "ã¨ã¯ã¹ããã£ã¢",
        "url": "https://prtimes.jp/companyrdf.php?company_id=3373",
        "category": "ç«¶åï¼æè¡",
        "keywords": AI_SERVICE_KEYWORDS,
    },
    {
        "name": "Agoda",
        "url": "https://prtimes.jp/companyrdf.php?company_id=152576",
        "category": "ç«¶åï¼æè¡",
        "keywords": AI_SERVICE_KEYWORDS,
    },
    # âââ ã«ã¹ã¿ãã¼AIååï¼èª¿æ»ã»ã¬ãã¼ãï¼ ââââââââââââââââââââââââââââ
    {
        "name": "MMç·ç ",
        "url": "https://prtimes.jp/companyrdf.php?company_id=6717",
        "category": "ã«ã¹ã¿ãã¼AIåå",
        "keywords": AI_CONSUMER_KEYWORDS,
    },
    {
        "name": "ICTç·ç ",
        "url": "https://prtimes.jp/companyrdf.php?company_id=19182",
        "category": "ã«ã¹ã¿ãã¼AIåå",
        "keywords": AI_CONSUMER_KEYWORDS,
    },
    {
        "name": "é»éç·ç ",
        "url": "https://prtimes.jp/companyrdf.php?company_id=43138",
        "category": "ã«ã¹ã¿ãã¼AIåå",
        "keywords": AI_CONSUMER_KEYWORDS,
    },
    {
        "name": "ãã­ã¤ã ãã¼ãã",
        "url": "https://prtimes.jp/companyrdf.php?company_id=202",
        "category": "ã«ã¹ã¿ãã¼AIåå",
        "keywords": AI_CONSUMER_KEYWORDS,
    },
    {
        "name": "PwC Japan",
        "url": "https://prtimes.jp/companyrdf.php?company_id=29907",
        "category": "ã«ã¹ã¿ãã¼AIåå",
        "keywords": AI_CONSUMER_KEYWORDS,
    },
    {
        "name": "ããã­ã³ã¼ã¼",
        "url": "https://prtimes.jp/companyrdf.php?company_id=94688",
        "category": "ã«ã¹ã¿ãã¼AIåå",
        "keywords": AI_CONSUMER_KEYWORDS,
    },
    {
        "name": "æ¥çµã¯ã­ã¹ããã¯",
        "url": "https://xtech.nikkei.com/rss/xtech-it.rdf",
        "category": "ã«ã¹ã¿ãã¼AIåå",
        "keywords": AI_CONSUMER_KEYWORDS,
    },
    # âââ ã«ã¹ã¿ãã¼AIååï¼æµ·å¤ï¼èª¿æ»ã»ã¬ãã¼ãï¼ ââââââââââââââââââââââ
    {
        "name": "McKinsey Insights",
        "url": "https://www.mckinsey.com/insights/rss",
        "category": "ã«ã¹ã¿ãã¼AIåå",
        "keywords": AI_CONSUMER_KEYWORDS,
    },
    {
        "name": "Gartner Newsroom",
        "url": "https://www.gartner.com/en/newsroom/rss",
        "category": "ã«ã¹ã¿ãã¼AIåå",
        "keywords": AI_CONSUMER_KEYWORDS,
    },
    {
        "name": "Forrester Blog",
        "url": "https://www.forrester.com/blogs/feed/",
        "category": "ã«ã¹ã¿ãã¼AIåå",
        "keywords": AI_CONSUMER_KEYWORDS,
    },
    {
        "name": "Pew Research (Internet & Tech)",
        "url": "https://www.pewresearch.org/topic/internet-technology/feed/",
        "category": "ã«ã¹ã¿ãã¼AIåå",
        "keywords": AI_CONSUMER_KEYWORDS,
    },
    {
        "name": "Stanford HAI",
        "url": "https://hai.stanford.edu/news/rss.xml",
        "category": "ã«ã¹ã¿ãã¼AIåå",
        "keywords": AI_CONSUMER_KEYWORDS,
    },
    # âââ AIæè³ã»ãã¼ã±ããåå ââââââââââââââââââââââââââââââââââââââââ
    {
        "name": "a16z",
        "url": "https://a16z.com/feed/",
        "category": "AIæè³ã»ãã¼ã±ãã",
        "keywords": AI_MARKET_KEYWORDS,
    },
    {
        "name": "CB Insights",
        "url": "https://www.cbinsights.com/research/feed/",
        "category": "AIæè³ã»ãã¼ã±ãã",
        "keywords": AI_MARKET_KEYWORDS,
    },
    {
        "name": "Crunchbase News",
        "url": "https://news.crunchbase.com/feed/",
        "category": "AIæè³ã»ãã¼ã±ãã",
        "keywords": AI_MARKET_KEYWORDS,
    },
    {
        "name": "Benedict Evans",
        "url": "https://www.ben-evans.com/feed",
        "category": "AIæè³ã»ãã¼ã±ãã",
        "keywords": AI_MARKET_KEYWORDS,
    },
    {
        "name": "BCG",
        "url": "https://www.bcg.com/rss.xml",
        "category": "AIæè³ã»ãã¼ã±ãã",
        "keywords": AI_MARKET_KEYWORDS,
    },
    {
        "name": "Bain & Company",
        "url": "https://www.bain.com/insights/rss/",
        "category": "AIæè³ã»ãã¼ã±ãã",
        "keywords": AI_MARKET_KEYWORDS,
    },
]
