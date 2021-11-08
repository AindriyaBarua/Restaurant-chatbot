"""
Developed by Aindriya Barua in November, 2021
"""

import codecs
import json

import numpy as np

import embed_data
import preprocess_sentence


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

    return max_sim_intent


if __name__ == '__main__':
    data = load_embedded_intents()

    ft_model = embed_data.load_embedding_model()

    input = "Hey!"
    print("INPUT----->", input)
    input = preprocess_sentence.preprocess_main(input)
    input_vec = embed_data.embed_sentence(input, ft_model)
    output_intent = detect_intent(data, input_vec)
    print("OUTPUT-----> ", output_intent, "\n")

    input = "What are the working hours of the restaurant?"
    print("INPUT----->", input)
    input = preprocess_sentence.preprocess_main(input)
    input_vec = embed_data.embed_sentence(input, ft_model)
    output_intent = detect_intent(data, input_vec)
    print("OUTPUT-----> ", output_intent, "\n")

    input = "Are there any seats available now?"
    print("INPUT----->", input)
    input = preprocess_sentence.preprocess_main(input)
    input_vec = embed_data.embed_sentence(input, ft_model)
    output_intent = detect_intent(data, input_vec)
    print("OUTPUT-----> ", output_intent, "\n")

    input = "Ok, please book a table for me"
    print("INPUT----->", input)
    input = preprocess_sentence.preprocess_main(input)
    input_vec = embed_data.embed_sentence(input, ft_model)
    output_intent = detect_intent(data, input_vec)
    print("OUTPUT-----> ", output_intent, "\n")

    input = "Give me your address"
    print("INPUT----->", input)
    input = preprocess_sentence.preprocess_main(input)
    input_vec = embed_data.embed_sentence(input, ft_model)
    output_intent = detect_intent(data, input_vec)
    print("OUTPUT-----> ", output_intent, "\n")

    input = "I am not sure about sanitation safety in COVID"
    print("INPUT----->", input)
    input = preprocess_sentence.preprocess_main(input)
    input_vec = embed_data.embed_sentence(input, ft_model)
    output_intent = detect_intent(data, input_vec)
    print("OUTPUT-----> ", output_intent, "\n")

    input = "OK. Whats the menu?"
    print("INPUT----->", input)
    input = preprocess_sentence.preprocess_main(input)
    input_vec = embed_data.embed_sentence(input, ft_model)
    output_intent = detect_intent(data, input_vec)
    print("OUTPUT-----> ", output_intent, "\n")

    input = "You have any suggestion?"
    print("INPUT----->", input)
    input = preprocess_sentence.preprocess_main(input)
    input_vec = embed_data.embed_sentence(input, ft_model)
    output_intent = detect_intent(data, input_vec)
    print("OUTPUT-----> ", output_intent, "\n")

    input = "I am vegetarian"
    print("INPUT----->", input)
    input = preprocess_sentence.preprocess_main(input)
    input_vec = embed_data.embed_sentence(input, ft_model)
    output_intent = detect_intent(data, input_vec)
    print("OUTPUT-----> ", output_intent, "\n")

    input = "Do you serve vegan food?"
    print("INPUT----->", input)
    input = preprocess_sentence.preprocess_main(input)
    input_vec = embed_data.embed_sentence(input, ft_model)
    output_intent = detect_intent(data, input_vec)
    print("OUTPUT-----> ", output_intent, "\n")

    input = "Can I know the recipe of the Pad-Thai noodles?"
    print("INPUT----->", input)
    input = preprocess_sentence.preprocess_main(input)
    input_vec = embed_data.embed_sentence(input, ft_model)
    output_intent = detect_intent(data, input_vec)
    print("OUTPUT-----> ", output_intent, "\n")

    input = "Tell me more about the Thukpa recipe"
    print("INPUT----->", input)
    input = preprocess_sentence.preprocess_main(input)
    input_vec = embed_data.embed_sentence(input, ft_model)
    output_intent = detect_intent(data, input_vec)
    print("OUTPUT-----> ", output_intent, "\n")

    input = "I just finished eating, loved the food!"
    print("INPUT----->", input)
    input = preprocess_sentence.preprocess_main(input)
    input_vec = embed_data.embed_sentence(input, ft_model)
    output_intent = detect_intent(data, input_vec)
    print("OUTPUT-----> ", output_intent, "\n")

    input = "Hate the staff behavior though"
    print("INPUT----->", input)
    input = preprocess_sentence.preprocess_main(input)
    input_vec = embed_data.embed_sentence(input, ft_model)
    output_intent = detect_intent(data, input_vec)
    print("OUTPUT-----> ", output_intent, "\n")

    input = "Ok I will leave now, Bye!"
    print("INPUT----->", input)
    input = preprocess_sentence.preprocess_main(input)
    input_vec = embed_data.embed_sentence(input, ft_model)
    output_intent = detect_intent(data, input_vec)
    print("OUTPUT-----> ", output_intent, "\n")
