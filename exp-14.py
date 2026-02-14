import nltk
from nltk import CFG
from nltk.parse import RecursiveDescentParser

grammar = CFG.fromstring("""
S -> NP_SG VP_SG
S -> NP_PL VP_PL
NP_SG -> Det N_SG
NP_PL -> Det N_PL
VP_SG -> V_SG
VP_PL -> V_PL
Det -> 'the'
N_SG -> 'boy'
N_PL -> 'boys'
V_SG -> 'runs'
V_PL -> 'run'
""")

parser = RecursiveDescentParser(grammar)

def check_agreement(sentence):
    words = sentence.split()
    for _ in parser.parse(words):
        return "Sentence has correct agreement"
    return "Sentence has agreement error"

sentence = "the boy runs"
print(check_agreement(sentence))
