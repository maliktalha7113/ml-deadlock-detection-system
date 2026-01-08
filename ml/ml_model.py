import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Load dataset
df = pd.read_csv("../data/deadlock_dataset.csv")

X = df.drop("deadlock", axis=1)
y = df["deadlock"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = LogisticRegression()
model.fit(X_train, y_train)

# Evaluate
predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)

print(f"🎯 Model Accuracy: {accuracy:.2f}")

def predict_deadlock(system_state):
    probability = model.predict_proba([system_state])[0][1]
    return probability
