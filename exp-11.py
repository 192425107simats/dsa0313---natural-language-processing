tokens = []
pos = 0

def match(expected):
    global pos
    if pos < len(tokens) and tokens[pos] == expected:
        pos += 1
        return True
    return False

def S():
    return NP() and VP()

def NP():
    return Det() and N()

def VP():
    return V() and NP()

def Det():
    return match('the') or match('a')

def N():
    return match('boy') or match('girl')

def V():
    return match('sees') or match('likes')

sentence = "the boy sees a girl"
tokens = sentence.split()
pos = 0

if S() and pos == len(tokens):
    print("Sentence is grammatically correct")
else:
    print("Sentence is NOT grammatically correct")
