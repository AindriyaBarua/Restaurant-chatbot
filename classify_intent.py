import codecs
import json

import numpy as np
#import sklearn

import embed_data

import preprocess_sentence


# from sklearn.metrics.pairwise import cosine_similarity


def load_embedded_intents():
    obj_text = codecs.open('embedded_data.json', 'r', encoding='utf-8').read()
    data = json.loads(obj_text)

    return data

def normalize(vec):
    norm = np.linalg.norm(vec)

    return norm

def cosine_similarity(A, B):
    normA = normalize(A)
    normB = normalize(B)
    sim = np.dot(A, B) / (normA * normB)
    return sim
'''
just lower case and not removing punctuation not working -- similarity not working
should lemmatise, stem
remove stop words
'''

def detect_intent(data, input_vec):

    max_sim_score = -1
    max_sim_intent = ''
    max_score_avg = -1
    break_flag = 0

    for intent in data['intents']:
        #print("--------------------------CHECKING INTENT:", intent['tag'])
        #print("Present leading intent= ", max_sim_intent)
        #print(max_sim_score)
        #sum = 0
        scores = []
        intent_flag = 0
        tie_flag = 0
        for pattern in intent['patterns']:

            pattern = np.array(pattern)
            similarity = cosine_similarity(pattern, input_vec)
            similarity = round(similarity, 6)
            scores.append(similarity)

            if similarity == 1.000000:
                intent_flag = 1
                break_flag = 1
                break
            elif similarity > max_sim_score:
                    max_sim_score = similarity
                    intent_flag = 1
            elif similarity == max_sim_score and intent_flag == 0:
                    tie_flag = 1

        if tie_flag ==1:
            scores.sort()
            top = scores[:min(4,len(scores))]
            intent_score_avg = np.mean(top)
            if intent_score_avg > max_score_avg:
                max_score_avg = intent_score_avg
                intent_flag = 1

        if intent_flag == 1:
            max_sim_intent = intent['tag']

        if break_flag == 1:
            break

    return max_sim_intent


if __name__ == '__main__':
    data = load_embedded_intents()

    ft_model = embed_data.load_embedding_model()

    input = "I just finished eating, loved the food!"
    input = preprocess_sentence.preprocess_main(input)
    input_vec = embed_data.embed_sentence(input, ft_model)
    output_intent = detect_intent(data, input_vec)
    print("INPUT----->", input)
    print("OUTPUT-----> ", output_intent)


    input = "Hate the staff behavior though"
    input = preprocess_sentence.preprocess_main(input)
    input_vec = embed_data.embed_sentence(input, ft_model)
    output_intent = detect_intent(data, input_vec)
    print("INPUT----->", input)
    print("OUTPUT-----> ", output_intent)





