"""
Main file to run.

"""
import argparse
import os
import random
import string

import nltk
from nltk.corpus import brown as n_brown

import haiku
from postag import Tagger

STOPLIST = set(nltk.corpus.stopwords.words())


def is_content_word(word):
    """A content word is not on the stoplist and its first character is a letter."""
    return word.lower() not in STOPLIST and word[0].isalpha()


def make_haikus(source):
    tagger = Tagger(n_brown.tagged_sents(categories="fiction", tagset="universal"))
    tags = tagger.tag(source)
    return haiku.arrange_haiku(tags, 4)


def random_generator(size=4, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


if __name__ == "__main__":
    # creates and trains tagger
    parser = argparse.ArgumentParser(description="Haiku generator")
    parser.add_argument("--custom-text")
    parser.add_argument("--store", action="store_true")
    args = vars(parser.parse_args())
    haikus = []
    if args.get('custom_text', None):
        path = args['custom_text']
        if os.path.isfile(path):
            with open(path, "r") as input:
                text = input.read()
            haikus = make_haikus(nltk.word_tokenize(text))
            print(*haikus, sep="\n")
    else:
        haikus = make_haikus(n_brown.words(categories="news"))
        print(*haikus, sep="\n")
    if args.get("store", None):
        file_name = "generated_poems\\haikus_" + random_generator() + ".txt"
        with open(file_name, "w") as output:
            output.write("\n".join(haikus))
