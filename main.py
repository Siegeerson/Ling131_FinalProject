"""
Main file to run.

"""
import re
import nltk
import haiku
from nltk.corpus import PlaintextCorpusReader
from nltk.corpus import brown as n_brown
from nltk.corpus import wordnet as wn
from postag import Tagger

STOPLIST = set(nltk.corpus.stopwords.words())

def is_content_word(word):
    """A content word is not on the stoplist and its first character is a letter."""
    return word.lower() not in STOPLIST and word[0].isalpha()

# def tagger_train(a):
#     """
#     Trains a tagger based on the brown news corpus
#     :param a: a tagger to train
#     :return:
#     """
#     sents = n_brown.tagged_sents(categories="fiction",tagset="universal")
#     sents_train = sents[0:int(len(sents) * .9)]
#     a.train(sents_train)

#
# def make_haikus(source, n):
#     tagger = Tagger()
#     tagger_train(tagger)
#     tags = tagger.tag(source)


if __name__ == "__main__":
    # creates and trains tagger
    tagger = Tagger(n_brown.tagged_sents(categories="fiction",tagset="universal"))
    # tagger_train(tagger)

    # applies tags to given word set (default is Brown "News")
    source = n_brown.words(categories="news")
    tags = tagger.tag(source)

    # creates haikus usuing the created tags, default number is 1 if no number is specified.
    haiku = haiku.arrange_haiku(tags, 5)
    for h in haiku:
        print(h)
        print()
