import random

# Open the corpus
corpus_file = open("pg1342.txt", 'r')
corpus_text = corpus_file.read()
#print(corpus_text)

# Split it into words
words = corpus_text.split(' ')

# Pick a random word
r = random.Random()
current_word = r.sample(words, 1)[0]

outp_string = current_word

for x in range(20):
    # Get all the indices of where this word occurs
    indices = [i for i, x in enumerate(words) if x == current_word]

    # Build a list of the words that occur after our chosen word
    next_words = [x for i, x in enumerate(words)  if (i-1) in indices]
    # Pick a second word that occurs after this one
    next_word = r.sample(next_words, 1)[0]
    outp_string += " " + next_word
    current_word = next_word

print outp_string.strip('\n')

