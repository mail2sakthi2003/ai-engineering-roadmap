from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# Iris is a classic tiny built-in dataset: 150 flower measurements,
# 3 species to predict from 4 features (petal/sepal length & width).
# It's the "hello world" of ML — small, clean, no downloads needed.
X, y = load_iris(return_X_y=True)

print(f"Total samples: {len(X)}")
print(f"Features per sample: {X.shape[1]}")
print(f"Classes to predict: {set(y)}")

# 80% train, 20% test — a common default split.
# random_state=42 makes the split reproducible — same split every run,
# useful when you want to compare changes fairly instead of getting
# a different random split each time.
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.5, random_state=42
)
print(f"\nTraining on {len(X_train)} samples, testing on {len(X_test)} samples")

# RandomForestClassifier: an ensemble of decision trees that vote on the answer.
# Good default choice for a first classifier — reasonably accurate,
# doesn't need feature scaling, easy to reason about.
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Predict on the test set — data the model never saw during training
predictions = model.predict(X_test)

accuracy = accuracy_score(y_test, predictions)
print(f"\nAccuracy on unseen test data: {accuracy:.2%}")

print("\nDetailed report:")
print(classification_report(y_test, predictions))