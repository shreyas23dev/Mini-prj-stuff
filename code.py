
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report


data = pd.read_csv("nvd_labeled.csv")
text_column = "cve_text"

# CVSS metric columns we want to predict
metric_columns = ["AV", "AC", "PR", "UI", "S", "C", "I", "A"]

# Spliting data into training and testing parts
X_train, X_test, y_train, y_test = train_test_split(
    data[text_column],
    data[metric_columns],
    test_size=0.2,
    random_state=42,
    stratify=data["AV"].dropna()  # make sure split keeps label balance
)

# empty dictionary to store models
models = {}

# training model for each CVSS metric
for metric in metric_columns:
    print(f"Training model for {metric}...")

    # Create a simple text classifier
    vectorizer = TfidfVectorizer(ngram_range=(1, 2), min_df=3, max_df=0.9)
    classifier = LogisticRegression(max_iter=300, class_weight="balanced")

    # Make a pipeline (text → TF-IDF → logistic regression)
    model = Pipeline([
        ("tfidf", vectorizer),
        ("clf", classifier)
    ])

    # Train the model on that one metric
    model.fit(X_train, y_train[metric])

    # Save the trained model
    models[metric] = model

# predictions for each metric
predictions = {}

for metric in metric_columns:
    print(f"Predicting for {metric}...")
    y_pred = models[metric].predict(X_test)
    predictions[metric] = y_pred

    # Step 8: Show how well the model performed
    print(f"\n----Results for {metric}----")
    print(classification_report(y_test[metric], y_pred, zero_division=0))
