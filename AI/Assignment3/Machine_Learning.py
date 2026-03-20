# ---------------------------------------------------------
# Machine Learning - Assignment (1)
# Deema Mohammed AL-Maqadma
# ---------------------------------------------------------
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
import pandas as pd

# 1. Load dataset
iris = load_iris()
X = iris.data
y = iris.target

print("Shape of X:", X.shape)
print("Number of classes:", len(set(y)))
print("Class distribution:\n", pd.Series(y).value_counts())

# 2. Split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. Models
models = {
    "KNN": KNeighborsClassifier(),
    "SVM": SVC(),
    "Logistic Regression": LogisticRegression(max_iter=200),
    "Decision Tree": DecisionTreeClassifier()
}

results = []

for name, model in models.items():
    print("\n==============================")
    print(f"Model: {name}")
    print("==============================")

    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    acc = accuracy_score(y_test, y_pred)
    print("Accuracy:", acc)

    print("\nClassification Report:")
    print(classification_report(y_test, y_pred))

    print("Confusion Matrix:")
    print(confusion_matrix(y_test, y_pred))

    report = classification_report(y_test, y_pred, output_dict=True)

    results.append({
        "Model": name,
        "Precision": report["macro avg"]["precision"],
        "Recall": report["macro avg"]["recall"],
        "F1-score": report["macro avg"]["f1-score"],
        "Accuracy": acc
    })

# 4. Comparison Table
df_results = pd.DataFrame(results)
print("\n\n=== Comparison Table ===")
print(df_results)


# ============================
# Analysis Paragraph
# ============================
# All four models achieved perfect performance on the Iris dataset, with 100% accuracy, precision, recall, and F1-score. This result is expected because the Iris dataset is small, clean, and the three classes—especially Setosa—are very well separated in the feature space. The confusion matrices show that none of the models misclassified any samples, meaning all classes were predicted correctly. Although all models performed equally well in this experiment, this does not mean they always behave the same on more complex datasets. In general, SVM and Logistic Regression tend to create smooth decision boundaries, KNN relies on local neighbors, and Decision Trees split the data into simple rules. But for this dataset, all of them were able to perfectly separate the classes.
# Thx ^_^ 