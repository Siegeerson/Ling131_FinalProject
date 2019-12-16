"""
Our haiku generator
"""

import random

VOWELS = ['a','e','i','o','u','y']
TAGS = ['ADJ', 'ADV', 'DET', 'NOUN', 'NN', 'NUM', 'VERB', 'ADP', 'PRT', 'CONJ']
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
        # if tag == 'VERB':
        #     syll -= 1
        if (wordL[-3] not in VOWELS) and (wordL[-3] not in ['x', 'c', 's', 'z', 'h', 'g']):
            syll -= 1

    if len(wordL) > 2 and wordL[-2:] == 'ed':
        if (wordL[-3] not in VOWELS) and (wordL[-3] in ['n', 'm', 'k', 'g','s', 'z', 'h']):
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
        if not(cur == 'u' and word[i-1] == 'q'):
            if not(cur == 'e' and i + 1 == len(word)):
                if not(i > 0 and is_syll(word, i-1, syll)):
                    return True
            elif syll == 0 and (cur == 'e' and i + 1 == len(word)):
                return True

    return False

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
        cur = 'S'
        haiku = ""
        for x in [5,7,5]:
            line = []
            linesyl = 0
            while linesyl < x:
                types = SENTENCE[cur][:]
                options = []
                new_cur = ""
                while len(options) < 1 and len(types) > 0:
                    new_cur = random.choice(types)
                    options = [entry for entry in info if entry[1] == new_cur if entry[2] <= (x - linesyl)]
                    types.remove(new_cur)
                nextword = random.choice(options)
                line.append(nextword[0])
                linesyl += nextword[2]
                # print("line {}: {}".format(x, nextword))
                cur = new_cur
            haiku += " ".join(line) + "\n"
        haikus.append(haiku)
    return haikus

# print(estimate_syll('eyes'))
