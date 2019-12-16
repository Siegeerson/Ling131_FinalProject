# import argparse
# import os
# Didn't seem to actually need the imports above
import re
import nltk
import cmudict
import haiku
from syllables import estimate
from nltk.corpus import PlaintextCorpusReader
from nltk.corpus import brown as n_brown
from nltk.corpus import wordnet as wn
from postag import Tagger

STOPLIST = set(nltk.corpus.stopwords.words())
cdict = cmudict.dict()

def is_content_word(word):
    """A content word is not on the stoplist and its first character is a letter."""
    return word.lower() not in STOPLIST and word[0].isalpha()

def tagger_train(a):
    """
    Trains a tagger based on the brown news corpus
    :param a: a tagger to train
    :return:
    """
    sents = n_brown.tagged_sents(categories="fiction",tagset="universal")
    sents_train = sents[0:int(len(sents) * .9)]
    a.train(sents_train)

def estimator(word):
    cword = cdict.get(word,None)
    if cword:
        cmudict_syllables = 0
        for phone in cword[0]:
            if re.match(r"\w*[012]$", phone):
                cmudict_syllables += 1
        return cmudict_syllables
    return estimate(word)

def cat(wordL,tagger):
    tags = tagger.tag(wordL)
    return {(word,estimator(word.lower()),tag)
        for word,tag in tags if is_content_word(word) }
    # return {(word,haiku.estimate_syll(word), tag)
    #         for word, tag in tags if is_content_word(word) }

def basic_construtor(p_words):
    out = []
    for x in [5,7,5]:
        line1 = []
        line1s = 0
        syl = x
        v_used = False
        while line1s != syl:
            c_word = p_words.pop()
            if line1s + c_word[1] <= syl and (c_word[2] == 'VERB') != v_used:
                if c_word[2] == 'VERB':
                    v_used = True
                line1.append(c_word[0])
                line1s +=c_word[1]
            else:
                p_words.add(c_word)
        print(*line1)
        out.append(line1)


if __name__ == "__main__":
    tagger = Tagger()
    tagger_train(tagger)
    cs = cat(n_brown.words(categories="news"),tagger)
    print(cs)
    basic_construtor(cs)
