# IMDB - Movie Review

Ky projekt perdor Dataset-in IMBD 50K Movie Reviews nga **Kaggle** per te ndertuar nje model te thjesht per Analizen e Sentimentit me 2 kategori(Pozitiv apo Negativ)
↗ [IMDB 50K Movie Reviews Dataset](https://www.kaggle.com/datasets/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews)

## Data Preperation
Per perpunimin e te dhenave e kam perdorur **Jupyter Nootebook** dhe hapat kryesor qe kam ndjekur jan:

📂 Ngarkimi i dataset-it me pandas ku u hoqen duplikatat dhe u pastruan review-t nga HTML tags, simbolet e panevojshme dhe hapesirat e teperta; gjithashtu teksti u shnderrua ne lowercase.

🧹 Pastrimi i metejshem i tekstit ku u hoqen stopwords dhe u analizua shperndarja e sentimentit (positive/negative) si dhe fjalet me te shpeshta ne review.

💾 Ruajtja e rezultateve → dataset-i i pastruar u eksportua ne nje file te ri: IMDB_Cleaned_Reviews.csv.

## Funksionalitetet e Kodit

📂 Leximi i dataset-it të pastruar (IMDB_Cleaned_Reviews.csv) me pandas.

✂️ Ndarja e të dhënave në train/test sets me train_test_split.

🔍 Vektorizimi i tekstit duke përdorur TF-IDF (unigram + bigram).

🤖 Trajnimi i modeleve:

Logistic Regression

Naive Bayes

📊 Vlerësimi i performancës me:

Accuracy

Precision, Recall, F1-score (classification report)

Confusion Matrix (vizualizuar me seaborn heatmap)

⚖️ Krahasimi i performancës së modeleve me grafik bar chart.

✍️ Prediction Script: Funksion ku përdoruesi mund të japë një fjali, dhe modeli parashikon sentimentin positive/negative në kohë reale.
