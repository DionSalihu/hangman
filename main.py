def main():
    import random
    guess_list = []
    index = 0
    wrong_guess = 5
    print("Welcome to Hangman game!")
    print("Type 'exit' if you want to exit the game!")
    guess_figures = [""" 
      --------    
     |        |   
     |            
     |            
     |            
     |            
    _|_           

      """
        ,
                     """
       
         --------       
        |        |   
        |        o    
        |            
        |            
        |            
       _|_
                  
      """,

                     """
         --------    
        |        |   
        |        o            
        |        |    
        |        |    
        |            
       _|_           
       
        """

        ,

                     """        
               --------         
              |        |        
              |        o        
              |       /|\       
              |        |        
              |              
             _|_                
                                
    """
        ,
                     """
               --------                
              |        |    
              |        o    
              |       /|\  
              |        |      
              |       / \    
             _|_            
                          
    """
                     ]
    fin = open('words.txt')
    file2 = open('spanishwords.txt')
    file3 = open('shqipwords.txt')

    words = [line.strip().lower() for line in fin.readlines()]
    swords = [line.strip().lower() for line in file2.readlines()]
    shwords = [line.strip().lower() for line in file3.readlines()]

    while True:
        s = input("Please choose the language of the game(English , Spanish or Shqip): ").lower()
        if s == "English".lower():
            word = random.choice(words)
        elif s == "Spanish".lower():
            word = random.choice(swords)
        elif s== "Shqip".lower():
            word = random.choice(shwords)
        else:
            print("Wrong input , please type the available languages shown below:  ")
            continue

        #diff = input("Please choose the difficulty of the game (Easy , Medium or Hard): ").lower()
        #if diff == "easy":




        print(word)
        user_score = 0
        length = len(word)

        print(f"Guess the word with {length} letters!")

        word_list = []
        for i in range(length):
            word_list.append('_')

        print(*word_list)

        while True:
            letter = input("Guess a letter: ").lower()
            if letter != "exit".lower():
                if letter.isalpha():
                    if letter not in guess_list:
                        guess_list.append(letter)
                    else:
                        print("You already guessed that letter")
                        continue

                    if letter not in word:
                        wrong_guess -= 1
                        user_score -= 1
                        print("invalid letter " + str(wrong_guess) + " tries left")
                        print(guess_figures[index])
                        index += 1
                        if index >= 5:
                            print("You failed")
                            print("You got a score of: " + str(user_score))
                            print("----------------------------")


                            d = input(
                                "Press 'Enter' if you want to play again or 'exit' if you want to quit the game: ")

                            if d == "exit".lower():
                                print("The program is exiting...")
                                exit()
                            elif d == "":
                                main()
                    if letter in word:
                        user_score += 10
                    for i in range(length):
                        if letter == word[i]:
                            word_list[i] = letter

                    print(*word_list)
                else:
                    print("Invalid input please type a letter")
                    continue

                if '_' not in word_list:
                    print("You won!")
                    print("You got a score of: " + str(user_score))
                    z = input("Press 'Enter' if you want to play again or 'exit' if you want to quit the game: ")

                    if z == "exit".lower():
                        print("The program is exiting...")
                        exit()
                    elif z == "":
                        main()
            else:
                print("The game is exiting...")
                print("You got a score of: " + str(user_score))

                exit()


main()
