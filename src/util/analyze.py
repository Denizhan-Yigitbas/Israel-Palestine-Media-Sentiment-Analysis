import pandas as pd
import re
from textblob import TextBlob
import matplotlib.pyplot as plt
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
# nltk.download('vader_lexicon')

df = pd.read_csv("./data/combined.csv")

def compute_polarity_textblob(txt):
    cleaned = ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", txt).split())
    analysis = TextBlob(cleaned)
    return analysis.polarity

def compute_sentiment(double):
    if double > 0.3:
        return "positive"
    elif double < -0.3:
        return "negative"
    else:
        return "neutral"

def compute_polarity_vader(txt):
    sid = SentimentIntensityAnalyzer()
    ss = sid.polarity_scores(txt)
    return ss["compound"]

df["polarity"] = df["headline"].apply(lambda x: compute_polarity_vader(x))
df["sentiment"] = df["polarity"].apply(lambda x: compute_sentiment(x))

df.to_csv("./data/results_vader_03.csv", index=False)