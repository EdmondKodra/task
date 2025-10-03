# IMDB - Movie Review

Ky projekt perdor Dataset-in IMBD 50K Movie Reviews nga **Kaggle** per te ndertuar nje model te thjesht per Analizen e Sentimentit me 2 kategori(Pozitiv apo Negativ)
↗ [IMDB 50K Movie Reviews Dataset](https://www.kaggle.com/datasets/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews)

# Data Preperation
Per perpunimin e te dhenave e kam perdorur **Jupyter Nootebook** dhe hapat kryesor qe kam ndjekur jan:

📂 Ngarkimi i dataset-it me pandas ku u hoqen duplikatat dhe u pastruan review-t nga HTML tags, simbolet e panevojshme dhe hapesirat e teperta gjithashtu teksti u shnderrua ne lowercase.

🧹 Pastrimi i metejshem i tekstit ku u hoqen stopwords dhe u analizua shperndarja e sentimentit (positive/negative) si dhe fjalet me te shpeshta ne review.

💾 Ruajtja e rezultateve → dataset-i i pastruar u eksportua ne nje file te ri: IMDB_Cleaned_Reviews.csv.

# Funksionalitetet e Kodit

📂 Lexon dataset-in e pastruar IMDB_Cleaned_Reviews.csv.

✂️ Ndan të dhënat në train/test sets.

🔍 Shndërron tekstin në vektorë duke përdorur TF-IDF (unigram + bigram).

🤖 Trajnon dy modele: Logistic Regression dhe Naive Bayes.

📊 Vlerëson performancën me accuracy, classification report dhe confusion matrix.

⚖️ Krahason rezultatet e modeleve me grafik.

# Clonimi

git clone https://github.com/username/IMDB-Sentiment-Analysis.git
cd IMDB-Sentiment-Analysis
pip install pandas scikit-learn matplotlib seaborn notebook
python app.py


✍️ Ka një script interaktiv ku përdoruesi shkruan një fjali dhe modeli jep parashikimin e sentimentit (positive/negative).
