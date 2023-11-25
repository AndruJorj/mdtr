#!/usr/bin/env python3

import argparse
from rich.console import Console
from rich.markdown import Markdown
from pathlib import Path

def render_markdown(text, use_color=True):
    """Render Markdown text with color option."""
    console = Console(force_terminal=use_color)
    console.print(Markdown(text))

def read_markdown_file(file_path):
    """Read Markdown content from a file."""
    with open(file_path, "r") as file:
        return file.read()

def main():
    parser = argparse.ArgumentParser(description="Render Markdown in the terminal")
    parser.add_argument("file", nargs="?", help="Markdown file to render")
    parser.add_argument(
        "--no-color",
        action="store_true",
        help="Disable color output for terminal",
    )
    
    args = parser.parse_args()

    if args.file:
        markdown_text = read_markdown_file(args.file)
        render_markdown(markdown_text, not args.no_color)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
