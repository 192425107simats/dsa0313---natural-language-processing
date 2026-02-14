def initial_tagger(words):
    return [(word, 'NN') for word in words]

def apply_rules(tagged_words):
    transformed = []

    for i, (word, tag) in enumerate(tagged_words):
        if word.endswith('ing'):
            tag = 'VBG'
        elif word.endswith('ly'):
            tag = 'RB'
        elif word.lower() in ['is', 'are', 'was', 'were']:
            tag = 'VB'
        elif tag == 'NN' and i > 0 and tagged_words[i-1][1] == 'DT':
            tag = 'NN'
        transformed.append((word, tag))

    return transformed


sentence = "The boy is running quickly"
words = sentence.split()

initial_tags = initial_tagger(words)
final_tags = apply_rules(initial_tags)

print(final_tags)
