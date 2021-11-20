"""
Developed by Aindriya Barua in November, 2021
"""

import numpy as np

import json
import fasttext as ft

import sentence_normalizer


def parse_data(ft_model):
    with open("dataset.json") as file:
        data = json.load(file)

    embedded_patterns = []
    for intent in data['intents']:

        for pattern in intent['patterns']:
            pattern = sentence_normalizer.preprocess_main(pattern)
            embedded_sentence = embed_sentence(pattern, ft_model)

            embedded_patterns.append(embedded_sentence)
        intent['patterns'] = np.array(embedded_patterns).tolist()


    return data


def embed_sentence(sentence, ft_model):
    sentence_vec = ft_model.get_sentence_vector(sentence)
    return sentence_vec


def write_embedded_data(data):
    json_object = json.dumps(data, indent=4)

    with open("embedded_data.json", "w") as outfile:
        outfile.write(json_object)


def load_embedding_model():
    ft_model = ft.load_model('cc.en.300.bin')
    return ft_model


if __name__ == '__main__':
    ft_model = load_embedding_model()
    embedded_data = parse_data(ft_model)
    write_embedded_data(embedded_data)

