#!/usr/bin/env python3
"""Render {{token}} placeholders in IFU/label pages using config.json."""
import argparse
import json
import sys
import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
CONFIG_PATH = REPO_ROOT / "config.json"
SOURCE_DIR = REPO_ROOT / "ifu" / "ll-ifu"

TOKEN_PATTERN = re.compile(r"\{\{(\w+)\}\}")
LANG_SUFFIXES = ["es-LAT", "de", "es", "fr", "it", "nl", "th"]


def detect_lang(stem):
    for suffix in LANG_SUFFIXES:
        if stem.endswith(f"-{suffix}"):
            return suffix
    return "en"


def resolve_token(config, token, lang, filename):
    if token == "changeControl":
        return config["changeControl"][lang]
    if token not in config:
        raise KeyError(f"Unresolved token {{{{{token}}}}} in {filename}")
    return config[token]


def render_content(content, config, lang, filename):
    def replace(match):
        return resolve_token(config, match.group(1), lang, filename)
    return TOKEN_PATTERN.sub(replace, content)


def main():
    parser = argparse.ArgumentParser(description="Render config.json values into tokenized IFU/label pages.")
    parser.add_argument("--check", action="store_true", help="Verify all tokens resolve without writing any files.")
    args = parser.parse_args()

    config = json.loads(CONFIG_PATH.read_text(encoding="utf-8"))
    errors = []

    for path in sorted(SOURCE_DIR.glob("*.html")):
        content = path.read_text(encoding="utf-8")
        if not content.strip():
            continue  # skip empty files (e.g. us-en)
        lang = detect_lang(path.stem)
        try:
            rendered = render_content(content, config, lang, path.name)
        except KeyError as e:
            errors.append(str(e))
            continue
        if not args.check:
            path.write_text(rendered, encoding="utf-8")
        print(f"{'Checked' if args.check else 'Rendered'} {path.name} ({lang})")

    if errors:
        for e in errors:
            print(f"ERROR: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
