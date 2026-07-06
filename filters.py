"""
競合ニュース関連度フィルタ

「国内競合ニュース」「海外競合ニュース」カテゴリは Google News のキーワード検索で
記事を集めているため、会社名が本文や引用元に含まれるだけの無関係な記事
（コラボメニュー、自動車の新型車情報、株式の売買報告など）を大量に拾ってしまう。

このモジュールは Claude (Anthropic API) を使って、各記事が下記の採用基準に
該当するかどうかを意味的に判定し、該当しない記事を除外する。
"""

import json
import logging
import os

logger = logging.getLogger(__name__)

# フィルタ対象のカテゴリ（このカテゴリの記事だけを Claude に判定させる）
FILTER_CATEGORIES = {"国内競合ニュース", "海外競合ニュース"}

CLAUDE_MODEL = os.environ.get("ANTHROPIC_MODEL", "claude-haiku-4-5-20251001")

SYSTEM_PROMPT = """あなたは競合分析の担当者です。競合企業に関するニュース記事一覧が渡されるので、
以下の採用基準に沿って「配信する価値がある」記事だけを選んでください。

# 採用基準（いずれかに該当すれば採用）
1. 競合企業のビジネスに関するプレスリリース（新サービス、事業提携、資金調達、M&A、
   上場・非公開化、経営体制の変更、新規事業の開始・撤退など）
2. 売上や株価に影響を与えうるニュース（決算・業績修正、大型契約、規制・訴訟、
   格付け変更、重大なインシデントなど）
3. 競合企業に関する分析・考察（Findings）を含むニュース（競合の戦略・市場ポジション・
   財務状況についての第三者による分析記事）

# 除外する記事の例
- 特定店舗のコラボメニューやキャンペーンなど、その企業のコーポレートニュースと無関係な一般記事
- 自動車の新型車情報・試乗記事・旧型車紹介など、企業名が情報源として引用されているだけの記事
- 個人投資家・機関投資家の株式売買（保有株数の増減）を機械的に報告するだけの記事
- 単なる商品レビュー、ランキング記事、趣味的なコンテンツ

出力は与えられた記事の "id" のうち、採用すべきものだけを含む JSON 配列で返してください。
例: [0, 3, 5]
記事が1件も採用基準を満たさない場合は空配列 [] を返してください。
説明文やコードフェンスは一切不要で、JSON 配列のみを出力してください。
"""


def filter_articles(articles: list[dict]) -> list[dict]:
    """国内/海外競合ニュースのみ Claude で関連度判定する。それ以外はそのまま通す。

    ANTHROPIC_API_KEY が未設定、または API 呼び出しに失敗した場合は
    フィルタをスキップして全件そのまま返す（配信が止まらないようにするため）。
    """
    targets = [a for a in articles if a.get("category") in FILTER_CATEGORIES]
    others = [a for a in articles if a.get("category") not in FILTER_CATEGORIES]

    if not targets:
        return articles

    api_key = os.environ.get("ANTHROPIC_API_KEY", "")
    if not api_key:
        logger.warning("ANTHROPIC_API_KEY 未設定のため競合ニュースフィルタをスキップします。")
        return articles

    try:
        import anthropic
    except ImportError:
        logger.warning("anthropic パッケージ未インストールのためフィルタをスキップします。")
        return articles

    items = [
        {"id": i, "company": a.get("source", ""), "title": a.get("title", "")}
        for i, a in enumerate(targets)
    ]
    items_json = json.dumps(items, ensure_ascii=False)

    try:
        client = anthropic.Anthropic(api_key=api_key)
        resp = client.messages.create(
            model=CLAUDE_MODEL,
            max_tokens=1024,
            system=SYSTEM_PROMPT,
            messages=[
                {
                    "role": "user",
                    "content": f"以下の記事一覧を判定してください。\n{items_json}",
                }
            ],
        )
        raw = resp.content[0].text.strip()

        # ```json ... ``` のようなコードフェンスが付いた場合に備えて除去
        if raw.startswith("```"):
            raw = raw.strip("`")
            if "\n" in raw:
                raw = raw.split("\n", 1)[1]
            if "```" in raw:
                raw = raw.rsplit("```", 1)[0]

        keep_ids = set(json.loads(raw))
    except Exception as e:
        logger.warning(f"競合ニュースフィルタ判定に失敗しました。全件残します: {e}")
        return articles

    kept = [a for i, a in enumerate(targets) if i in keep_ids]
    logger.info(f"競合ニュースフィルタ: {len(targets)} 件 → {len(kept)} 件に絞り込み")
    return others + kept
