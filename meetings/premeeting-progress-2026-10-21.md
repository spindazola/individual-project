# Work completed before supervision — 21 October 2026

## Concrete progress to show Nery

- Drafted Report 1 covering the CP problem setup, marginal coverage, split conformal prediction, the corrected calibration quantile, conditional coverage, the general impossibility result, class-conditional coverage, and APS.
- Added references for Angelopoulos & Bates, Romano et al., Vovk (conditional validity), and CheXpert.
- Built and executed a 10-class split-conformal sanity-check notebook using scikit-learn digits as a controlled proxy dataset.
- The notebook compares the simple probability/LAC score with APS and reports marginal coverage, class-wise coverage, and mean prediction-set size.
- Prepared CheXpert data-audit questions, but deliberately did **not** choose the single-label transformation without supervisor agreement.

## Decisions still required tomorrow

1. Exact single-label CheXpert construction.
2. Treatment of uncertain and blank labels.
3. Whether `No Finding` is included as a target class.
4. Whether class-conditional conformal should be a core method or later comparison.
5. Exact deliverable for next Tuesday.
