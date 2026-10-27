# Supervisor Meeting 2 — 20 October 2026

## Main decisions

### 1. Immediate data-analysis task
CheXpert is multi-label, but many images/studies contain only one positive observation.

The next concrete task is to quantify:
- how many examples contain exactly one positive label;
- the frequency of each condition among those single-positive examples;
- the overall positive frequency of each condition.

This analysis should feed directly into Report 2.

### 2. Calibration unit: patient vs image
Both should be tested.

Methodologically, patient-level calibration is the more natural clinical choice because the ultimate decision concerns a patient, but image-level calibration is a useful comparison.

The experiment should quantify the practical cost/benefit of this methodological choice in terms of:
- coverage;
- efficiency (prediction-set size).

### 3. Calibration image composition
CheXpert includes frontal and lateral images.

A planned experiment should compare calibration sets such as:
- mixed frontal + lateral;
- frontal-only.

The aim is to test whether calibration data composition accurately represents deployment conditions and how mismatch affects coverage and efficiency.

### 4. Evaluation
The core predictor-evaluation metrics are:
- marginal coverage;
- efficiency, measured by prediction-set size;
- empirical approximations to conditional coverage.

True pointwise conditional coverage should not be claimed.

### 5. Project framing
The project is becoming a controlled investigation of how calibration decisions affect the reliability and efficiency of a conformal predictor.

A useful experimental framing is:

> Fix a classifier and conformal pipeline, then vary calibration design choices and measure their effect on marginal coverage, condition-specific / subgroup coverage, and prediction-set efficiency.

### 6. Reporting
- Continue Report 1 on conformal prediction.
- Report 2 is about CheXpert and should include the dataset analysis now being performed.
- The immediate short-term technical task is data inspection/statistics, not sophisticated model development.

## Immediate actions

1. Load the CheXpert training CSV.
2. Audit label values and missingness.
3. Count examples with exactly one positive pathology.
4. Count single-positive examples by pathology.
5. Count total positives / uncertain / negative / blank by observation.
6. Break counts down by frontal vs lateral view.
7. Break counts down by patient where useful.
8. Put tables/figures into Report 2 notes.
9. Continue Report 1.
10. Design later calibration experiments:
   - image-level vs patient-level;
   - mixed-view vs frontal-only calibration.

## Questions still open

- Which conditions will form the final simplified single-label task?
- Should `No Finding` and `Support Devices` be excluded from the pathology target?
- How should uncertain labels (`-1`) be handled for the initial single-label experiment?
- What exact classifier(s) will be used for the first CheXpert baseline?

These should be resolved after the dataset statistics are available.
