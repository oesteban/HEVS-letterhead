# HES-SO Letterhead

## Local build dependencies

To build the PDF and run linting locally, install these packages (Debian/Ubuntu names):

- texlive-latex-base
- texlive-latex-recommended
- texlive-fonts-recommended
- texlive-latex-extra
- texlive-xetex
- latexmk
- chktex
- inkscape

Then run:

```sh
chktex -q -n1 -n2 -n8 -n24 -n26 template.tex
latexmk -pdf -interaction=nonstopmode -halt-on-error -xelatex -shell-escape template.tex
```

To enable the ISC logo in the header, toggle it in the TeX source or pass it on the command line:

```sh
pdflatex "\showisclogotrue\input{template.tex}"
latexmk -xelatex -use-make -latexoption="\\showisclogotrue" template.tex
```

Note: the `svg` package requires `-shell-escape` so LaTeX can run Inkscape during the build.
If you run latexmk without the command above, make sure your `latexmkrc` includes `-shell-escape`
and that Inkscape is installed so `svg` conversions succeed.

## Fonts

This template uses the Arimo sans-serif family from Google Fonts. Place these TTF files in
`fonts/` (already included in this repository):

- `Arimo-Regular.ttf`
- `Arimo-Bold.ttf`
- `Arimo-Italic.ttf`
- `Arimo-BoldItalic.ttf`
