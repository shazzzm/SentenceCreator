import random
import nltk

def get_next_words(words, current_word):
    return [words[i+1] for i,x in enumerate(words) if x == current_word]

# Open some Jane Austin!
corpus_file = open("pg1342.txt", 'r')
corpus_text = corpus_file.read()

# Setup NLTK
sentence_tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')

# Split our file into sentences
sentences = sentence_tokenizer.tokenize(corpus_text)
#sentences = corpus_text.split('.')
# Get the first word from each sentence
sentence_start_words = [x.split(' ')[0] for x in sentences]

# Split it into words
words = corpus_text.split(' ')

# Pick a random word
r = random.Random()
current_word = r.sample(sentence_start_words, 1)[0]

outp_string = current_word

while True:
    # Get all the indices of where this word occurs
    #indices = get_word_occurances_indices(words, current_word)

    # Build a list of the words that occur after our chosen word
    next_words = get_next_words(words, current_word)
    
    # If there's no more words then stop
    if len(next_words) == 0:
        break
    
    # Pick a second word that occurs after this one
    next_word = r.sample(next_words, 1)[0]
    outp_string += " " + next_word
    current_word = next_word
    
    if current_word[-1] == '.' or current_word[-1] == '\n':
        break
        

print(outp_string.strip('\r\n'))

