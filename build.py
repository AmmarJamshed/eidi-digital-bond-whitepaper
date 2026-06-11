from pathlib import Path

import markdown

ROOT = Path(__file__).parent
MD_PATH = ROOT / "white-paper.md"
OUT_PATH = ROOT / "index.html"

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Eidi Digital Bond Program (EDBP) — White Paper</title>
  <meta name="description" content="Policy white paper on Pakistan's Eidi Digital Bond Program: trend analysis, fiscal impact, RAAST integration, and implementation roadmap for banking, government, and research." />
  <meta name="author" content="Eidi Digital Bond Program" />
  <meta property="og:title" content="Eidi Digital Bond Program — White Paper" />
  <meta property="og:description" content="A modern way to replace cash Eidi with digital bonds while increasing financial inclusion in Pakistan." />
  <meta property="og:type" content="article" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Source+Serif+4:opsz,wght@8..60,400;8..60,600;8..60,700&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="styles.css" />
</head>
<body>
  <header class="site-header">
    <div class="container header-inner">
      <div class="brand">
        <span class="brand-badge">Policy White Paper</span>
        <h1>Eidi Digital Bond Program</h1>
        <p class="subtitle">Trend Analysis · Policy Framework · Implementation Roadmap</p>
      </div>
      <div class="header-meta">
        <span>Version 1.0</span>
        <span>June 2026</span>
        <a class="btn" href="white-paper.pdf" download>Download PDF</a>
      </div>
    </div>
  </header>

  <nav class="toc-bar" aria-label="On this page">
    <div class="container">
      <span class="toc-label">Jump to:</span>
      <a href="#executive-summary">Executive Summary</a>
      <a href="#1-introduction--cultural-economic-context">Introduction</a>
      <a href="#3-global--regional-trend-analysis">Trends</a>
      <a href="#13-implementation-roadmap-18-months">Roadmap</a>
      <a href="#16-policy-recommendations">Policy</a>
      <a href="#references--sources">Sources</a>
    </div>
  </nav>

  <main class="container article">
    {content}
  </main>

  <footer class="site-footer">
    <div class="container">
      <p>Public document for policy, banking, research, and implementation use.</p>
      <p class="muted">Prepared for State Bank of Pakistan, Ministry of Finance, commercial banks, fintechs, academia, and development partners.</p>
    </div>
  </footer>
</body>
</html>
"""


def slugify_heading(text: str) -> str:
    return (
        text.lower()
        .replace("—", "-")
        .replace("–", "-")
        .replace("&", "")
        .replace("'", "")
        .replace("(", "")
        .replace(")", "")
        .replace(",", "")
        .replace(".", "")
        .replace(":", "")
        .strip()
        .replace(" ", "-")
    )


def add_heading_ids(html: str) -> str:
    import re

    def replacer(match: re.Match[str]) -> str:
        level = match.group(1)
        title = match.group(2)
        anchor = slugify_heading(title)
        return f'<h{level} id="{anchor}">{title}</h{level}>'

    return re.sub(r"<h([1-6])>(.*?)</h\1>", replacer, html)


def main() -> None:
    md_text = MD_PATH.read_text(encoding="utf-8")
    html_body = markdown.markdown(
        md_text,
        extensions=["tables", "fenced_code", "toc", "sane_lists"],
    )
    html_body = add_heading_ids(html_body)
    html_body = html_body.replace(
        "<h2>Executive Summary</h2>",
        '<h2 id="executive-summary">Executive Summary</h2>',
    )
    OUT_PATH.write_text(HTML_TEMPLATE.format(content=html_body), encoding="utf-8")
    print(f"Built {OUT_PATH}")


if __name__ == "__main__":
    main()
