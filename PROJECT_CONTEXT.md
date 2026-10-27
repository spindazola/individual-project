# PROJECT_CONTEXT — Updated after 20 October 2026 supervision

## Title
**Marginal and condition-specific reliability of conformal prediction in chest X-ray classification**

## Dataset
CheXpert.

## Current experimental direction
The project will use a reusable conformal-prediction pipeline and study how practical calibration choices affect reliability and efficiency.

### Calibration factors currently identified
1. **Calibration unit**: image-level vs patient-level.
2. **Calibration image composition**: mixed frontal+lateral vs frontal-only.
3. **Calibration sample design**: repeated random splits, calibration-set size, repeated seeds.

## Core metrics
- marginal coverage;
- condition-specific empirical coverage;
- subgroup / approximate conditional coverage;
- prediction-set size and mean set size;
- distribution of prediction-set sizes.

## Methodological position
Patient-level calibration is likely more clinically meaningful because decisions concern patients, but image-level calibration remains a useful comparison. The project should quantify the cost or benefit of this choice.

## Immediate technical task
- inspect CheXpert's label structure;
- count examples with exactly one positive label;
- compute condition frequencies;
- inspect frontal/lateral composition;
- inspect patient repetition;
- document results for Report 2.

## Writing
### Report 1
Definitions, marginal coverage, split conformal, conditional coverage, impossibility of exact distribution-free conditional coverage, empirical/relaxed approximations.

### Report 2
CheXpert structure, label generation, uncertainty labels, multi-label structure, view types, patient structure, exploratory label statistics, and implications for conformal calibration.

## Stretch work
Multi-label conformal prediction, label hierarchy, structured uncertainty, knowledge-graph ideas, epistemic/aleatoric decomposition. These are not immediate priorities.
