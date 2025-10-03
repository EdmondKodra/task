import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv("IMDB_Cleaned_Reviews.csv")  

texts = df["cleaned_review"]
labels = df["sentiment"]


X_train, X_test, y_train, y_test = train_test_split(texts, labels, test_size=0.2, random_state=42)

vectorizer = TfidfVectorizer(max_features=5000, ngram_range=(1,2))
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)


log_model = LogisticRegression(max_iter=1000)
log_model.fit(X_train_vec, y_train)
log_preds = log_model.predict(X_test_vec)

# Accuracy 0.88 
print(" Logistic Regression Unigram + Bigram ")
print("Accuracy:", accuracy_score(y_test, log_preds))
print(classification_report(y_test, log_preds))


cm_log = confusion_matrix(y_test, log_preds)
plt.figure(figsize=(6,5))
sns.heatmap(cm_log, annot=True, fmt='d', cmap='Blues')
plt.title("Confusion Matrix - Logistic Regression")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.show()


nb_model = MultinomialNB()
nb_model.fit(X_train_vec, y_train)
nb_preds = nb_model.predict(X_test_vec)

# Accuracy 0.85
print("\n Naive Bayes Unigram + Bigram ")
print("Accuracy:", accuracy_score(y_test, nb_preds))
print(classification_report(y_test, nb_preds))


cm_nb = confusion_matrix(y_test, nb_preds)
plt.figure(figsize=(6,5))
sns.heatmap(cm_nb, annot=True, fmt='d', cmap='Greens')
plt.title("Confusion Matrix - Naive Bayes")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.show()


accuracies = {
    "Logistic Regression": accuracy_score(y_test, log_preds),
    "Naive Bayes": accuracy_score(y_test, nb_preds)
}

plt.bar(accuracies.keys(), accuracies.values(), color=['blue','green'])
plt.title("Model Performance Comparison")
plt.ylabel("Accuracy")
plt.show()


def predict_sentence(sentence):
    vec = vectorizer.transform([sentence])
    pred = log_model.predict(vec)[0]
    return pred


while True:
    user_input = input("\nType a sentence (or 'exit' to quit): ")
    if user_input.lower() == "exit":  
        break
    prediction = predict_sentence(user_input)
    print("Predicted Category:", prediction)