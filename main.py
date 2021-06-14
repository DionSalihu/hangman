def main():
    import random
    guess_list = []
    index = 0
    wrong_guess = 5
    print("Welcome to Hangman game!")
    print("Type 'exit' if you want to exit the game!")
    print("Each unique letter in the word contains 10 points if you guess it right, if you make a wrong guess"
           + " you get -1 point")

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
    EEW = open('EEW.txt')
    EHW = open('EHW.txt')
    SEW = open('SEW.txt')
    SHD = open('SHD.txt')
    #
    # english_ewords = [line.strip().lower() for line in EEW.readlines()]
    # english_hwords = [line.strip().lower() for line in EHW.readlines()]
    # spanish_hwords = [line.strip().lower() for line in SHD.readlines()]
    # spanish_ewords = [line.strip().lower() for line in SEW.readlines()]

    words_dict = {
        'english-easy': [line.strip().lower() for line in EEW.readlines()],
        'english-hard': [line.strip().lower() for line in EHW.readlines()],
        'spanish-easy': [line.strip().lower() for line in SHD.readlines()],
        'spanish-hard': [line.strip().lower() for line in SEW.readlines()],
    }

    while True:
        def choose_language():
            while True:
                language_choose = input("Please choose the language of the game(English or Spanish): ").lower()
                if language_choose in ['english', 'spanish']:
                    return language_choose
                print("Wrong input , please choose one of the options shown below!")

        def choose_difficulty():
            while True:
                difficulty_choose = input("PLease choose the difficulty of the game(easy or hard): ").lower()
                if difficulty_choose in ['easy', 'hard']:
                    return difficulty_choose
                print("Wrong input , please choose one of the options shown below!")

        language_choose = choose_language()
        difficulty_choose = choose_difficulty()

        word = random.choice(words_dict[f'{language_choose}-{difficulty_choose}'])
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
