
from nltk.corpus import stopwords
from nltk.sentiment import SentimentIntensityAnalyzer

english_stopwords = stopwords.words('english')
print(english_stopwords[:5])

analyse = SentimentIntensityAnalyzer()
print(analyse.polarity_scores("I am furious, i'm abslutely annoyed and disappointed"))
print(analyse.polarity_scores("Look at those beautiful mountains, they are idyllic and beautiful!"))

