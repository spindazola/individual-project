# Individual Project

## Marginal and condition-specific reliability of conformal prediction in chest X-ray classification

Supervisor: **Dr Nery Riquelme-Granada**  
University of Southampton — Part III Individual Project

## Start here

1. `PROJECT_CONTEXT.md` — current scope and research direction.
2. `TASKS.md` — current priorities.
3. `DECISIONS.md` — why important methodological choices were made.
4. `LINKS.md` — canonical link index.
5. `literature/SOURCE_MAP.md` — which papers support which ideas.
6. `meetings/` — cleaned meeting notes; `meetings/raw/` preserves source transcripts.
7. `notebooks/` — reproducible explorations and experiments.
8. `src/conformal/` — reusable conformal-prediction code.
9. `experiments/EXPERIMENT_LOG.md` — record of experimental questions/configurations/results.
10. `reports/` — LaTeX writing and project-plan material.
11. `sources/` — local copies of primary papers and coursework guidance.

## Current technical sequence

`00_conformal_reproduction.ipynb` → `01_split_conformal_sanity.ipynb` → `02_chexpert_label_audit.ipynb`

The immediate data task from supervision is to quantify CheXpert's single-positive cases and label/view/patient structure before fixing the final simplified classification target.

## Data policy

The CheXpert images and raw CSVs are intentionally **not** included in Git. See `data/README.md` and point the audit notebook at the local dataset copy.

## Writing workflow

- Code/experiments: VS Code + Jupyter + Git.
- Reports: LaTeX / Overleaf.
- References: Mendeley → `literature/references.bib`.
- Project context: Markdown files in this repository.
