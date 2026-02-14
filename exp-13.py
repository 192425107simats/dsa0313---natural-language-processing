import nltk
from nltk import CFG
from nltk.parse import RecursiveDescentParser

grammar = CFG.fromstring("""
S -> NP VP
NP -> Det N
VP -> V NP
Det -> 'the' | 'a'
N -> 'boy' | 'girl'
V -> 'sees' | 'likes'
""")

parser = RecursiveDescentParser(grammar)

sentence = "the boy sees a girl".split()

for tree in parser.parse(sentence):
    print(tree.pformat())
