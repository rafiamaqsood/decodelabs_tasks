import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score


# Load dataset
df = pd.read_csv("titanic.csv")

# Step 1: Handle missing values (important)
df["Age"] = df["Age"].fillna(df["Age"].mean())

# Step 2: Convert categorical data to numeric
df["Sex"] = df["Sex"].map({"male": 0, "female": 1})

# Step 3: Select features (INPUTS)
X = df[["Pclass", "Sex", "Age", "SibSp", "Parch", "Fare"]]

# Step 4: Select target (OUTPUT)
y = df["Survived"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# Predict
predictions = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, predictions)
print("Accuracy:", accuracy)

new_data = pd.DataFrame([
    {"Pclass": 1, "Sex": 1, "Age": 30, "SibSp": 0, "Parch": 0, "Fare": 100},
    {"Pclass": 3, "Sex": 0, "Age": 20, "SibSp": 1, "Parch": 0, "Fare": 8},
    {"Pclass": 2, "Sex": 1, "Age": 45, "SibSp": 0, "Parch": 2, "Fare": 30}
])

predictions = model.predict(new_data)

for i, pred in enumerate(predictions):
    print(f"Passenger {i+1}:", "Survived" if pred == 1 else "Did NOT survive")