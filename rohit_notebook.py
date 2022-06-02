# %%
import json
import pandas as pd
from collections import Counter
import seaborn as sns
import wordcloud

# %%
tweets = pd.read_csv("./data/baby_formula_geo_statewise.csv")
tweets
# %%
# hashes = tweets.loc[tweets.apply(lambda x: '#' in x['text'], axis=1)]
person = tweets.iloc[8735]
print(person)
# print(person['text'])
# print(person['entities'])
person['geo']

# %%
c = Counter()
for hashtag in person['entities'].get('hashtags'):
    c.update([hashtag['tag']])
# %%

# %%
