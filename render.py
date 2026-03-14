#!/usr/bin/env python3
"""Render letter.tex from letter.yaml and template.tex.j2."""

import sys
from pathlib import Path

import yaml
from jinja2 import Environment, FileSystemLoader, StrictUndefined

DEFAULTS = {
    "show_isc_logo": True,
    "show_signature": False,
    "date_iso": "",
    "signature": "",
    "endorser": "",
    "city": "Sion",
    "pdf_author": "",
    "pdf_title": "",
    "pdf_subject": "",
    "title": {"en": "", "fr": ""},
    "subtitle": {"en": "", "fr": ""},
    "greeting": {"en": "", "fr": ""},
    "closing": {"en": "", "fr": ""},
    "endorsement_label": {
        "en": "",
        "fr": "",
    },
}


def main():
    yaml_path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("letter.yaml")
    data = yaml.safe_load(yaml_path.read_text())

    # Merge defaults (shallow, then nested dicts)
    context = {**DEFAULTS, **data}
    for key, default in DEFAULTS.items():
        if isinstance(default, dict):
            context[key] = {**default, **(data.get(key) or {})}

    # Strip trailing whitespace from body
    if "body" in context:
        context["body"] = context["body"].rstrip()

    env = Environment(
        loader=FileSystemLoader(Path(__file__).resolve().parent),
        variable_start_string="<<",
        variable_end_string=">>",
        block_start_string="<%",
        block_end_string="%>",
        comment_start_string="<#",
        comment_end_string="#>",
        trim_blocks=True,
        lstrip_blocks=True,
        undefined=StrictUndefined,
    )

    template = env.get_template("template.tex.j2")
    Path("letter.tex").write_text(template.render(context))
    print("Rendered letter.tex")


if __name__ == "__main__":
    main()
