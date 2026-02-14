import re

def rule_based_pos_tagger(sentence):
    words = sentence.split()
    tagged = []

    for word in words:
        if re.fullmatch(r'.*ing$', word):
            tag = 'VBG'
        elif re.fullmatch(r'.*ed$', word):
            tag = 'VBD'
        elif re.fullmatch(r'.*ly$', word):
            tag = 'RB'
        elif re.fullmatch(r'.*ous$', word):
            tag = 'JJ'
        elif re.fullmatch(r'.*ness$', word):
            tag = 'NN'
        elif re.fullmatch(r'[0-9]+', word):
            tag = 'CD'
        elif re.fullmatch(r'[A-Z].*', word):
            tag = 'NNP'
        else:
            tag = 'NN'

        tagged.append((word, tag))

    return tagged


sentence = "Running quickly John finished 5 tasks"
print(rule_based_pos_tagger(sentence))
