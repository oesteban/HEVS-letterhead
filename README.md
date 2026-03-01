# HES-SO Letterhead

LaTeX letterhead template for HES-SO Valais-Wallis / School of Engineering (HEI).

Letter content is defined in a YAML file (`letter.yaml`), rendered into `letter.tex`
via Jinja2, and compiled to PDF with XeLaTeX.

## Quick start

1. Install [pixi](https://pixi.sh)
2. Copy the example and edit your letter content:

   ```sh
   cp letter.yaml.example letter.yaml
   # edit letter.yaml with your content
   ```

3. Render, lint, and build in one step:

   ```sh
   pixi run all
   ```

The output is `letter.pdf`.

## Step-by-step tasks

| Task | Command | Description |
|------|---------|-------------|
| Render | `pixi run render` | Render `letter.yaml` → `letter.tex` |
| Lint | `pixi run lint` | Run chktex on `letter.tex` (renders first) |
| Build | `pixi run build` | Compile `letter.tex` → `letter.pdf` (renders first) |
| Clean | `pixi run clean` | Remove generated files |
| All | `pixi run all` | Render + lint + build |

## Platforms

The pixi environment is configured for **linux-64** and **osx-arm64**.

## Configuration

### Language

Set `language` in `letter.yaml` to `english` or `french`. The template handles
date formatting and localized strings automatically.

### ISC logo

Set `show_isc_logo: true` in `letter.yaml` to display the ISC logo in the header.

### Signature

To include a handwritten signature:

1. Place `signature.png` in the project root (git-ignored by default)
2. Set `show_signature: true` in `letter.yaml`
3. Optionally set `signature:` to the signer's printed name

### Endorsement

To add an endorser alongside the signature, set both `signature` and `endorser`
fields in `letter.yaml`.

## Manual build (without pixi)

Install these system packages (Debian/Ubuntu):

- texlive-latex-base, texlive-latex-recommended, texlive-fonts-recommended
- texlive-latex-extra, texlive-xetex
- latexmk, chktex, inkscape
- python3, python3-jinja2, python3-yaml

Then run:

```sh
cp letter.yaml.example letter.yaml
python3 render.py
chktex -q -n1 -n2 -n8 -n24 -n26 letter.tex
latexmk -pdf -interaction=nonstopmode -halt-on-error -xelatex -shell-escape letter.tex
```

## Fonts

This template uses the Arimo sans-serif family from Google Fonts. The TTF files
are included in `fonts/`:

- `Arimo-Regular.ttf`
- `Arimo-Bold.ttf`
- `Arimo-Italic.ttf`
- `Arimo-BoldItalic.ttf`
