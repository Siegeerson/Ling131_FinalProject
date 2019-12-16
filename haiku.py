"""
Our haiku generator
"""

import re

VOWELS = ['a','e','i','o','u','y']
SENTENCES = {
            'DET'   : ['ADJ', 'NOUN'],
            'ADJ'   : ['ADJ', 'NOUN'],
            'NOUN'  : ['VERB', 'NOUN', 'PREP'],
            'VERB'  : ['ADV', 'PREP'],
            'PREP'  : ['NOUN', 'DET', 'PREP'],
            'ADV'   : ['ADV', 'PREP']
            }

def estimate_syll(word):
    """
    estimates the syllables that the given word has

    :param word: string of a word
    :return: int guess to number of syllables
    """
    w = list(word.lower())
    syll = 0
    for i in range(0, len(w)):
        if (is_syll(word, i)):
            syll += 1

    return syll

def is_syll(word, i):
    """
    decides if a letter is a new syllable in a word

    TODO:
    no way to tell if "ed" is a syllable (distracted) vs not a syllable (happened)
    no way to tell if wordfinal "es" is a syllable (foxes) vs not (becomes)
        maybe look at POS for both?


    :param word: whole word (string)
    :param i: index of current letter to be examined
    :return: true if is syllable, false if not
    """
    cur = word[i]
    if cur in VOWELS:
        if not(cur == 'u' and word[i-1] == 'q'):
            if not(cur == 'e' and i + 1 == len(word)):
                if not(i > 0 and is_syll(word, i-1)):
                    return True

    return False

def arrange_haiku(words_tags):
    """

    :param words_tags: tuple with (word, tag)
    :return: a haiku!
    """
    # ((the, DET), 1) for an example word entry
    info = [((word, tag), estimate_syll(word)) for word, tag in words_tags]
