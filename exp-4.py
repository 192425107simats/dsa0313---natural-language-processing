def pluralize(noun):
    if noun.endswith(('s', 'x', 'z', 'ch', 'sh')):
        return noun + 'es'
    elif noun.endswith('y') and noun[-2] not in 'aeiou':
        return noun[:-1] + 'ies'
    else:
        return noun + 's'

nouns = ["cat", "dog", "bus", "box", "baby", "lady"]

for n in nouns:
    print(n, "->", pluralize(n))