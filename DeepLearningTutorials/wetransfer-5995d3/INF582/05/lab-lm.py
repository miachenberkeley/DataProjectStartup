import nltk
import sys

# Import the Presidential inaugural speeches corpus
from nltk.corpus import inaugural

# Import the gutenberg corpus                                                                               
from nltk.corpus import gutenberg

# Import NLTK's ngram module (for building language models)
# It has been removed from standard NLTK, so we access it from the nltkx package
sys.path.extend(['/path/to/nltkx'])

from nltkx import model
from nltkx.model.counter import build_vocabulary, count_ngrams
from nltkx.model.ngram import MLENgramModel, LidstoneNgramModel, LaplaceNgramModel





#################### EXERCISE 1 ####################

# Solution for exercise 1
# Input: doc_name (string)
# Output: total_words (int), total_distinct_words (int)
def ex1(doc_name):
    # Use the plaintext corpus reader to access a pre-tokenised list of words
    # for the document specified in "doc_name"
    doc_words = inaugural.words(doc_name)

    # Find the total number of words in the speech
    #total_words =

    # Find the total number of DISTINCT words in the speech
    #total_distinct_words = 

    # Return the word counts
    return (total_words, total_distinct_words)


### Uncomment to test exercise 1
#speech_name = '2009-Obama.txt'
#(tokens,types) = ex1(speech_name)
#print "Total words in %s: %s"%(speech_name,tokens)
#print "Total distinct words in %s: %s"%(speech_name,types)



#################### EXERCISE 2 ####################

# Solution for exercise 2
# Input: doc_name (string)
# Output: avg_word_length (float)
def ex2(doc_name):
    doc_words = inaugural.words(doc_name)

    # Construct a list that contains the word lengths for each DISTINCT word in the document
    #distinct_word_lengths = 

    # Find the average word length
    #avg_word_length =

    # Return the average word length of the document
    return avg_word_length


### Uncomment to test exercise 2 
#speech_name = '2009-Obama.txt'
#result2 = ex2(speech_name)
#print "Average word length for %s: %s"%(speech_name,result2)




#################### EXERCISE 3 ####################

# Solution for exercise 3
# Input: doc_name (string), x (int)
# Output: top_words (list)
def ex3(doc_name, x):
    doc_words = inaugural.words(doc_name)
    
    # Construct a frequency distribution over the lowercased words in the document
    #fd_doc_words = 

    # Find the top x most frequently used words in the document
    #top_words = 

    # Return the top x most frequently used words
    return top_words


### Uncomment to test exercise 3
#print "Top 50 words for Obama's 2009 speech:"
#result3a = ex3('2009-Obama.txt', 50)
#print result3a
#print "Top 50 words for Washington's 1789 speech:"
#result3b = ex3('1789-Washington.txt', 50)
#print result3b


#################### EXERCISE 4 ####################

# Solution for exercise 4
# Input: doc_name (string), n (int)
# Output: lm (NgramModel language model)
def ex4(doc_name, n):
   # words =
   # sents =

   # vocab =
   # counter =
   # lm =
   
   # Return the language model (we'll use it in exercise 5)
   return lm


### Uncomment to test exercise 4
# result4 = ex4('austen-sense.txt',2)
# print "Sense and Sensibility bigram language model built"



#################### EXERCISE 5 ####################

# Solution for exercise 5
# Input: lm (MLENgramModel language model, from exercise 4), word (string), context (list)
# Output: p (float)
def ex5(lm,word,context):
   # Compute the probability for the word given the context
   # p =
   # Return the probability
   return p


### Uncomment to test exercise 5
# result5a = ex5(result4,'for',['reason'])
# print "Probability of \'reason\' followed by \'for\': %s"%result5a
# result5b = ex5(result4,'end',['the'])
# print "Probability of \'the\' followed by \'end\': %s"%result5b
# result5c = ex5(result4,'the',['end'])
# print "Probability of \'end\' followed by \'the\': %s"%result5c




#################### EXERCISE 6 ####################

# Solution for exercise 6
# Input: doc_name (string), n (int)
# Output: print the probability for the word in the context according to each LM
def ex6(doc_name, n, word, context):
   # words =
   # sents =

   # vocab =
   # counter =
   
   # lm_mle =
   # lm_lap =
   # lm_lid =
   
   # print the probabilities
   # ...
   return



#################### EXERCISE 7 ####################

# Solution for exercise 7
# Input: word (string), context (string)
# Output: p (float)
# Compute the unsmoothed (MLE) probability for word given the single word context
def ex7(word,context):
   p = 0.0
   
   austen_words = [w.lower() for w in gutenberg.words('austen-sense.txt')]
   austen_bigrams = zip(austen_words[:-1], austen_words[1:])  # list of bigrams as tuples
   # (above doesn't include begin/end of corpus: but basically this is fine)
   
   # Compute probability of word given context. Make sure you use float division.
   # p = ...
   
   # Return probability
   return p


# ### Uncomment to test exercise 0
# print "MLE:"
# result0a = ex0('end','the')
# print "Probability of \'end\' given \'the\': " + str(result0a)
# result0b = ex0('the','end')
# print "Probability of \'the\' given \'end\': " + str(result0b)


#################### EXERCISE 8 ####################

# Solution for exercise 8
# Input: word (string), context (string)
# Output: p (float)
# Compute the Laplace smoothed probability for word given the single word context
def ex8(word,context):
    p = 0.0

    austen_words = [w.lower() for w in gutenberg.words('austen-sense.txt')]
    austen_bigrams = zip(austen_words[:-1], austen_words[1:])  # list of bigrams as tuples
    # (above doesn't include begin/end of corpus: but basically this is fine)
    
    # compute the vocabulary size
    # V = ... 

    # Compute probability of word given context
    #p = ...

    # Return probability
    return p


### Uncomment to test exercise 1
# print "LAPLACE:"
# result1a = ex1('end','the')
# print "Probability of \'end\' given \'the\': " + str(result1a)
# result1b = ex1('the','end')
# print "Probability of \'the\' given \'end\': " + str(result1b)



#################### EXERCISE 9 ####################
# Solution for exercise 2
# Input: word (string), context (string), alpha (float)
# Output: p (float)
# Compute the Lidstone smoothed probability for word given the single word context
# Alpha is the smoothing parameter, normally between 0 and 1.
def ex9(word,context,alpha):
    p =0.0

    austen_words = [w.lower() for w in gutenberg.words('austen-sense.txt')]
    austen_bigrams = zip(austen_words[:-1], austen_words[1:])  # list of bigrams as tuples

    # compute the vocabulary size
    # V = ... 

    # Compute probability of word given context
    #p = ...

    # Return probability
    return p


### Uncomment to test exercise 2
# print "LIDSTONE, alpha=0.01:"
# result2a = ex2('end','the',.01)
# print "Probability of \'end\' given \'the\': " + str(result2a)
# result2b = ex2('the','end',.01)
# print "Probability of \'the\' given \'end\': " + str(result2b)
# print "LIDSTONE, alpha=0:"
# result2c = ex2('end','the',0)
# print "Probability of \'end\' given \'the\': " + str(result2c)
# result2d = ex2('the','end',0)
# print "Probability of \'the\' given \'end\': " + str(result2d)
# print "LIDSTONE, alpha=1:"
# result2e = ex2('end','the',1)
# print "Probability of \'end\' given \'the\': " + str(result2e)
# result2f = ex2('the','end',1)
# print "Probability of \'the\' given \'end\': " + str(result2f)






#################### EXERCISE 10 ####################

# Solution for exercise 10 - entropy calculation
# Input: lm (language model), doc_name (string)
# Output: e (float)
def ex4_tot_entropy(lm,doc_name):
    e = 0.0

    # Construct a list of all the words from the document (test document)
    # doc_words = ...
    
    # Compute the TOTAL cross entropy of the text in doc_name
    #e = ...

    # Return the entropy
    return e

# Solution for exercise 10 - per-word entropy calculation
# Input: lm (language model), doc_name (string)
# Output: e (float)
def ex4_perword_entropy(lm,doc_name):
    e = 0.0

    # Construct a list of all the words from the document (test document)
    # doc_words = ...

    # Compute the PER-WORD cross entropy of the text in doc_name
    # e = ...

    # Return the entropy
    return e


# Solution for exercise 10 - language model training
# Input: doc_name (string)
# Output: l (language model)
def ex10_lm(doc_name):
    l = None

    # Train a trigram language model using doc_name with Lidstone probability distribution with +0.01 added to the sample count for each bin
    # l =

    # Return the language model
    return l

### Uncomment to test exercise 4
# lm4 = ex10_lm('austen-sense.txt')
# result4a = ex4_tot_entropy(lm4,'austen-emma.txt')
# print "Total cross-entropy for austen-emma.txt: " + str(result4a)
# result4b = ex4_tot_entropy(lm4,'chesterton-ball.txt')
# print "Total cross-entropy for chesterton-ball.txt: " + str(result4b)
# result4c = ex4_perword_entropy(lm4,'austen-emma.txt')
# print "Per-word cross-entropy for austen-emma.txt: " + str(result4c)
# result4d = ex4_perword_entropy(lm4,'chesterton-ball.txt')
# print "Per-word cross-entropy for chesterton-ball.txt: " + str(result4d)

