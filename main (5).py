import random

print("Welcome to Hangman game!")


fin = open('words.txt')

words = [line.strip().lower() for line in fin.readlines()]

while True:
    word = random.choice(words)

    length = len(word)

    print(f"Guess the word with {length} letters!")

    word_list = []
    for i in range(length):
        word_list.append('_')

    print(*word_list)

    while True:
        letter = input("Guess a letter: ")

        for i in range(length):
            if letter == word[i]:
                word_list[i] = letter
                
        if '_' not in word_list:
            print("You won!")
            break
        
        print(*word_list)






