import random
import nltk

def get_word_occurances_indices(words, current_word):
    return [i for i, x in enumerate(words) if x == current_word]

def get_next_possible_words(words, indices):
    return [words[i+1] for i in indices]
    
def get_next_words(words, current_word):
    return [words[i+1] for i,x in enumerate(words) if x == current_word]

# Open some Jane Austin!
corpus_file = open("pg1342.txt", 'r')
corpus_text = corpus_file.read()

# Setup NLTK
sentence_tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')

# Split our file into sentences
sentences = sentence_tokenizer.tokenize(corpus_text)

# Get the first word from each sentence
sentence_start_words = [x.split(' ')[0] for x in sentences]

sentence_end_words = [x.split(' ')[-1] for x in sentences]

# Split it into words
words = corpus_text.split(' ')

# Pick a random word
r = random.Random()
current_word = r.sample(sentence_start_words, 1)[0]

outp_string = current_word

not_sentence_end = True

while not_sentence_end:
    # Get all the indices of where this word occurs
    #indices = get_word_occurances_indices(words, current_word)

    # Build a list of the words that occur after our chosen word
    next_words = get_next_words(words, current_word)
    
    # Pick a second word that occurs after this one
    next_word = r.sample(next_words, 1)[0]
    outp_string += " " + next_word
    current_word = next_word
    
    if current_word in sentence_end_words:
        if r.random() > 0.5:
            not_sentence_end = False
        

print(outp_string.strip('\r\n'))

