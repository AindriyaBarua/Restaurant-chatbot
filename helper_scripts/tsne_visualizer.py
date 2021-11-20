from sklearn.manifold import TSNE
import json
import numpy as np
from sklearn.cluster import KMeans

# embedded data has fasttext vectors of the sentences
with open("embedded_data_short.json") as file:
    data = json.load(file)

X = []

for intent in data['intents']:

    for pattern in intent['patterns']:
      if not (intent['tag'] == 'general'):
        pattern = np.array(pattern)
        X.append(pattern)


clusters = KMeans(n_clusters=5)
clusters.fit(X)

tsne = TSNEVisualizer()
tsne.fit(X, ["c{}".format(c) for c in clusters.labels_])
tsne.poof()