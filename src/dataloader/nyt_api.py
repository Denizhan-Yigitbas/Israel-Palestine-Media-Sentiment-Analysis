from pynytimes import NYTAPI
from datetime import datetime
import re
from textblob import TextBlob
import numpy
import pandas as pd

nyt = NYTAPI("WxQXsVSaIIlTgEfG0VnrlP7JhOVYYL0j")

search="US Embassy move to Jerusalem"
start_date = datetime(2015, 1, 1)
end_date = datetime(2019, 12, 31)

articles = nyt.article_search(
    query = search,
    results = 50,
    dates = {
        "begin": start_date,
        "end": end_date
    },
    options = {
        "sort": "relevance",
        "sources": [
            "New York Times",
        ],

    }
)

def clean(text):
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t]) | (\w+:\/\/\S+)", " ", text).split())

headlines = []
pub_dates = []
for article in articles:
    headlines.append(article['headline']['main'])
    date = datetime.strptime(article['pub_date'], '%Y-%m-%dT%H:%M:%S%z')
    pub_dates.append(date.strftime("%b %Y"))

df = pd.DataFrame()
df['headline'] = headlines
df['pub_date'] = pub_dates
df['source'] = "The New York Times"
df['query'] = search
 
print("")
for i in df['headline']:
    print(i)

df.to_csv('data/emb_nyp.csv', index=False)