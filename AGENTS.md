# Agent Instructions

- Commits must follow the Conventional Commits specification:
  https://www.conventionalcommits.org/en/v1.0.0/
- PRs titles follow Conventional Commits specifications for the message subject,
  writing the type in upper case and dropping the scope parenthetical (e.g., FIX: <description-headline>).
- Test every task:
   - First with the linter: `chktex -q -n1 -n2 -n8 -n24 -n26 template.tex`
   - Then building: `latexmk -pdf -interaction=nonstopmode -halt-on-error -xelatex template.tex`
