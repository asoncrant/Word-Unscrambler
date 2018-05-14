import sys, random
#file = sys.argv[1] 
try: 
    input = raw_input
except NameError:
    pass

file = sys.argv[1]
# open file and split on new lines
#file = open(file, 'r')
data = open(file, 'r')
words = data.read().splitlines()
data.close()

# read through word by word
lengths_dict = {} #will be a dictionary mapping word lengths to another dictionary mapping sorted words to their originals
lengths = []
for w in words:
    w = w.lower() # convert to lower case
    w_alph = "".join(sorted(w)) # sort word letters alphabetically
    size = len(w_alph) # keep track of size
    lengths.append(size) # append to lengths (to be drawn from randomly later)
    if size not in lengths_dict.keys(): # if new size is encountered, initialize
        lengths_dict[size] = {}
    try:
        # check to see if word is in dictionary with sorted words as keys
        # If not, append it
        if w not in lengths_dict[size][w_alph]: 
            lengths_dict[size][w_alph].append(w)
        
    except KeyError: 
        # if that sorted word hasn't been encountered yet, initialize
        lengths_dict[size][w_alph] = []
        lengths_dict[size][w_alph].append(w)
        

k = 0
while True:
    # print welcome message, instructions for playing
    print("Welcome to asoncran's word unscrambler!")
    print("First, type the length of the word with which you'd like to be challenged:")
    # collect user input
    w_len = input("(type q to quit or type Enter to pick a random word): " )
    
    if w_len == "q": # if the user wants to quit
        print("Thanks for enjoying %s games of asoncran's word unscrambler!" %k)
        break
        
    else: # if user wants to play
        if w_len == "": # if no length is specified
            # pick random length from lengths vector
            # pick random alphabetized word of that length
            # permute that random word
            w_len = random.choice(list(lengths)) 
            rand_alph = random.choice(list(lengths_dict[w_len].keys()))
            word_perm = ''.join(random.sample(rand_alph,len(rand_alph)))
        
        elif int(w_len) not in lengths_dict.keys(): # if the length requested is unavailable
            print("There is no word of length %s. Please pick a different length" %w_len)
            continue
        
        else: # valid length is specified and available
            # pick random word of specified length
            # permute that random word
            w_len = int(w_len)
            rand_alph = random.choice(list(lengths_dict[w_len].keys()))
            word_perm = ''.join(random.sample(rand_alph,len(rand_alph)))
        
        # ask user to unscramble the permuted word
        guess_string = "Unscramble the word '%s': " %word_perm
        guess = input(guess_string)
    
        if guess in lengths_dict[w_len][rand_alph]: # if the user guesses correctly
            print("Correct!")
            print("Correct Answers %s:" %lengths_dict[w_len][rand_alph])
        else: # if the user guesses incorrectly
            print("Sorry, that is incorrect.")
            print("Correct Answers %s:" %lengths_dict[w_len][rand_alph])
        # incrememnt by one
        k += 1
            