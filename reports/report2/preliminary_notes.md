# Report 2 — CheXpert preliminary research notes

## What the original paper establishes

- CheXpert contains **224,316 chest radiographs from 65,240 patients**.
- The dataset is labelled for **14 observations**.
- Labels can be **positive, negative, uncertain, or not mentioned/blank** depending on the stage of the labelling pipeline.
- The labels are extracted from free-text radiology reports by a rule-based labeler with three stages: mention extraction, mention classification, and mention aggregation.
- The original prediction task is to estimate the probability of the 14 observations from chest radiographs; this is therefore naturally a **multi-label** task rather than an ordinary mutually exclusive 14-class problem.
- The validation set contains 200 studies annotated by three board-certified radiologists; the test set contains 500 studies with a consensus reference standard from five radiologists.

## Important implication for our project

Do **not** yet hard-code a 10-class target. Ask Nery tomorrow to approve the exact single-label transformation. Record:

1. Which conditions are included?
2. Are examples with multiple positive findings excluded?
3. Is `No Finding` a class?
4. How are uncertain labels treated?
5. Are blank / not-mentioned labels treated as negative or excluded?
6. Are data splits performed at patient level?

## First data-audit notebook once the rule is agreed

The first CheXpert notebook should report:

- number of patients, studies and images available locally;
- counts of positive / negative / uncertain / blank labels by observation;
- number of positive observations per study;
- frequency of multiple-positive studies;
- class counts after the proposed single-label filter;
- patient overlap checks across any supplied train/validation/test splits;
- examples of paths / metadata only (do not duplicate the image dataset into Git).

## Research angle to preserve

The project is not primarily a CheXpert leaderboard project. The classifier is an experimental instrument. The main downstream quantities are marginal conformal coverage, class/condition-specific empirical coverage, prediction-set size, calibration sensitivity, and stability across repeated splits.
