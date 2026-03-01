# Agent Instructions

- Commits must follow the Conventional Commits specification:
  https://www.conventionalcommits.org/en/v1.0.0/
- PRs titles follow Conventional Commits specifications for the message subject,
  writing the type in upper case and dropping the scope parenthetical (e.g., FIX: <description-headline>).
- Test every task:
   - Render the template: `pixi run render`
   - Lint with chktex: `pixi run lint`
   - Build the PDF: `pixi run build`
