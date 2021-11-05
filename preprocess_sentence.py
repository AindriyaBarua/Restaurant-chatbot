import string

import nltk
from nltk.corpus import stopwords
from pywsd.utils import lemmatize_sentence

#nltk.download('averaged_perceptron_tagger')
stop_words = set(stopwords.words('english'))

def remove_punctuation(sentence):
    return sentence.translate(str.maketrans('', '', string.punctuation))

def remove_stopwords(word_tokens):
    filtered_tokens = []
    for w in word_tokens:
        if w not in stop_words:
            filtered_tokens.append(w)
    return filtered_tokens


def preprocess_main(sent):
    sent = sent.lower()
    sent = remove_punctuation(sent)
    lemmatized_tokens = lemmatize_sentence(sent)
    orig = lemmatized_tokens
    filtered_tokens = remove_stopwords(lemmatized_tokens)
    if len(filtered_tokens) == 0:
        filtered_tokens = orig
    normalized_sent = " ".join(filtered_tokens)
    return normalized_sent
