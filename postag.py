import gzip
import nltk
import os
import pickle

STORED_TAGGER = "trigram_tagger_pickle"

"""
The tagger class is a useful way of manipulating the taggers constructed rather than manually loading 
each time its needed
"""


class Tagger:
    def __init__(self):
        if os.path.exists(STORED_TAGGER):
            with gzip.open(STORED_TAGGER, "rb") as t:
                self.tagger = pickle.load(t)
        else:
            # if no tagger is trained use a default
            self.tagger = nltk.DefaultTagger('NN')

    def train(self, training_sents):
        default = nltk.DefaultTagger('NN')
        unigram = nltk.UnigramTagger(training_sents, backoff=default)
        self.tagger = nltk.BigramTagger(training_sents, backoff=unigram)
        with gzip.open(STORED_TAGGER, "wb") as st:
            pickle.dump(self.tagger, st)

    def tag(self, input_s):
        return self.tagger.tag(input_s)

    def evaluate(self, input_standard):
        return self.tagger.evaluate(input_standard)
