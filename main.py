"""
Main file to run.

"""
import re
import nltk
import haiku
import os
import argparse
from nltk.corpus import PlaintextCorpusReader
from nltk.corpus import brown as n_brown
from nltk.corpus import wordnet as wn
from postag import Tagger

STOPLIST = set(nltk.corpus.stopwords.words())

def is_content_word(word):
    """A content word is not on the stoplist and its first character is a letter."""
    return word.lower() not in STOPLIST and word[0].isalpha()


def make_haikus(source):
    tagger = Tagger(n_brown.tagged_sents(categories="fiction",tagset="universal"))
    tags = tagger.tag(source)
    return haiku.arrange_haiku(tags,4)


if __name__ == "__main__":
    # creates and trains tagger
    parser = argparse.ArgumentParser(description="Haiku generator")
    parser.add_argument("--custom-text")
    args = vars(parser.parse_args())
    if args.get('custom_text',None):
        path = args['custom_text']
        if os.path.isfile(path):
            text = ""
            with open(path,"r") as input:
                text = input.read()
            haikus = make_haikus(nltk.word_tokenize(text))
            print(*haikus,sep="\n")
    else:
        haikus = make_haikus(n_brown.words(categories="news"))
        print(*haikus,sep="\n")
