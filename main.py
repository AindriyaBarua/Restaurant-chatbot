import nltk
import os
from nltk.stem.lancaster import LancasterStemmer
import numpy as np
import tflearn
import tensorflow as tf
import random
import json
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
import fasttext as ft

# from gensim.models import KeyedVectors
# from gensim import models
# from gensim.models.fasttext import FastText

from sklearn.preprocessing import LabelEncoder

import gzip
import shutil


def parse_data():
    with open("dataset.json") as file:
        data = json.load(file)
    labels = []
    docs_x = []
    docs_y = []

    # Looping through our data
    for intent in data['intents']:
        for pattern in intent['patterns']:
            pattern = pattern.lower()
            # Creating a list of words
            words = nltk.tokenize.RegexpTokenizer(r'\w+').tokenize(pattern)
            docs_x.append(' '.join(map(str, words)))  # words has all words in a sentence
            docs_y.append(intent['tag'])
        if intent['tag'] not in labels:
            labels.append(intent['tag'])
        # doc means sentence
    labels = sorted(labels)
    print(labels)
    return docs_x, docs_y, labels


def encode_labels(docs_y):
    print(docs_y)
    label_encoder = LabelEncoder()
    label_encoder.fit(docs_y)
    output = label_encoder.transform(docs_y)
    print('docs_y embedded:', len(output))

    return output


def embed(docs_x, docs_y, labels):
    training = []
    output = []
    out_empty = [0 for _ in range(len(labels))]

    for index, doc in enumerate(docs_x):
        print(doc)
        doc_vec = ft_model.get_sentence_vector(doc)
        training.append(doc_vec)
        output_row = out_empty[:]
        output_row[labels.index(docs_y[index])] = 1
        output.append(output_row)
        print(output_row)

    return training, output


def loadEmbeddingModel():
    ft_path = 'cc.en.300.bin.gz'
    with gzip.open(ft_path, 'rb') as f_in:
        with open('cc.en.300.bin', 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)
    ft_model = ft.load_model('cc.en.300.bin')

    return ft_model


def train(training, output):
    model = RandomForestClassifier().fit(training, output)
    return model


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    ft_model = loadEmbeddingModel()
    docs_x, docs_y, labels = parse_data()
    # output = encode_labels(docs_y)
    training, output = embed(docs_x, docs_y, labels)
    output = np.array(output)
    print("_______________________")

    print(training[0])

    training = np.array(training)
    print(output[0])
    print(training[0])
    print(len(training), len(output))
    #print(training.shape)
    #training = training.reshape((nsamples,nx*ny))
    #print(nsamples,' ' , nx, ' ' ,ny)
    with open("data.pickle", "wb") as f:
        pickle.dump((training, output), f)
    model = train(training, output)
    with open("model.pickle", "wb") as f:
        pickle.dump((training, output), f)
    doc_vec = ft_model.get_sentence_vector("Hey Janet")

    print(model.predict([doc_vec]))
