"""
Developed by Aindriya Barua in November, 2021
https://codepen.io/sajadhsm/pen/odaBdd
https://towardsdatascience.com/how-to-build-a-basic-chatbot-from-scratch-f63a2ccf5262
https://raw.githubusercontent.com/iampratheesh/Restaurant-Chatbot/master/templates/index.html


"""

import codecs
import json

import numpy as np

import data_embedder
import sentence_normalizer

obj_text = codecs.open('embedded_data.json', 'r', encoding='utf-8').read()
data = json.loads(obj_text)

ft_model = data_embedder.load_embedding_model()


def normalize(vec):
    norm = np.linalg.norm(vec)

    return norm


def cosine_similarity(A, B):
    normA = normalize(A)
    normB = normalize(B)
    sim = np.dot(A, B) / (normA * normB)
    return sim


def detect_intent(data, input_vec):
    max_sim_score = -1
    max_sim_intent = ''
    max_score_avg = -1
    break_flag = 0

    for intent in data['intents']:

        scores = []
        intent_flag = 0
        tie_flag = 0
        for pattern in intent['patterns']:

            pattern = np.array(pattern)
            similarity = cosine_similarity(pattern, input_vec)
            similarity = round(similarity, 6)
            scores.append(similarity)
            # if exact match is found, then no need to check any further
            if similarity == 1.000000:
                intent_flag = 1
                break_flag = 1
                # no need to check any more sentences in this intent
                break
            elif similarity > max_sim_score:
                max_sim_score = similarity
                intent_flag = 1
            # if a sentence in this intent has same similarity as the max and this max is from a previous intent,
            # that means there is a tie between this intent and some previous intent
            elif similarity == max_sim_score and intent_flag == 0:
                tie_flag = 1
        '''
        If tie occurs check which intent has max top 4 average
        top 4 is taken because even without same intent there are often different ways of expressing the same intent,
        which are vector-wise less similar to each other.
        Taking an average of all of them, reduced the score of those clusters
        '''

        if tie_flag == 1:
            scores.sort()
            top = scores[:min(4, len(scores))]
            intent_score_avg = np.mean(top)
            if intent_score_avg > max_score_avg:
                max_score_avg = intent_score_avg
                intent_flag = 1

        if intent_flag == 1:
            max_sim_intent = intent['tag']
        # if exact match was found in this intent, then break 'cause we don't have to iterate through anymore intents
        if break_flag == 1:
            break
    if break_flag != 1 and ((tie_flag == 1 and intent_flag == 1 and max_score_avg < 0.06) or (intent_flag == 1 and max_sim_score < 0.6)):
        max_sim_intent = ""

    return max_sim_intent


def classify(input):
    input = sentence_normalizer.preprocess_main(input)
    input_vec = data_embedder.embed_sentence(input, ft_model)
    output_intent = detect_intent(data, input_vec)
    return output_intent

if __name__ == '__main__':
    input = sentence_normalizer.preprocess_main("hmm")
    input_vec = data_embedder.embed_sentence(input, ft_model)
    output_intent = detect_intent(data, input_vec)
    print(output_intent)

    input = sentence_normalizer.preprocess_main("nice food")
    input_vec = data_embedder.embed_sentence(input, ft_model)
    output_intent = detect_intent(data, input_vec)
    print(output_intent)

