# IMDB - Movie Review

Ky projekt perdor Dataset-in IMBD 50K Movie Reviews nga **Kaggle** per te ndertuar nje model te thjesht per Analizen e Sentimentit me 2 kategori(Pozitiv apo Negativ)
↗ [IMDB 50K Movie Reviews Dataset](https://www.kaggle.com/datasets/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews)

## Data Preperation
Per perpunimin e te dhenave e kam perdorur **Jupyter Nootebook** dhe hapat kryesor qe kam ndjekur jan:

📂 Ngarkimi i dataset-it me pandas ku u hoqen duplikatat dhe u pastruan review-t nga HTML tags, simbolet e panevojshme dhe hapesirat e teperta; gjithashtu teksti u shnderrua ne lowercase.

🧹 Pastrimi i metejshem i tekstit ku u hoqen stopwords dhe u analizua shperndarja e sentimentit (positive/negative) si dhe fjalet me te shpeshta ne review.

💾 Ruajtja e rezultateve → dataset-i i pastruar u eksportua ne nje file te ri: IMDB_Cleaned_Reviews.csv.

## Model Training

📊 Dataset-i u nda ne train/test split per te siguruar validim te drejte.

🤖 U trajnuan dy modele te thjeshta klasifikimi: Logistic Regression dhe Naive Bayes.

📈 Modelet u vleresuan duke perdorur accuracy, precision, recall dhe F1-score, dhe performanca u krahasua me grafik bar chart dhe confusion matrix.

## Prediction Script

✍️ U krijua nje funksion i thjeshte ku perdoruesi mund te shkruaje nje fjali dhe modeli parashikon sentimentin (positive/negative).

## Bonus

🔍 U perdor TF-IDF me unigram + bigram ne vend te bag-of-words.

⚖️ U krahasuan dy modele dhe u vizualizuan rezultatet per te pare cili performon me mire.

📊 U krijuan confusion matrices per te shfaqur performancen e modeleve.
