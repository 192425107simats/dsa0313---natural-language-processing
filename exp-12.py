grammar = {
    'S': [['NP', 'VP']],
    'NP': [['Det', 'N']],
    'VP': [['V', 'NP']],
    'Det': [['the'], ['a']],
    'N': [['boy'], ['girl']],
    'V': [['sees'], ['likes']]
}

def earley_parser(sentence):
    words = sentence.split()
    n = len(words)
    chart = [set() for _ in range(n + 1)]

    chart[0].add(('S', tuple(grammar['S'][0]), 0, 0))

    for i in range(n + 1):
        changed = True
        while changed:
            changed = False
            for state in list(chart[i]):
                lhs, rhs, dot, start = state

                if dot < len(rhs):
                    next_sym = rhs[dot]

                    if next_sym in grammar:
                        for prod in grammar[next_sym]:
                            new_state = (next_sym, tuple(prod), 0, i)
                            if new_state not in chart[i]:
                                chart[i].add(new_state)
                                changed = True

                    elif i < n and next_sym == words[i]:
                        chart[i + 1].add((lhs, rhs, dot + 1, start))
                else:
                    for st in chart[start]:
                        l, r, d, s = st
                        if d < len(r) and r[d] == lhs:
                            new_state = (l, r, d + 1, s)
                            if new_state not in chart[i]:
                                chart[i].add(new_state)
                                changed = True

    return ('S', tuple(grammar['S'][0]), 1, 0) in chart[n]

sentence = "the boy sees a girl"
if earley_parser(sentence):
    print("Sentence is grammatically correct")
else:
    print("Sentence is NOT grammatically correct")
