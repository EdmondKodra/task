# IMDB - Movie Review

Ky projekt perdor Dataset-in IMBD 50K Movie Reviews nga **Kaggle** per te ndertuar nje model te thjesht per Analizen e Sentimentit me 2 kategori(Pozitiv apo Negativ)
↗ [IMDB 50K Movie Reviews Dataset](https://www.kaggle.com/datasets/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews)

## Data Preperation
Per perpunimin e 50K+ te dhenave e kam perdorur **Jupyter Notebook** dhe hapat kryesor qe kam ndjekur jan:

📂 Ngarkimi i dataset-it me pandas ku i hoqa duplicates dhe i pastrova review-t nga HTML tags, simbolet e panevojshme dhe hapesirat e teperta gjithashtu tekstin e shnderrova ne lowercase.

🧹 Pastrimi i metejshem i tekstit ku i hoqa stopwords dhe u analizua shperndarja e sentimentit (positive/negative) si dhe fjalet me te shpeshta ne review.

💾 Ruajtja e rezultateve dataseti i pastruar u eksportua ne nje file te ri: IMDB_Cleaned_Reviews.csv.

## Funksionalitetet e Kodit

📂 Lexon dataset-in e pastruar IMDB_Cleaned_Reviews.csv.

✂️ Ndan te dhenat ne train/test sets.

🔍 Shnderron tekstin ne vektore duke perdorur TF-IDF (unigram + bigram).

🤖 Trajnon dy modele: Logistic Regression dhe Naive Bayes.

📊 Vlereson performancen me accuracy, classification report dhe confusion matrix.

✍️ Ka nje script interaktiv ku perdoruesi shkruan nje fjali dhe modeli jep parashikimin e sentimentit (positive/negative).

⚖️ Krahaso rezultatat e modeleve me grafik.

🎬 [Kjo video tregon projektin](https://youtu.be/UqWWqwmDr9o) #Skip 1:07

## Clone

Clono Projektin

cd task

pip install pandas scikit-learn matplotlib seaborn notebook

python app.py



