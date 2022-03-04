# -*- coding: utf-8 -*-
"""Unit 4 Build Week.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1iO1X6_2oT5Rb7gy8Yxzs09pcC9rl6ycI
"""

import pandas as pd
import numpy as np
from sklearn.neighbors import NearestNeighbors
from sklearn import preprocessing
from sklearn.preprocessing import minmax_scale

"""Kaggle Link: https://www.kaggle.com/rodolfofigueroa/spotify-12m-songs"""

df = pd.read_csv('tracks_features.csv')
df.head()

"""We can recommend songs that are similiar to searched results via some of the song characteristics like danceability, acousticsness, instrumentalness, etc."""

# We can use a KNN (Nearest Neighbors)

def create_knnmodel(X, number_neighbors):
    '''Gets Similar Songs based on Number'''
    model = NearestNeighbors(n_neighbors=(number_neighbors+1, X.shape[0]))
    model.fit(X)
    return model

# Categories I mentioned earlier that we would need to compare values with
X = df[['id', 'acousticness', 'danceability', 'duration_ms', 'energy', 'instrumentalness', 'key', 'liveness', 'loudness', 'mode', 'speechiness', 'tempo', 'time_signature']]
# For easier reading, can set the index for ID
X.set_index('id', inplace=True)
X.head()

# Here I will take one of the entries as an example and organize it into a DF

q={'danceability': 0.470, 
   'energy': 0.978,
   'key': 7,
   'loudness': -5.399,
   'mode': 1,
   'speechiness': 0.0727,
   'acousticness': 0.02610,
   'instrumentalness': 0.000011,
   'liveness': 0.3560,
   'tempo': 117.906,
   'id': '7lmeHLHBe4nmXzuXc0HDjk',
   'type': 'audio_features',
   'duration_ms': 210133,
   'time_signature': 4}

r = pd.DataFrame({'id':[q['id']],
                  'acousticness':[q['acousticness']],
                  'danceability':[q['danceability']],
                  'duration_ms':[q['duration_ms']],
                  'energy':[q['energy']],
                  'instrumentalness':[q['instrumentalness']],
                  'key':[q['key']],
                  'liveness':[q['liveness']],
                  'loudness':[q['loudness']],
                  'mode':[q['mode']],
                  'speechiness':[q['speechiness']],
                  'tempo':[q['tempo']],
                  'time_signature':[q['time_signature']]})
r.set_index('id', inplace=True)
r.head()