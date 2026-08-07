# Day 5 Notes — Understanding Train/Test Split (In Simple Terms)

## The Analogy: Studying for an Exam

Imagine you're teaching a student to identify 3 types of flowers just by looking at
measurements (how long/wide the petals and leaves are) — no pictures, just numbers.

- You give the student **120 practice examples**, each with the measurements *and*
  the correct answer written next to it ("this one is Species A", "this one is
  Species B"...). The student studies these and learns the pattern — e.g., "flowers
  with long, narrow petals tend to be Species A."
- Then, to check if they *actually* learned the pattern (instead of just
  memorizing the 120 examples), you give them **30 brand-new examples they've
  never seen before** — measurements only, no answers. You ask them to guess
  the species.
- You reveal the real answers and count how many they got right. That score is
  the real test of whether they learned something useful, not just memorized.

That's the entire idea behind `test_ml.py`. Everything in the code is just doing
that, in code form.

---

## Mapping the Analogy to the Code

### 1. Load the data (the "spreadsheet" of flowers)
```python
X, y = load_iris(return_X_y=True)
```
- `X` = the measurements (petal length, petal width, etc.) — the "clues"
- `y` = the correct species for each flower — the "answer key"

Think of it as one big spreadsheet: columns of measurements, plus one column
that says the right answer.

### 2. Split into practice questions and a real exam
```python
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
```
- **80% (120 flowers) → the "practice questions"** — `X_train` (measurements)
  and `y_train` (answer key) — what the student studies from
- **20% (30 flowers) → the "real exam"** — `X_test` (measurements only) and
  `y_test` (the answer key, kept hidden until grading time)

### 3. Studying
```python
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)
```
`model` is the student. `.fit(X_train, y_train)` means: "here are 120 practice
questions *with* the answers — go learn the pattern." After this line runs,
the model has learned something like "if petals are this shape, it's usually
this species."

### 4. Taking the exam
```python
predictions = model.predict(X_test)
```
We hand the model the 30 test measurements — **without the answers** — and ask
it to guess. `predictions` is just its list of 30 guesses.

### 5. Grading
```python
accuracy = accuracy_score(y_test, predictions)
```
Now we compare the model's guesses (`predictions`) against the real answers we
kept hidden (`y_test`), and calculate what percentage it got right.

---

## The One-Sentence Summary

We showed the model 120 flowers with answers so it could learn the pattern,
then quizzed it on 30 different flowers it had never seen, and measured how
many it got right — that's the only honest way to know if it actually learned
something, instead of just memorized the practice set.

---

## Why This Matters Later (Track B)

This same train/test idea is the foundation for every ML project in Track B —
especially the **Incident Severity Classifier**, where "did the model actually
learn the pattern or just memorize past tickets" is exactly the question we'll
need to answer before trusting it on new incidents.
