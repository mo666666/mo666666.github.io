#!/usr/bin/env python3
"""Generate static Google Scholar citation assets."""

from __future__ import annotations

import datetime as dt
import html
import re
import sys
import urllib.parse
import urllib.request
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent.parent
CONFIG_PATH = REPO_ROOT / "_config.yml"
BADGE_PATH = REPO_ROOT / "images" / "google-scholar-citations.svg"
DATA_PATH = REPO_ROOT / "_data" / "google_scholar.yml"


def read_google_scholar_url() -> str:
    content = CONFIG_PATH.read_text(encoding="utf-8")
    match = re.search(r'^\s*googlescholar\s*:\s*"([^"]+)"\s*$', content, re.MULTILINE)
    if match:
        return match.group(1)

    match = re.search(r"^\s*googlescholar\s*:\s*'([^']+)'\s*$", content, re.MULTILINE)
    if match:
        return match.group(1)

    raise RuntimeError("Could not find googlescholar URL in _config.yml")


def extract_user_id(scholar_url: str) -> str:
    parsed = urllib.parse.urlparse(scholar_url)
    user_id = urllib.parse.parse_qs(parsed.query).get("user", [""])[0]
    if not user_id:
        raise RuntimeError("Could not extract Scholar user ID from googlescholar URL")
    return user_id


def fetch_profile_html(user_id: str) -> str:
    profile_url = f"https://scholar.google.com/citations?user={user_id}&hl=en"
    request = urllib.request.Request(
        profile_url,
        headers={
            "User-Agent": (
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/123.0.0.0 Safari/537.36"
            ),
            "Accept-Language": "en-US,en;q=0.9",
        },
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        return response.read().decode("utf-8", errors="ignore")


def extract_total_citations(html_text: str) -> int:
    matches = re.findall(r'<td class="gsc_rsb_std">([0-9,]+)</td>', html_text)
    if matches:
        return int(matches[0].replace(",", ""))

    # Fallback for slightly different markup variants.
    matches = re.findall(r'>Citations</td>\s*<td[^>]*>([0-9,]+)</td>', html_text, re.IGNORECASE)
    if matches:
        return int(matches[0].replace(",", ""))

    raise RuntimeError("Could not locate total citations in Google Scholar profile HTML")


def estimate_text_width(text: str, font_size: int, bold: bool = False) -> int:
    average = 8.6 if bold else 7.2
    return int(len(text) * average + 10)


def build_badge_svg(label: str, message: str) -> str:
    left_width = max(78, estimate_text_width(label, 11, bold=False))
    right_width = max(46, estimate_text_width(message, 11, bold=True))
    total_width = left_width + right_width

    label_escaped = html.escape(label)
    message_escaped = html.escape(message)

    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{total_width}" height="20" role="img" aria-label="{label_escaped}: {message_escaped}">
  <title>{label_escaped}: {message_escaped}</title>
  <linearGradient id="smooth" x2="0" y2="100%">
    <stop offset="0" stop-color="#fff" stop-opacity=".7"/>
    <stop offset=".1" stop-color="#aaa" stop-opacity=".1"/>
    <stop offset=".9" stop-color="#000" stop-opacity=".3"/>
    <stop offset="1" stop-color="#000" stop-opacity=".5"/>
  </linearGradient>
  <clipPath id="round">
    <rect width="{total_width}" height="20" rx="3" fill="#fff"/>
  </clipPath>
  <g clip-path="url(#round)">
    <rect width="{left_width}" height="20" fill="#555"/>
    <rect x="{left_width}" width="{right_width}" height="20" fill="#4285f4"/>
    <rect width="{total_width}" height="20" fill="url(#smooth)"/>
  </g>
  <g fill="#fff" text-anchor="middle" font-family="DejaVu Sans,Verdana,Geneva,sans-serif" text-rendering="geometricPrecision" font-size="11">
    <text x="{left_width / 2:.1f}" y="15" fill="#010101" fill-opacity=".3">{label_escaped}</text>
    <text x="{left_width / 2:.1f}" y="14">{label_escaped}</text>
    <text x="{left_width + right_width / 2:.1f}" y="15" fill="#010101" fill-opacity=".3">{message_escaped}</text>
    <text x="{left_width + right_width / 2:.1f}" y="14" font-weight="700">{message_escaped}</text>
  </g>
</svg>
"""


def main() -> int:
    scholar_url = read_google_scholar_url()
    user_id = extract_user_id(scholar_url)
    profile_html = fetch_profile_html(user_id)
    citations = extract_total_citations(profile_html)

    BADGE_PATH.parent.mkdir(parents=True, exist_ok=True)
    BADGE_PATH.write_text(
        build_badge_svg("citations", f"{citations:,}"),
        encoding="utf-8",
    )

    updated_at = dt.datetime.now(dt.timezone.utc).isoformat()
    DATA_PATH.parent.mkdir(parents=True, exist_ok=True)
    DATA_PATH.write_text(
        f"citations: {citations}\nupdated_at: '{updated_at}'\n",
        encoding="utf-8",
    )

    print(f"Updated Google Scholar assets with {citations} citations at {updated_at}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
