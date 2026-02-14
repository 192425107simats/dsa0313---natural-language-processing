import nltk

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

text = "The quick brown fox jumps over the lazy dog"

tokens = nltk.word_tokenize(text)

pos_tags = nltk.pos_tag(tokens)

print("Word\tPOS Tag")
for word, tag in pos_tags:
    print(f"{word}\t{tag}")