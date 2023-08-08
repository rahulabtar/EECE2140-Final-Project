
import random 

def get_all_words_of_size(size):
    words_to_guess = []
    with open('1-1000.txt','r') as file:
        for line in file:
            word = line.strip('\n')
            if len(word) == size:
                words_to_guess.append(word)
    return words_to_guess

def pick_word_to_guess(words_to_guess):
    index = random.randint(1,len(words_to_guess))
    return words_to_guess[index]

word = pick_word_to_guess(get_all_words_of_size(5))
print(word)

#This code reads in the word to be guessed as a dictionary, with key is letter and value is list of indexes of where letter occurs
def get_word_dict(word):
    word_dict = {}
    for char2 in word:
        letter = char2
        positions = []
        for index, char in enumerate(word):
            if char == letter:
                positions.append(index)
        word_dict[char2] = set(positions)
    return word_dict

def compare_dicts(word,guess):
    letters_in_common = []
    for key in guess:
        if key in word:
            letters_in_common.append(key)
    return letters_in_common

def check_indexes(word,guess,letters_in_common):
    right_indexes, letters_correct = [], []
    for element in letters_in_common:
        if word[element] & guess[element] != set():
            right_indexes.append(word[element] & guess[element])
            letters_correct.append(element)
    return [int(element) for subset in right_indexes for element in subset], letters_correct
        
def get_clean(word,guess): #a cleaner way to get the results needed, in one simple function. Uses branch system
    list = []
    for i in range(len(word)):
        list.append(['',''])
    for i in range(len(guess)):
        if guess[i] not in word:
            list[i] = [guess[i],'0']
        elif guess[i] in word and guess[i] != word[i]:
            list[i] = [guess[i],'!']
        elif guess[i] in word and guess[i] == word[i]:
            list[i] = [guess[i],'*'] 
    return list

board = [] #fills board before hand, 5 letter words, 3 lives
for i in range(3):
    row = []
    for j in range(5):
        row.append(['0','0'])
    board.append(row)

    
board[0] = get_clean('grape','abcde')
print(board)
board[1] = get_clean('grape','grape')
print(board)

            




