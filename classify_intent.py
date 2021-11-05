import codecs
import json

import numpy as np
import math

import embed_data



def load_embedded_intents():
    obj_text = codecs.open('embedded_data.json', 'r', encoding='utf-8').read()
    data = json.loads(obj_text)

    return data


def cosine_similarity(A, B):
    sim = np.dot(A, B) / (np.linalg.norm(A) * np.linalg.norm(B))

    return sim


def get_intent_similarity(data, input_vec, sim_dict):
    for intent in data['intents']:
        sum = 0
        for pattern in intent['patterns']:

            pattern = np.array(pattern)
            similarity = cosine_similarity(pattern, input_vec)
            
            sum = sum + similarity
        intent_sim_score = sum / len(intent['patterns'])
        sim_dict[intent['tag']] = intent_sim_score
    return sim_dict


if __name__ == '__main__':
    data = load_embedded_intents()
    sim_dict = {}
    input = "ok bye"
    ft_model = embed_data.load_embedding_model()
    input_vec = embed_data.embed_sentence(input, ft_model)
    sim_dict = get_intent_similarity(data, input_vec, sim_dict)
    print(sim_dict)
    output_intent = max(sim_dict, key=sim_dict.get)
    print("INPUT----->", input)
    print("OUTPUT-----> ", output_intent)
