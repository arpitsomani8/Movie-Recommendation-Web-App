from flask import Flask, render_template, request
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

data = pd.read_csv('model.csv')

vec = CountVectorizer()
vec_matrix = vec.fit_transform(data['combined']
                               similarity=cosine_similarity(vec_matrix)
