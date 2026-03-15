# Growth SEO OS Docs

## Install

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run locally

```bash
mkdocs serve
```

## Build

```bash
mkdocs build --clean --strict
```

## Language switcher

This documentation is configured with `mkdocs-static-i18n` and supports:

- English (`en`)
- Tiếng Việt (`vi`)

Vietnamese core pages are translated; untranslated pages automatically fall back to English.
