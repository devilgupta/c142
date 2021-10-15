import pandas as pd
import numpy as np

df=pd.read_csv("final.csv")
df=df[df["soup"].notna()]
from sklearn.feature_extraction.text import CountVectorizer
count=CountVectorizer(stop_words="english")
count_matrix=count.fit_transform(df["soup"])
from sklearn.metrics.pairwise import cosine_similarity
cosine_sin2=cosine_similarity(count_matrix,count_matrix)
df=df.reset_index()
indices=pd.Series(df.index,index=df["original_title"])
def get_recommendations(title,cosine_sin):
  idx=indices[title]
  sin_scores=list(enumerate(cosine_sin[idx]))
  sin_scores=sorted(sin_scores,key=lambda x:x[1],reverse=True)
  sin_scores=sin_scores[1:11]
  movie_indices=[i[0]for i in sin_scores]
  return df["original_title","poster_link","release_date","runtime","vote_average"].iloc[movie_indices].values.tolist()