"""Compute the ratio of Top Reviewers to the full reviewer pool for a NeurIPS
Program Committee page.

The page structure has evolved over the years, so this script tries a few
different section labels:

    * 2023 uses  "Top Reviewers"  vs  "Technical Reviewers"
    * 2024 uses  "Top Reviewers"  vs  "All Reviewers"
    * 2025 uses  "Top Reviewers"  vs  "All Reviewers"   (inside <h2> instead of <h3>)

Usage:
    python scripts/neurips_top_reviewer_ratio.py                 # NeurIPS 2023
    python scripts/neurips_top_reviewer_ratio.py --year 2024
    python scripts/neurips_top_reviewer_ratio.py --year 2025
    python scripts/neurips_top_reviewer_ratio.py --years 2023 2024 2025
    python scripts/neurips_top_reviewer_ratio.py --url https://neurips.cc/Conferences/2023/ProgramCommittee
"""

from __future__ import annotations

import argparse
import sys
from typing import Iterable, Optional
from urllib.request import Request, urlopen

from bs4 import BeautifulSoup, NavigableString, Tag


DEFAULT_URL = "https://neurips.cc/Conferences/{year}/ProgramCommittee"

TOP_SECTION_LABELS = ("Top Reviewers",)
POOL_SECTION_LABELS = ("All Reviewers", "Technical Reviewers")

HEADING_TAGS = {"h1", "h2", "h3", "h4", "h5", "h6"}


def fetch_html(url: str) -> str:
    req = Request(url, headers={"User-Agent": "Mozilla/5.0 (neurips-stats)"})
    with urlopen(req, timeout=30) as resp:
        return resp.read().decode("utf-8", errors="replace")


def _normalize(text: str) -> str:
    return " ".join(text.split()).strip().lower()


def _find_heading(soup: BeautifulSoup, candidates: Iterable[str]) -> Optional[Tag]:
    wanted = {_normalize(c) for c in candidates}
    for tag in soup.find_all(list(HEADING_TAGS)):
        if _normalize(tag.get_text()) in wanted:
            return tag
    return None


def _iter_section_names(soup: BeautifulSoup, candidates: Iterable[str]) -> list[str]:
    start = _find_heading(soup, candidates)
    if start is None:
        raise ValueError(f"Section heading not found: {list(candidates)!r}")

    names: list[str] = []
    for node in start.find_all_next():
        if not isinstance(node, Tag):
            continue
        if node.name in HEADING_TAGS and _normalize(node.get_text()):
            if node is start:
                continue
            break
        classes = node.get("class") or []
        if "reviewer-block" in classes:
            names.extend(_extract_names(node))
    return names


def _extract_names(block: Tag) -> list[str]:
    names: list[str] = []
    buffer: list[str] = []

    def flush() -> None:
        joined = " ".join(part.strip() for part in buffer if part.strip())
        if joined:
            names.append(joined)
        buffer.clear()

    for node in block.descendants:
        if isinstance(node, NavigableString):
            text = str(node)
            if text.strip():
                buffer.append(text)
        elif isinstance(node, Tag) and node.name == "br":
            flush()
    flush()
    return names


def compute_for_url(url: str) -> tuple[list[str], list[str], str]:
    html = fetch_html(url)
    soup = BeautifulSoup(html, "html.parser")

    top = _iter_section_names(soup, TOP_SECTION_LABELS)

    pool: list[str] = []
    pool_label = ""
    last_err: Optional[Exception] = None
    for label in POOL_SECTION_LABELS:
        try:
            pool = _iter_section_names(soup, [label])
            pool_label = label
            break
        except ValueError as exc:
            last_err = exc
    if not pool_label:
        raise ValueError(
            f"Could not find any reviewer-pool section on {url}. "
            f"Tried: {list(POOL_SECTION_LABELS)}"
        ) from last_err

    return top, pool, pool_label


def _print_report(url: str, top: list[str], pool: list[str], pool_label: str) -> None:
    print(f"Source: {url}")
    print(f"Top Reviewers:         {len(top)}")
    print(f"{pool_label + ':':<22} {len(pool)}")
    if len(pool):
        print(f"Top / {pool_label}:   {len(top) / len(pool):.4%}")
    total = len(top) + len(pool)
    if total and pool_label != "All Reviewers":
        print(f"Top / (Top + {pool_label}): {len(top) / total:.4%}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--year", type=int, default=None, help="Conference year (defaults to 2023)")
    parser.add_argument("--years", type=int, nargs="+", help="Compute for multiple years in one call")
    parser.add_argument("--url", type=str, default=None, help="Override the program committee URL")
    parser.add_argument(
        "--dump",
        choices=["top", "pool", "none"],
        default="none",
        help="Optionally print the full name list for one of the sections",
    )
    args = parser.parse_args()

    urls: list[str]
    if args.url:
        urls = [args.url]
    elif args.years:
        urls = [DEFAULT_URL.format(year=y) for y in args.years]
    else:
        urls = [DEFAULT_URL.format(year=args.year or 2023)]

    for i, url in enumerate(urls):
        if i:
            print()
        top, pool, pool_label = compute_for_url(url)
        _print_report(url, top, pool, pool_label)

        if args.dump == "top":
            print("\n--- Top Reviewers ---")
            print("\n".join(top))
        elif args.dump == "pool":
            print(f"\n--- {pool_label} ---")
            print("\n".join(pool))

    return 0


if __name__ == "__main__":
    sys.exit(main())
