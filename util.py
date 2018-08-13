# https://deeplearningcourses.com/c/deep-learning-recurrent-neural-networks-in-python
# https://udemy.com/deep-learning-recurrent-neural-networks-in-python
from __future__ import print_function, division
from builtins import range
import string
# Note: you may need to update your version of future
# sudo pip install -U future


import numpy as np

def init_weight(Mi, Mo):
    return np.random.randn(Mi, Mo) / np.sqrt(Mi + Mo)

def all_parity_pairs(nbit):
    # total number of samples (Ntotal) will be a multiple of 100
    # why did I make it this way? I don't remember.
    N = 2**nbit
    remainder = 100 - (N % 100)
    Ntotal = N + remainder
    X = np.zeros((Ntotal, nbit))
    Y = np.zeros(Ntotal)
    for ii in range(Ntotal):
        i = ii % N
        # now generate the ith sample
        for j in range(nbit):
            if i % (2**(j+1)) != 0:
                i -= 2**j
                X[ii,j] = 1
        Y[ii] = X[ii].sum() % 2
    return X, Y

def remove_punctuation(s):
    return s.translate(None, string.punctuation)

def get_robert_frost():
    word2idx = {'START': 0, 'END': 1}
    current_idx = 2
    sentences = []
    
    for line in open('../hmm_class/robert_frost.txt'):
            line = line.strip()
            if line:
                tokens = remove_punctuation(line.lower()).split()
                sentence = []
                for t in tokens:
                    if t not in word2idx:
                        word2idx[t] = current_idx
                        current_ix += 1
                        
                    idx = word2idx[t]
                    sentence.append(idx)
                
                sentences.append(sentence)
        
    return sentences, word2idx