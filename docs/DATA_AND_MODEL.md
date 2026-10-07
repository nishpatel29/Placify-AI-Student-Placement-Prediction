# Data & Model Documentation

## Inputs

| Feature | Meaning |
|---|---|
| CGPA | Academic performance indicator |
| Technical Skills Score | Demonstration score representing technical readiness |
| Internship | Whether internship experience is present |
| Aptitude Score | Demonstration aptitude assessment score |

## Output

The model estimates:

- Placed
- Not Placed

The application also presents probability/confidence information and model analytics.

## Model

The project uses Decision Tree Classification:

```python
DecisionTreeClassifier(
    criterion="gini",
    max_depth=5,
    min_samples_leaf=6,
    random_state=42,
)
```

The training script uses a stratified 80/20 train-test split with `random_state=42`.

## Dataset status

The included dataset is synthetic/demo data. It is not official institutional placement data. See `data/DATASET.md` for provenance and replacement requirements.

## Authentication data

User accounts and prediction history are stored separately from the ML dataset. Passwords are stored as salted PBKDF2-SHA256 hashes rather than plaintext.

## Responsible ML

For a real-world version, use authorized and representative data, document data provenance, evaluate class imbalance, use cross-validation, tune hyperparameters, assess fairness, evaluate calibration, protect personal information, and validate performance on an appropriate holdout population.

Do not treat synthetic/demo data or model confidence as real-world placement probability.
