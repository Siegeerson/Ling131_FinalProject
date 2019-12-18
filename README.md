# Ling131_FinalProject
### Ben Siege and Midgie Williams

## in main:
Trains a part of speech tagger on the Brown News Corpus.
Uses that tagger to tag the desired input.
Then uses the input and tagger to create a haiku with (extremely) loosely accurate syntax

## in haiku:
estimates the number of syllables in a word using vowel information and some (very) simple phonology
then uses the parts of speech and syllable counts for each word to create a three line poem,
where the first line has 5 syllables, the second 7 and the third 5.

## Required packages not in default library
* nltk
* all other files and folders included in this repositrory

## To Run
To generate haikus run the main.py file, this will print out 4 haikus generated using words
from the brown news corpus. For other behavior consult the optional arguments that can be passed in the command line

The haiku.py module can be used without main.py, it simply requires a list of
tuples of (word, tag) be passed in where the words are tagged with the NLTK universal tagset

### Optional Arguments for main.py
* --custom-text
    * requires a file address of a txt file be passed in
    * generates 4 haikus using the contents of the argument as the pool of words to draw from
    * for convenience several sample texts have been supplied in the data folder
* --store
    * stores a text file of haikus generated in the generated_poems folder
    * can be used with or without --custom-text
    * does not take any arguments