import re
import csv
import time
import random
import nltk
import string
import gensim
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
from sklearn.decomposition import PCA
from sklearn.metrics import euclidean_distances
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity as cosine
from sklearn.metrics import accuracy_score
from sklearn.datasets import fetch_20newsgroups
#from sklearn.metrics import classification_report

nltk.download('stopwords')
stpwds = set(nltk.corpus.stopwords.words("english"))

#############
# functions #
#############

# returns the vector of the word
def my_vector_getter(word, wv):
    try:
        index = unique_tokens.index(word)
		# we use reshape because cosine similarity in sklearn
		# now works only for multidimensional arrays
        word_array = wv[index].reshape(1,-1)
        return (word_array)
    except ValueError:
        print 'word: <', word, '> not in vocabulary!'

# returns cosine similarity between two word vectors
def my_cos_similarity(word1, word2, wv):
    sim = cosine(my_vector_getter(word1, wv),my_vector_getter(word2, wv)) 
    return (round(sim, 4))

# plots word vectors
def plot_points(my_names, my_wv):
    
    my_vectors = [my_vector_getter(elt, wv=my_wv) for elt in my_names]
    dim_1_coords = [element[0,0] for element in my_vectors]
    dim_2_coords = [element[0,1] for element in my_vectors]
    
    fig = plt.figure()
    ax = fig.add_subplot(111)
    plt.plot(dim_1_coords, dim_2_coords, 'ro')
    plt.axis([min(dim_1_coords)-0.1, max(dim_1_coords)+0.1, min(dim_2_coords)-0.1, max(dim_2_coords)+0.1])
    
    for x, y, name in zip(dim_1_coords , dim_2_coords, my_names):     
        ax.annotate(name, xy=(x, y))
    	
    plt.grid()
    plt.show()

# performs basic pre-processing
def clean_string(string):
    # remove formatting
    str = re.sub('\s+', ' ', string)
	# remove punctuation (preserving dashes)
    str = ''.join(l for l in str if l not in punct)
    # remove dashes that are not intra-word
    str = my_regex.sub(lambda x: (x.group(1) if x.group(1) else ' '), str)
    # strip extra white space
    str = re.sub(' +',' ',str)
    # strip leading and trailing white space
    str = str.strip()
    return str

######################################
# experimenting with word embeddings #
######################################

# my_path should be the absolute path poiting to where the files are located on your machine

my_path = 'C:\\Users\\mvazirg\\Desktop\\INF582 Text mining\\Lab04_03_02_2017\\final\\data\\'

# read unique tokens
with open(my_path + 'unique_tokens.txt','r') as file:
    unique_tokens = file.read().splitlines()

# read word vectors associated with the unique tokens
with open(my_path + 'word_vectors.csv', 'r') as file:
    reader = csv.reader(file)
    word_vectors = list(reader)
	
# convert to numpy array
word_vectors = np.array(word_vectors).astype(np.float)

# sanity check (should return True)
len(unique_tokens) == word_vectors.shape[0]

# two similar words
my_cos_similarity('man','woman', wv=word_vectors)

# two dissimilar words
my_cos_similarity('man','however', wv=word_vectors)

# examples of concepts captured in the embedding space:

# country-capital
France = my_vector_getter('France', wv=word_vectors)
Paris = my_vector_getter('Paris', wv=word_vectors)
Germany = my_vector_getter('Germany', wv=word_vectors)
Berlin = my_vector_getter('Berlin', wv=word_vectors)

operation = France - Paris + Berlin
round(cosine(operation, Germany),5)

# singular-plural
student = my_vector_getter('student', wv=word_vectors)
students = my_vector_getter("students", wv=word_vectors)
car = my_vector_getter('car', wv=word_vectors)
cars = my_vector_getter('cars', wv=word_vectors)

operation = students - student + car
round(cosine(operation, cars),5)

# we will visualize regularities among word vectors in the space made of the first two principal directions
my_pca = PCA(n_components=2) # to fill
wv_2d = my_pca.fit_transform(word_vectors) # to fill
# check
wv_2d.shape

plot_points(my_names=['France','Paris','Germany','Berlin'], my_wv=wv_2d)

plot_points(my_names=['students','student','car','cars','box','boxes'], my_wv=wv_2d)


s_1 = 'Kennedy was shot dead in Dallas'
s_2 = 'The President was killed in Texas'

# compute the features of the vector space (unique non-stopwords)

# remove stopwords
s_1 = [word for word in s_1.split(' ') if word.lower() not in stpwds]
s_2 = [word for word in s_2.split(' ') if word.lower() not in stpwds] # to fill

# the features are all the unique remaining words
features = list(set(s_1).union(set(s_2)))

# project the two sentences in the vector space
p_1 = [1 if feature in s_1 else 0 for feature in features]
p_2 = [1 if feature in s_2 else 0 for feature in features] # to fill

p_1_bow = zip(features, p_1)
p_2_bow = zip(features, p_2) # to fill

print "representation of '", s_1, "' : \n",
print p_1_bow

print "representation of '", s_2, "' : \n",
print p_2_bow

# 1) compute the similarity of these two sentences in the vector space
# of course, they have zero similarity since the dot product of the two vectors is equal to zero (they are orthogonal) - the two sentences have no word in common

round(cosine(np.array(p_1).reshape(1,-1),np.array(p_2).reshape(1,-1)), 5)

# now, if we use the word embedding space

p_1_embeddings = np.concatenate([my_vector_getter(word, word_vectors) for word in s_1])

p_2_embeddings = np.concatenate([my_vector_getter(word, word_vectors) for word in s_2])

# compute centroids
centroid_1 = np.mean(p_1_embeddings, axis=0).reshape(1,-1)
centroid_2 = np.mean(p_2_embeddings, axis=0).reshape(1,-1)

# 2) compute cosine similarity between sentence centroids
# this time we can see that the semantic similarity between the two sentences is captured
round(cosine(centroid_1, centroid_2),5)

# load our custom model
my_model = gensim.models.word2vec.Word2Vec.load(my_path + 'custom_w2v_model.txt')

# replace our custom word vectors by Google ones
# this is a trick to load only the Google News word vectors corresponding to our vocabulary - otherwise takes too much RAM
# ! executing the command below should take about one minute
my_model.intersect_word2vec_format(my_path + 'GoogleNews-vectors-negative300.bin.gz', binary=True)

# # the model can be queried like a dictionary
# # and returns as value the vector associated with the key, e.g.:
# my_model['astronomy']
# should be very small
my_model.wmdistance(s_1,s_2)

# should be null
my_model.wmdistance(s_1,s_1)

# compare with a completely different sentence
# we can see that it is higher
s_3 = 'not all computer science students are geeks'
s_3 = [word for word in s_3.split(' ') if word.lower() not in stpwds]
my_model.wmdistance(s_2,s_3)


##################
# classification #
##################

# we will use those two categories`
categories = ['comp.graphics', 'sci.space']

# load data set
newsgroups = fetch_20newsgroups(subset='test',remove=('headers', 'footers', 'quotes'),categories=categories)

documents, labels = newsgroups.data, newsgroups.target

index_long_docs = [i for i, doc in enumerate(documents) if len(doc)>4500]

# remove long documents (otherwise takes too much time with the WMD)
documents = [documents[i] for i in range(len(documents)) if i not in index_long_docs]

# of course, do the same for labels to maintain 1-1 matching
labels = [labels[i] for i in range(len(labels)) if i not in index_long_docs]

punct = string.punctuation.replace('-', '')
# regex to remove intra-word dashes
my_regex = re.compile(r"(\b[-']\b)|[\W_]")

lists_of_tokens = []

# clean
for doc in documents:
    doc = clean_string(doc)
    # tokenize (split based on whitespace)
    tokens = doc.split(' ')
    # remove stopwords
    tokens = [token for token in tokens if token not in stpwds]
    # remove tokens less than 2 characters in size
    tokens = [token for token in tokens if len(token)>2]
    # save result
    lists_of_tokens.append(tokens)

my_path = 'C:\\Users\\mvazirg\\Desktop\\INF582 Text mining\\Lab04_03_02_2017\\'

# Knn classification with 4-fold cross-validation

tfidf_vectorizer = TfidfVectorizer(stop_words = stpwds, preprocessor=clean_string, lowercase=False) 
# note: we do not lowercase for comparison purposes with Google News embeddings (which have been learned on non-lowercased text)

def neighbors_predict(instance, collection, my_labels, wmd_or_tfidf):
    
    # compute WMD or cosine similarity between the new (never seen) instance and each instance in the collection
    
    if wmd_or_tfidf == 'wmd':
        sims = []
        for doc in collection:
            # ! wmdistance works on lists of strings (idx 1 in the tuples)
            sims.append(my_model.wmdistance(' '.join(instance[1]).lower().split(), ' '.join(doc[1]).lower().split()))
		    # get indexes of elements sorted by INCREASING order (!distance)
            sorted_idx = sorted(range(len(sims)), key=lambda x: sims[x])
    
    elif wmd_or_tfidf == 'tfidf':
        # ! tfidf_vectorizer works on raw text (idx 0 in the tuples)
        doc_term_matrix = tfidf_vectorizer.fit_transform([elt[0] for elt in collection])
        
        # note that we just transform
        # fitting has been done on the collection
        instance_vector = tfidf_vectorizer.transform([instance[0]])
        
        # computes cosine similarity between new instance and all elements in the collection
        sims = cosine(doc_term_matrix, Y=instance_vector, dense_output=True).tolist()
        
        sims = [elt[0] for elt in sims]
        
        # get indexes of elements sorted by DECREASING order
        sorted_idx = sorted(range(len(sims)), key=lambda x: sims[x], reverse=True)
    
    predictions = []
     
	# we use odd numbers to break ties
    for k_nn in [3,7,11,17]:
        # get labels of k_nn nearest neighbors
        nn_labels = [my_labels[i] for i in sorted_idx][:k_nn]
        
        # get most represented label
        counts = dict(Counter(nn_labels))
        max_counts = max(counts.values())
        prediction = [k for k,v in counts.iteritems() if v==max_counts][0]
        		
        predictions.append(prediction)
    
    return predictions
		
		  
n_folds = 4

fold_size = int(round(len(documents)/float(n_folds))) - 1
			  
index_folds = []
index_fold = []
k = 0

for i in range(len(documents)):
    index_fold.append(i)
    k += 1
    if k == fold_size:
        print k
        index_folds.append(index_fold)
        index_fold = []
        k = 0
		
instances = zip(documents, lists_of_tokens)

t = time.time()

# at each iteration, we use 3 folds for 'training' and 1 for testing
fold_results = []
kk = 0

performance_wmd = []
performance_tfidf = []

for fold in range(n_folds):
    training_fold_indexes = [elt for elt in range(n_folds) if elt != fold]
    training_indexes = [index_folds[idx] for idx in training_fold_indexes]
    # flatten list of lists into a list
    training_indexes = [idx for sublist in training_indexes for idx in sublist]
    # because it is very time consuming, we only retain 100 instances randomly selected
    training_indexes_subset = random.sample(training_indexes, 100)
    instances_train = [instances[idx] for idx in training_indexes_subset]
    labels_train = [labels[idx] for idx in training_indexes_subset]
    	
    # here, no flattening needed since we only select the elements from a single sublist
    test_indexes = index_folds[fold]
    # again, to save time, we only generate predictions for 20 randomly selected instances
    test_indexes_subset = random.sample(test_indexes, 20)
    instances_test = [instances[idx] for idx in test_indexes_subset]
    labels_test = [labels[idx] for idx in test_indexes_subset]
    
    # generate predictions for the instances in the test set
    predictions_wmd_fold = []
    predictions_tfidf_fold = []
    kkk = 0
    for instance in instances_test:
        predictions_wmd_fold.append(neighbors_predict(instance=instance, collection=instances_train, my_labels=labels_train, wmd_or_tfidf='wmd')) # to fill
        predictions_tfidf_fold.append(neighbors_predict(instance=instance, collection=instances_train, my_labels=labels_train, wmd_or_tfidf='tfidf'))# to fill
        print kkk
        kkk+=1
    
    # compute performance for each value of k_nn
    accuracy_wmd_fold = []
    accuracy_tfidf_fold = []	
    for j in range(len([3,7,11,17])):
        accuracy_wmd_fold.append(accuracy_score(y_true=labels_test,y_pred=[elt[j] for elt in predictions_wmd_fold]))
        accuracy_tfidf_fold.append(accuracy_score(y_true=labels_test,y_pred=[elt[j] for elt in predictions_tfidf_fold]))
    
    performance_wmd.append(accuracy_wmd_fold)
    performance_tfidf.append(accuracy_tfidf_fold)
    	
    print 'fold', kk+1, 'done in', round(time.time() - t), 'secs'
    t = time.time()
    kk += 1
	
pwmd = np.array(performance_wmd)
ptfidf = np.array(performance_tfidf)

np.mean(pwmd, axis=0)
np.mean(ptfidf, axis=0)



