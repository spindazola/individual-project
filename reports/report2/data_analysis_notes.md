# Report 2 — CheXpert Analysis Notes

## Dataset facts from the CheXpert paper
- 224,316 chest radiographs;
- 65,240 patients;
- 14 labelled observations;
- positive, negative and uncertain labels;
- labels extracted from radiology reports using an automated labeler.

## Analysis required from our copy
1. Total row count.
2. Unique patient count.
3. Frontal/lateral counts.
4. Positive/uncertain/negative/blank count per observation.
5. Number and percentage of examples with exactly one positive observation.
6. Same statistic after excluding `No Finding` and `Support Devices`.
7. Frequency of each pathology within the single-positive subset.
8. Single-positive frequency by view.

## Why this matters
The project proposes a simplified single-label first experiment while CheXpert is naturally multi-label. The single-positive analysis determines whether a sufficiently large and balanced subset exists. Patient and view analyses also directly motivate later calibration comparisons.

## Interpretation to add after running the notebook
- Which conditions are feasible?
- Which are too rare?
- How imbalanced is the subset?
- How common are uncertain labels?
- How much repeated imaging is present per patient?
- How different are frontal and lateral distributions?
