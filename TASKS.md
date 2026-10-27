# TASKS — After 20 October 2026 supervision

## Highest priority
- [ ] Locate the CheXpert training CSV.
- [ ] Run `02_chexpert_label_audit.ipynb`.
- [ ] Verify label semantics in our copy.
- [ ] Compute exactly-one-positive count and percentage.
- [ ] Compute single-positive frequency by condition.
- [ ] Compute positive / uncertain / negative / blank counts by observation.
- [ ] Compare frontal vs lateral label frequencies.
- [ ] Count unique patients and repeated-image structure.
- [ ] Save tables/figures for Report 2.

## Report 1
- [ ] Finish first full draft.
- [ ] Check every substantive claim has a citation.
- [ ] Make marginal vs conditional coverage precise.
- [ ] Explain coverage vs efficiency.

## Report 2
- [ ] Dataset overview.
- [ ] 14 observations and label semantics.
- [ ] Automated report labeler.
- [ ] Frontal/lateral views.
- [ ] Patient/study/image structure.
- [ ] Single-positive statistics from our copy.
- [ ] Explain why these statistics matter for the simplified classification task.

## Later experiments
- [ ] Baseline classifier.
- [ ] Split conformal baseline.
- [ ] APS.
- [ ] Image-level calibration.
- [ ] Patient-level calibration.
- [ ] Mixed-view calibration.
- [ ] Frontal-only calibration.
- [ ] Coverage comparison.
- [ ] Efficiency comparison.
- [ ] Repeated calibration splits / sizes.
