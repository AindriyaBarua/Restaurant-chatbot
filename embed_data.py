import nltk
import numpy as np
import tflearn
import tensorflow as tf
import random
import json
import pickle
import fasttext as ft

import gzip
import shutil
import string


def parse_data(ft_model):
    with open("dataset.json") as file:
        data = json.load(file)
    orig_data = data
    labels = []
    embedded_patterns = []
    # Looping through our data
    for intent in data['intents']:
        print(intent)

        for pattern in intent['patterns']:
            pattern = pattern.lower()
            pattern.translate(str.maketrans('', '', string.punctuation))
            embedded_sentence = embed_sentence(pattern, ft_model)
            embedded_patterns.append(embedded_sentence)
        intent['patterns'] = np.array(embedded_patterns).tolist()

        # doc means sentence
    labels = sorted(labels)
    print(labels)
    print('____________________________')
    print(data)

    return data


def embed_sentence(sentence, ft_model):
    sentence_vec = ft_model.get_sentence_vector(sentence)
    return sentence_vec


def write_embedded_data(data):
    json_object = json.dumps(data, indent=4)

    with open("embedded_data.json", "w") as outfile:
        outfile.write(json_object)


def load_embedding_model():
    ft_path = 'cc.en.300.bin.gz'
    with gzip.open(ft_path, 'rb') as f_in:
        with open('cc.en.300.bin', 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)
    ft_model = ft.load_model('cc.en.300.bin')

    return ft_model


if __name__ == '__main__':
    ft_model = load_embedding_model()
    embedded_data = parse_data(ft_model)
    write_embedded_data(embedded_data)

