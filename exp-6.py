import random
from collections import defaultdict

def build_bigram_model(text):
    words = text.lower().split()
    bigram_model = defaultdict(list)

    for i in range(len(words) - 1):
        bigram_model[words[i]].append(words[i + 1])

    return bigram_model

def generate_text(bigram_model, start_word, length=10):
    current_word = start_word
    generated = [current_word]

    for _ in range(length - 1):
        next_words = bigram_model.get(current_word)
        if not next_words:
            break
        current_word = random.choice(next_words)
        generated.append(current_word)

    return " ".join(generated)

# Sample text
text = "twinkle twinkle little star how i wonder what you are"

bigram_model = build_bigram_model(text)
generated_text = generate_text(bigram_model, "twinkle", 2)

print("Generated Text:")
print(generated_text)