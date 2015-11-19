import random
import nltk

# Open some Jane Austin!
corpus_file = open("pg1342.txt", 'r')
corpus_text = corpus_file.read()

# Setup NLTK
sentence_tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')

# Split our file into sentences
sentences = sentence_tokenizer.tokenize(corpus_text)

# Get the first word from each sentence
sentence_start_words = [x.split(' ')[0] for x in sentences]

# Split it into words
words = corpus_text.split(' ')

# Pick a random word
r = random.Random()
current_word = r.sample(sentence_start_words, 1)[0]

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

print(outp_string.strip('\r\n'))

