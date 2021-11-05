import codecs
import json

import numpy as np
import math

import embed_data


# from sklearn.metrics.pairwise import cosine_similarity


def load_embedded_intents():
    obj_text = codecs.open('embedded_data.json', 'r', encoding='utf-8').read()
    data = json.loads(obj_text)

    return data


def cosine_similarity(A, B):
    sim = np.dot(A, B) / (np.linalg.norm(A) * np.linalg.norm(B))
    if sim != sim:
        print("sus cosineXXXXXXXXXXXXXXXXXXXXXXXXX")
        print(A)
        print(B)
        print(np.linalg.norm(A))
        print(np.linalg.norm(B))

    return sim
'''
just lower case and not removing punctuation not working -- similarity not working
should lemmatise, stem
remove stop words
'''

def get_intent_similarity(data, input_vec, sim_dict):
    for intent in data['intents']:
        sum = 0
        for pattern in intent['patterns']:

            pattern = np.array(pattern)
            similarity = cosine_similarity(pattern, input_vec)
            #print(similarity)
            #if similarity == similarity:
            sum = sum + similarity
            '''
            else:
                print("nan was here xxxxxxxxxxxxxxxxxxxxxxxxxxx")
                print(intent['tag'])
                print(similarity)
                print(pattern)
                print(input_vec)
                print(np.linalg.norm(pattern))
                print(np.linalg.norm(input_vec))
                print("XXXXXXXXXXXXXXXXXXXXXXXXXXX")'''
        #print("sum =  ",sum)
        #print("len(intent['patterns'])", len(intent['patterns']))
        intent_sim_score = sum / len(intent['patterns'])
        #print(intent_sim_score)
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

    input = "what do you suggest"
    ft_model = embed_data.load_embedding_model()
    input_vec = embed_data.embed_sentence(input, ft_model)
    sim_dict = get_intent_similarity(data, input_vec, sim_dict)
    print(sim_dict)
    output_intent = max(sim_dict, key=sim_dict.get)
    print("INPUT----->", input)
    print("OUTPUT-----> ", output_intent)
    '''
    input = "ok bye"
    ft_model = embed_data.load_embedding_model()
    input_vec = embed_data.embed_sentence(input, ft_model)
    sim_dict = get_intent_similarity(data, input_vec, sim_dict)
    print(sim_dict)
    output_intent = max(sim_dict, key=sim_dict.get)
    print("INPUT----->", input)
    print("OUTPUT-----> ", output_intent)

    input = "tell me the menu"
    ft_model = embed_data.load_embedding_model()
    input_vec = embed_data.embed_sentence(input, ft_model)
    sim_dict = get_intent_similarity(data, input_vec, sim_dict)
    print(sim_dict)
    output_intent = max(sim_dict, key=sim_dict.get)
    print("INPUT----->", input)
    print("OUTPUT-----> ", output_intent)

    input = "what do you suggest"
    ft_model = embed_data.load_embedding_model()
    input_vec = embed_data.embed_sentence(input, ft_model)
    sim_dict = get_intent_similarity(data, input_vec, sim_dict)
    print(sim_dict)
    output_intent = max(sim_dict, key=sim_dict.get)
    print("INPUT----->", input)
    print("OUTPUT-----> ", output_intent)

    input = "are you a bot?"
    ft_model = embed_data.load_embedding_model()
    input_vec = embed_data.embed_sentence(input, ft_model)
    sim_dict = get_intent_similarity(data, input_vec, sim_dict)
    print(sim_dict)
    output_intent = max(sim_dict, key=sim_dict.get)
    print("INPUT----->", input)

    print("OUTPUT-----> ", output_intent)

    input = "hey"
    ft_model = embed_data.load_embedding_model()
    input_vec = embed_data.embed_sentence(input, ft_model)
    sim_dict = get_intent_similarity(data, input_vec, sim_dict)
    print(sim_dict)
    output_intent = max(sim_dict, key=sim_dict.get)
    print("INPUT----->", input)

    print("OUTPUT-----> ", output_intent)


    input = "love the food"
    ft_model = embed_data.load_embedding_model()
    input_vec = embed_data.embed_sentence(input, ft_model)
    sim_dict = get_intent_similarity(data, input_vec, sim_dict)
    print(sim_dict)
    output_intent = max(sim_dict, key=sim_dict.get)
    print("INPUT----->", input)

    print("OUTPUT-----> ", output_intent)

    input = "i hate the staff"
    ft_model = embed_data.load_embedding_model()
    input_vec = embed_data.embed_sentence(input, ft_model)
    sim_dict = get_intent_similarity(data, input_vec, sim_dict)
    print(sim_dict)
    output_intent = max(sim_dict, key=sim_dict.get)
    print("INPUT----->", input)

    print("OUTPUT-----> ", output_intent)

    input = "what are your working hours"
    ft_model = embed_data.load_embedding_model()
    input_vec = embed_data.embed_sentence(input, ft_model)
    sim_dict = get_intent_similarity(data, input_vec, sim_dict)
    print(sim_dict)
    output_intent = max(sim_dict, key=sim_dict.get)
    print("INPUT----->", input)

    print("OUTPUT-----> ", output_intent)

    input = "whats the recipe of the thai noodles?"
    ft_model = embed_data.load_embedding_model()
    input_vec = embed_data.embed_sentence(input, ft_model)
    sim_dict = get_intent_similarity(data, input_vec, sim_dict)
    print(sim_dict)
    output_intent = max(sim_dict, key=sim_dict.get)
    print("INPUT----->", input)

    print("OUTPUT-----> ", output_intent)

    input = "do you have available tables?"
    ft_model = embed_data.load_embedding_model()
    input_vec = embed_data.embed_sentence(input, ft_model)
    sim_dict = get_intent_similarity(data, input_vec, sim_dict)
    print(sim_dict)
    output_intent = max(sim_dict, key=sim_dict.get)
    print("INPUT----->", input)

    print("OUTPUT-----> ", output_intent)

    input = "how do i reach the restaurant?"
    ft_model = embed_data.load_embedding_model()
    input_vec = embed_data.embed_sentence(input, ft_model)
    sim_dict = get_intent_similarity(data, input_vec, sim_dict)
    print(sim_dict)
    output_intent = max(sim_dict, key=sim_dict.get)
    print("INPUT----->", input)

    print("OUTPUT-----> ", output_intent)

    input = "whats the help desk phone number?"
    ft_model = embed_data.load_embedding_model()
    input_vec = embed_data.embed_sentence(input, ft_model)
    sim_dict = get_intent_similarity(data, input_vec, sim_dict)
    print(sim_dict)
    output_intent = max(sim_dict, key=sim_dict.get)
    print("INPUT----->", input)

    print("OUTPUT-----> ", output_intent)
    '''
