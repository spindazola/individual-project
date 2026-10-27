what should I do now

Worked for 29s

Given where you are **right now, Tuesday 20 October at about 12:46**, and your supervision is normally **Tuesday at 1 pm**, I would **not start anything big**. Your job for the next 10–15 minutes is to get the decisions you need from Nery.

Go into the meeting with this exact agenda:

1. **What I’ve done**
   - Read the core conformal prediction papers.
   - Built/understood the basic split-conformal pipeline: score → calibration quantile → prediction set. That is exactly the basic workflow Angelopoulos & Bates present. 
   - Looked at APS/adaptive classification and per-class/conditional coverage. Romano et al. specifically motivate methods that retain marginal guarantees while trying to behave better conditionally. 
   - Started the synthetic implementation/sanity checks.
2. **Get one crucial decision from him: how exactly are you turning CheXpert into the single-label problem he wants?**

   This is the thing I would **not guess yourself**. CheXpert is inherently multi-label: it has **14 observations** with positive, negative and uncertain labels.  You need Nery to agree on the transformation before you spend hours building the dataset.

   Ask something like:
   > “For the single-label setup, what exact target do you want me to construct from CheXpert? Should each image be assigned one mutually exclusive pathology class, should we restrict to images with exactly one positive pathology, or do you have another construction in mind?”
3. **Get the research question pinned down.**

   I think your cleanest version is now roughly:

   **How reliable are conformal prediction sets for chest X-ray classification when overall marginal coverage hides differences between classes or difficulty levels?**

   That directly follows the distinction you’ve been reading about: marginal coverage is guaranteed, whereas strong conditional coverage generally is not. 

   Then your experiments become very obvious:\
   **base classifier → split conformal → APS → overall coverage → per-class coverage → set size → calibration-set-size/reproducibility experiments.**
4. **Confirm the scope for the project plan due 26 October.**

   Ask whether he is happy with something like:
   > Baseline classifier → conformal calibration → APS → reliability diagnostics across classes → calibration-size/conformity-score experiments → CheXpert case study.
   You do **not** need to invent another clever research direction this week.
5. **Ask about the data logistics.**

   You were waiting on the large CheXpert dataset / drive arrangement. Find out whether you should download/process anything yourself or whether he is still supplying it.

After the meeting, I would make **today a writing/planning day rather than a CheXpert coding day**. Your priority order should be: **write up the decisions from Nery → finish the \~2-page Report 1 on conformal prediction → draft the CheXpert dataset/label section for Report 2 → build the project plan/Gantt for the 26th → only then continue implementation.**

For Report 2, you already have a useful central point: CheXpert deliberately preserves radiologist uncertainty, with labels classified as positive, negative or uncertain; the paper describes uncertainty as arising both from diagnostic uncertainty and ambiguity in reports.  That gives you a very natural bridge from **medical uncertainty → unreliable probability outputs → conformal prediction**.

So, **right now: open a blank note and write those four questions for Nery. Don't code.** The one thing that can save you the most wasted work today is leaving the meeting knowing **exactly what “single-label CheXpert” means and exactly what your primary experiment is**. 

do it for me

Here’s the exact note I’d take into the supervision meeting.

## Nery supervision — 20 October

### 1. Where I am now

I’ve worked through the main conformal prediction papers and I think I now understand the basic pipeline:

**trained classifier → conformity score → calibration set → quantile threshold → prediction set**

The key attraction is that conformal prediction can wrap around a black-box model and give finite-sample marginal coverage guarantees without requiring the model probabilities themselves to be perfectly calibrated. 

I’ve also looked at adaptive prediction sets. The motivation is that ordinary marginal coverage can hide poor behaviour on harder examples or particular groups/classes, whereas adaptive methods try to make the prediction sets better reflect the difficulty of each input. 

Romano, Sesia and Candès make essentially the same distinction: marginal coverage is achievable, while exact conditional coverage is generally not, so the goal is to retain marginal guarantees while getting as close as possible to useful conditional behaviour. 

---

### 2. Main question: what exactly should my CheXpert classification problem be?

This is the main thing I want to resolve before doing more implementation.

CheXpert is naturally a **multi-label** dataset. Each study can have labels for 14 different observations, and those labels can be positive, negative or uncertain. 

So for the single-label classification setup we discussed, what exactly would you like me to do?

Possible interpretations I can see are:

- restrict the dataset to examples containing exactly one positive pathology and use that pathology as the class;
- choose a subset of mutually exclusive pathologies and construct a single target;
- convert it into one-vs-rest classification for a particular pathology;
- or use some other transformation you already have in mind.

**Question for Nery:**

> What precise single-label formulation do you want me to use for CheXpert?

I’d like to fix this before building the dataset pipeline.

---

### 3. Proposed research question

At the moment I think the project could be framed as:

> **How reliable are conformal prediction sets for medical image classification when overall marginal coverage may conceal differences in reliability across classes and different levels of prediction difficulty?**

Or, slightly more technically:

> **To what extent can adaptive conformal prediction improve class-wise and difficulty-dependent reliability while preserving marginal coverage guarantees in chest X-ray classification?**

Does that sound like the right direction, or should the project question be narrower?

---

### 4. Proposed experiment structure

My current idea is:

**Step 1 — Baseline classifier**\
Train or use a classifier that outputs class probabilities.

**Step 2 — Standard split conformal**\
Apply a simple conformal method first to establish the baseline.

**Step 3 — Adaptive Prediction Sets / APS**\
Apply the cumulative-probability conformity score so that prediction-set size can vary according to model uncertainty.

The APS idea is to include classes from most likely to least likely until their cumulative probability reaches the conformally calibrated threshold. 

**Step 4 — Evaluate overall coverage**

- marginal coverage;
- average prediction-set size.

**Step 5 — Evaluate reliability beyond marginal coverage**

- coverage by true class;
- coverage by prediction-set size;
- possibly coverage by model confidence / difficulty.

This seems important because a method can achieve 90% overall coverage while performing much worse on a minority subgroup or difficult subset. 

**Step 6 — Investigate calibration-data size**\
Repeat calibration with different calibration-set sizes and random splits to see how stable the realised coverage is.

The conformal paper points out that the guarantee holds even with small calibration sets, but realised coverage becomes more stable as the calibration set grows. 

**Question for Nery:**

> Is this enough experimental scope for the project, or do you want another conformal method or another research dimension included?

---

### 5. Metrics I propose using

For each method:

- marginal coverage;
- average prediction-set size;
- prediction-set-size distribution;
- class-conditional coverage;
- worst-performing class;
- size-stratified coverage;
- possibly feature/difficulty-stratified coverage.

The literature explicitly recommends looking beyond mean set size. A useful conformal method should ideally give small sets for easy points and larger sets for difficult points. 

---

### 6. CheXpert uncertainty labels

I also wanted to ask how we should treat CheXpert’s original **uncertain labels**.

The original CheXpert paper deliberately preserves uncertainty in radiology reports rather than simply forcing every observation into positive or negative. 

They tested several strategies including:

- ignoring uncertain labels;
- mapping them to 0;
- mapping them to 1;
- self-training;
- treating uncertainty as a separate class. 

And importantly, the best uncertainty treatment varied by pathology. 

**Question for Nery:**

> Should I treat the uncertain labels as part of the research problem, or should I simplify them away so the focus stays on conformal prediction?

My instinct is to simplify them initially unless you think uncertainty labels are central to the project.

---

### 7. Project scope for the report / Gantt

For the project plan due soon, I was thinking of structuring it roughly as:

**October**

- literature review;
- understand conformal prediction;
- define CheXpert task;
- baseline synthetic experiments.

**Late October–November**

- preprocess CheXpert;
- implement baseline classifier;
- implement split conformal and APS;
- validate coverage.

**November–December**

- class-conditional and difficulty-based reliability analysis;
- calibration-set-size experiments;
- compare methods.

**January**

- refine experiments;
- additional baselines if needed;
- visualisation and interpretation.

**February onward**

- final experiments;
- write-up;
- dissertation/report preparation.

**Question for Nery:**

> Is that the right level of ambition and sequencing for the project?

---

### 8. Dataset access

I also need to clarify the practical side:

> What is the current plan for accessing/storing CheXpert? Should I download and preprocess it myself now, or are we still arranging access through the university / shared drive?

I don’t want to build a pipeline around the wrong version of the dataset.

---

## The four things I need to leave the meeting knowing

1. **Exactly what the single-label CheXpert target is.**
2. **Whether the proposed research question is narrow enough.**
3. **Which conformal methods and evaluation metrics are required.**
4. **What I should have completed before the next supervision.**

And at the very end I’d ask:

> “If I come back next week with the CheXpert task constructed, a baseline classifier working, and split conformal plus APS implemented, would that be the right amount of progress?”

That forces a concrete deliverable rather than leaving the meeting with another vague reading task.
