# Simple training data (word, POS)
training_data = [
    ('the', 'DT'),
    ('dog', 'NN'),
    ('cat', 'NN'),
    ('runs', 'VB'),
    ('eats', 'VB')
]

# Function for stochastic POS tagging
def pos_tagger(sentence):
    words = sentence.lower().split()
    result = []

    for word in words:
        tag = 'NN'   # default tag
        for w, t in training_data:
            if word == w:
                tag = t
                break
        result.append((word, tag))

    return result

# Input sentence
sentence = "the dog eats"
tagged = pos_tagger(sentence)

# Output
print("Word\tPOS")
for word, tag in tagged:
    print(word, "\t", tag)