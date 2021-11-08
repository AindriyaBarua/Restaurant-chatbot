from nltk.tokenize import RegexpTokenizer
from nltk.stem.wordnet import WordNetLemmatizer

'''
Since the dataset is small, using NLTK stop words stripped it off many words that were important for this context 
So I wrote a small script to get words and their frequencies in the whole document, and manually selected 
inconsequential words to make this list 
'''

stop_words = ['the', 'you', 'i', 'are', 'is', 'a', 'me', 'to', 'can', 'this', 'your', 'have', 'any', 'of', 'we', 'very',
              'could', 'please', 'it', 'with', 'here', 'if', 'my', 'am']


def lemmatize_sentence(tokens):
    lemmatizer = WordNetLemmatizer()
    lemmatized_tokens = [lemmatizer.lemmatize(word) for word in tokens]
    return lemmatized_tokens


def tokenize_and_remove_punctuation(sentence):
    tokenizer = RegexpTokenizer(r'\w+')
    tokens = tokenizer.tokenize(sentence)
    return tokens


def remove_stopwords(word_tokens):
    filtered_tokens = []
    for w in word_tokens:
        if w not in stop_words:
            filtered_tokens.append(w)
    return filtered_tokens


'''
Convert to lower case,
remove punctuation
lemmatize
'''


def preprocess_main(sent):
    sent = sent.lower()
    tokens = tokenize_and_remove_punctuation(sent)
    lemmatized_tokens = lemmatize_sentence(tokens)
    orig = lemmatized_tokens
    filtered_tokens = remove_stopwords(lemmatized_tokens)
    if len(filtered_tokens) == 0:
        # if stop word removal removes everything, don't do it
        filtered_tokens = orig
    normalized_sent = " ".join(filtered_tokens)
    return normalized_sent
