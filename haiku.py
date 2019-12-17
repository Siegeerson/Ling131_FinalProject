"""
Our haiku generator
"""

import random

# Vowels, used to identify syllables
VOWELS = ['a','e','i','o','u','y']
# Parts of Speach which our haiku items can take
TAGS = ['ADJ', 'ADV', 'DET', 'NOUN', 'NN', 'NUM', 'VERB', 'ADP', 'PRT', 'CONJ']
# Transitions to make as close to a cohesive thought as possible
SENTENCE = {
            'S'     : ['DET', 'NUM', 'ADJ', 'NOUN', 'NN'],
            'DET'   : ['NUM', 'ADJ', 'NOUN', 'NN'],
            'NUM'   : ['ADJ', 'NOUN', 'NN'],
            'ADJ'   : ['NOUN', 'NN'],
            'NOUN'  : ['ADP', 'PRT', 'VERB'],
            'NN'    : ['ADP', 'PRT', 'VERB'],
            'ADP'   : ['DET', 'NUM', 'NOUN', 'NN'],
            'PRT'   : ['DET', 'NUM', 'NOUN', 'NN'],
            'VERB'  : ['ADV', 'ADP', 'PRT'],
            'ADV'   : ['CONJ', 'ADP', 'PRT'],
            'CONJ'  : ['DET', 'NUM', 'ADJ', 'NOUN', 'NN']
            }


def estimate_syll(word):
    """
    estimates the syllables that the given word has.

    :param word: string of a word
    :return: int guess to number of syllables
    """
    wordL = word.lower()
    w = list(wordL)
    syll = 0
    for i in range(0, len(w)):
        cur = is_syll(wordL, i, syll)
        # print("{} is syllable: {}".format(w[i], cur))
        if cur:
            syll += 1

    #Checks the special cases of the word ending in 'es' or in 'ed'
    # checks previous letter wasn't vowel because if it was, the 'es' wouldn't have been assigned a syllable
    if len(wordL) > 2 and wordL[-2:] == 'es':
        if (wordL[-3] not in VOWELS) and (wordL[-3] not in ['x', 'c', 's', 'z', 'h', 'g']):
            syll -= 1

    if len(wordL) > 2 and wordL[-2:] == 'ed':
        if (wordL[-3] not in VOWELS) and (wordL[-3] in ['n', 'm', 'k', 'g','s', 'z', 'h', 'w']):
            syll -= 1

    return syll

def is_syll(word, i, syll):
    """
    decides if a letter is a new syllable in a word

    :param word: whole word (string)
    :param i: index of current letter to be examined
    :return: true if is syllable, false if not
    """
    cur = word[i]
    if cur in VOWELS:
        if not is_qu(word, i):
            if not is_silent_e(word, i, syll):
                if not prev_is_syll(word, i, syll):
                    return True

    return False

def prev_is_syll(word, i, syll):
    """
    checks if the current letter is a second (or third) vowel in a single syllable
    """
    if syll > 0 and i > 0:
        if word[i-1] in VOWELS and not is_qu(word, i-1):
            return True
    return False

def is_silent_e(word, i, syll):
    """
    checks if the given vowel is a wordfinal "e" which has no syllable.
    (if it is wordfinal 'e' but no other syllable, will give it a syllable)
    """
    return (word[i] == 'e' and i + 1 == len(word)) and syll != 0

def is_qu(word, i):
    """
    checks if the given vowel is a 'u' after a 'q', because that should have a vowel.
    """
    return i > 0 and (word[i] == 'u' and word[i-1] == 'q')

def arrange_haiku(words_tags, num_haiku = 1):
    """

    :param words_tags: tuple with (word, tag)
    :param num_haiku: int number of haikus to generate; default is 1
    :return: a haiku!
    """
    # (the, 'DET', 1) for an example word entry
    info = [(word, tag, estimate_syll(word)) for word, tag in words_tags if tag in TAGS]
    info = [entry for entry in info if entry[2] > 0]
    haikus = []
    for i in range(0, num_haiku):
        # each haiku starts with the start symbol
        cur = 'S'
        haiku = ""
        # first line has 5 syllables, second has 7, third has 5
        for x in [5,7,5]:
            line = []
            linesyl = 0
            # while there need to be more syllables in the line
            while linesyl < x:
                types = SENTENCE[cur][:]
                options = []
                new_cur = ""
                # until you have some words to pick from which won't overload the syllable needs and are of a compatible next POS
                while len(options) < 1 and len(types) > 0:
                    new_cur = random.choice(types)
                    options = [entry for entry in info if entry[1] == new_cur if entry[2] <= (x - linesyl)]
                    types.remove(new_cur)
                nextword = random.choice(options)
                line.append(nextword[0])
                linesyl += nextword[2]
                cur = new_cur
            haiku += " ".join(line) + "\n"
        haikus.append(haiku)
    return haikus
