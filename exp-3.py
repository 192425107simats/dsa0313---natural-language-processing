import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

sentence = "The children are playing happily"

tokens = word_tokenize(sentence)
print("Tokens:", tokens)
pos_tags = pos_tag(tokens)
print("POS Tags:", pos_tags)