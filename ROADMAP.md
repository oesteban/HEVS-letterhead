# Roadmap

## Near-term: polish what's there

- ~~**Matrix CI**: test both `language: english` and `language: french` in the
  workflow, plus edge cases like `show_signature: true` and endorser enabled.
  Currently CI only exercises one configuration.~~ **Done.**
- **Schema documentation**: maintain a JSON Schema for `letter.yaml` to enable
  editor autocompletion and catch typos before render.
- **Multi-letter builds**: accept a glob or list of YAML files
  (e.g., `letters/*.yaml`) so one repo can produce several letters in a single
  run. The render script already accepts a path argument but CI and pixi tasks
  are hardcoded to `letter.yaml`.
- **Inkscape / SVG support in CI**: the build warns `inkscape: not found`.
  Either install it or convert the SVG logos to PDF at repo level so the `svg`
  package is not needed at build time.

## Medium-term: expand utility

- **Language-aware header logo**: the template hardcodes `EN_HEI.png` in the
  header. A `FR-DE_HEI.png` variant exists but is never selected. Wire the logo
  to `language` so French letters get the French logo automatically.
- **Additional output formats**: besides PDF, produce a print-ready version
  (with bleed/crop marks) and a digital version (with clickable links, no
  signature placeholder).
- **Envelope / address label companion**: reuse `recipient` data to render a
  DL-envelope or label sheet for physical mailings.
- **Reusable sender profiles**: extract `sender` blocks into standalone YAML
  files (e.g., `senders/oesteban.yaml`) and reference them by name, avoiding
  duplication across letters.

## Longer-term: institutional scale

- **Web form front-end**: a simple form (e.g., Streamlit or static HTML+JS) that
  fills the YAML fields and triggers a GitHub Actions workflow via
  `workflow_dispatch`, returning the PDF as an artifact. Lowers the barrier for
  non-technical colleagues.
- **Multi-institution theming**: parameterize colors, logos, and footer text so
  other HES-SO schools or labs can reuse the template with their own branding
  via a `theme.yaml` alongside `letter.yaml`.
- **Archival / versioning**: tag each sent letter with a date-stamped release so
  there is an audit trail of institutional correspondence.
