# -*- coding: utf-8 -*-
"""
# **MOVIE RECOMMENDATION SYSTEM**
"""

import numpy as np
import pandas as pd

data = pd.read_csv('/content/movie_metadata.csv')

data.columns

data = data.drop(['color', 'num_critic_for_reviews', 'duration',
                  'director_facebook_likes', 'actor_3_facebook_likes',
                  'actor_1_facebook_likes', 'gross',
                  'num_voted_users', 'cast_total_facebook_likes',
                  'facenumber_in_poster', 'plot_keywords',
                  'movie_imdb_link', 'num_user_for_reviews', 'language', 'country',
                  'content_rating', 'budget', 'title_year', 'actor_2_facebook_likes',
                  'imdb_score', 'aspect_ratio', 'movie_facebook_likes'], axis=1)

data.dropna(inplace=True)

data.columns

data.head()

data["movie_title"] = data["movie_title"].str.lower()

data.head()

data['genres']

data['genres'] = data['genres'].apply(lambda x: str(x).replace('|', ' '))

data['movie_title']

data['movie_title'] = data['movie_title'].apply(lambda x: x[:-1])

data['combined'] = data['director_name']+' '+data['actor_2_name'] + \
    ' '+data['genres']+' '+data['actor_1_name']+' '+data['actor_3_name']

data.to_csv('model.csv')
