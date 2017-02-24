
from gensim.models import Word2Vec
import numpy as np

rebuild = True

def learn_word_representation(sentences, save=False):
    if rebuild:
        print("Learning model...")
        model = Word2Vec(sentences, size=100, min_count=5, workers=4)
        model.init_sims(replace=True)
        wordsVectors = {word: model[word] for word in model.vocab.keys()}
        if save:
            print("Saving model...")
            np.save('wordsVectors', wordsVectors)
    else:
        print("Loading word representations...")
        wordsVectors = np.load('wordsVectors.npy').item()
    return wordsVectors

def build_vectors_for_mails(words_per_mail_id, vectors_for_words):
    vectors_for_mails = {}
    for mid, words in words_per_mail_id.iteritems():
        try:
            vectors_for_mails[mid] = np.mean(operator.itemgetter(*words)(vectors_for_words))
        except:
            vectors_for_mails[mid] = np.zeros(100)
            lgth = 0
            for word in words:
                if word in vectors_for_words:
                    vectors_for_mails[mid] += vectors_for_words[word]
                    lgth += 1
            if lgth > 0:
                vectors_for_mails[mid] /= lgth
            else:
                del vectors_for_mails[mid]
    return vectors_for_mails