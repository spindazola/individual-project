# Repository Instructions

## Research
- Do not invent numerical results.
- Distinguish synthetic experiments from CheXpert experiments.
- Preserve calibration/test separation.
- Avoid patient leakage across data splits.
- Record random seeds and experimental configuration.
- Do not claim clinical validity.
- Do not claim exact instance-wise conditional coverage.
- Cite technical/literature claims or mark them as needing a citation.

## Python
- Put reusable code in `src/conformal/`.
- Use notebooks for exploration and figures.
- Avoid duplicating statistical logic across notebooks.
- Do not hard-code absolute local paths.
- Add tests for reusable functions.
- Never commit CheXpert images or raw/protected data.

## Writing
- Reports are written in LaTeX.
- Bibliography lives in `literature/references.bib`.
- Define notation before using it.
- Separate formal guarantees from empirical observations.
