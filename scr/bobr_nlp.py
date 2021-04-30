import numpy as np
import random
import pickle

def get_ansver(text):
    with open('scr/clf.pickle', 'rb') as handle:
        clf = pickle.load(handle)
    with open('scr/vectorizer.pickle', 'rb') as handle:
        vectorizer = pickle.load(handle)
    with open('scr/le.pickle', 'rb') as handle:
        le = pickle.load(handle)
    pred_wars = np.argsort(clf.predict_proba(vectorizer.transform([text]))[0])[:10]
    answer = le.inverse_transform([random.choice(pred_wars)])
    return answer[0]