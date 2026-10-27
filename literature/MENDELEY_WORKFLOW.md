# Mendeley / BibTeX Workflow

## Recommended collection structure

- Individual Project / 01 Core CP
- Individual Project / 02 Conditional Coverage
- Individual Project / 03 CheXpert
- Individual Project / 04 Medical ML and Uncertainty
- Individual Project / 05 Hierarchy / Structured Uncertainty
- Individual Project / 99 Maybe Later

## Core papers to add now

1. Angelopoulos & Bates — Gentle Introduction.
2. Romano, Sesia & Candès — Classification with Valid and Adaptive Coverage.
3. Irvin et al. — CheXpert.
4. Vovk — Conditional Validity of Inductive Conformal Predictors.

## Repository workflow

`literature/references.bib` is the canonical BibTeX file used by the LaTeX reports.

When Mendeley metadata is correct:
1. export the relevant collection as BibTeX;
2. replace/update `literature/references.bib`;
3. keep citation keys stable once a key appears in a report;
4. commit the BibTeX change with the corresponding report edits.

## Source discipline

- Read and cite the original paper when it supports a claim.
- Use `literature/SOURCE_MAP.md` to record what each source is being used for.
- Do not cite a webpage when the underlying paper supports the same scientific claim more directly.
- Mark unsupported report statements with `TODO: citation` rather than inventing a reference.
