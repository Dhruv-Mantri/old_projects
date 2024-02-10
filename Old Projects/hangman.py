# from random_words import RandomWords
import os
import time
import random

def drawing(stickman_pieces):
    stickman = ["""
    |--------
    |       |
    |
    |
    |
    |
    |________
    ""","""
    |--------
    |       |
    |       O
    |
    |
    |
    |________
    ""","""
    |--------
    |       |
    |       O
    |       |
    |
    |
    |________
    ""","""
    |--------
    |       |
    |       O
    |       |/
    |
    |
    |________
    ""","""
    |--------
    |       |
    |       O
    |      \|/
    |
    |
    |________
    ""","""
    |--------
    |       |
    |       O
    |      \|/
    |       |
    |
    |________
    ""","""
    |--------
    |       |
    |       O
    |      \|/
    |       |
    |      /
    |________
    ""","""
    |--------
    |       |
    |       O
    |      \|/
    |       |
    |      / \\
    |________
    """]
    # 8 indexes
    if stickman_pieces > 6:
        stickman_pieces = 7
    return stickman[stickman_pieces]

def time_display(sec):
  mins = sec // 60
  sec = sec % 60
  hours = mins // 60
  mins = mins % 60
  time = "You took {0} hours, {1} minutes, {2} seconds".format(int(hours),int(mins),int(sec))
  return time

def classic_hangman(progress):
    print("This is level", progress)
    word = RandomWords()
    if int(progress) <= 3:
        while len(word) < 10:
            word = RandomWords()
    if int(progress) <= 7 and int(progress) > 3:
        while len(word) > 8:
            word = RandomWords()
    if int(progress) <= 10 and int(progress) > 7:
        while len(word) > 6:
            word = RandomWords()
    if int(progress) > 11:
        return 1001
    word_list = list(word.lower())
    for i,m in enumerate(word_list):
        if word_list[i] == " ":
            word_list[i] = ""
        if word_list[i] == '-':
            print("there's a hyphen in this word")
    blank_word = []
    missed_letters = []
    for char in word:
        blank_word.append("_ ")
    print(" ".join(blank_word))
    tries = 0
    while "_ " in blank_word:
        letter_or_word = input("Enter a letter or type an entire word:   ").lower()
        tries += 1

        if len(letter_or_word) == 1:
            if letter_or_word not in word_list:
                missed_letters.append(letter_or_word)
            else:
                for i,m in enumerate(word_list):
                    if letter_or_word in m:
                        blank_word[i] = letter_or_word
            print("Missed Letters: ", end="")
            print(" ".join(missed_letters))
            print(" ".join(blank_word))
        elif len(letter_or_word) > 1:
            if letter_or_word == word:
                letter_percent = 100/len(word_list)
                missed_points = int(len(missed_letters)*letter_percent)
                final_points = 100-missed_points
                return final_points
        if letter_or_word == "i give up":
            print(word)
            print("You lose.")
            return 0
        if "_ " not in blank_word:
            final_word = "".join(blank_word)
            if final_word == word:
                letter_percent = 100/len(word_list)
                missed_points = int(len(missed_letters)*letter_percent)
                final_points = 100-missed_points
                return final_points

rand_word_list = []
with open("words.txt","r") as f:
    rand_word_list = f.readlines()
def RandomWords():
    for i in rand_word_list:
        i.strip()
    return rand_word_list[random.randint(0,len(rand_word_list)-1)].strip()

hangman_options = ['0','1','2','3','4','5','6','7','8','9']

repeat = True
while repeat:
    print("Type 0 to quit")
    rand_word = RandomWords()
    rand_word_two = RandomWords()
    if rand_word == rand_word_two:
        rand_word = RandomWords()
        rand_word_two = RandomWords()
    while len(rand_word) == 3:
        rand_word = RandomWords()
    while len(rand_word) != len(rand_word_two):
        rand_word_two = RandomWords()

    print("[1] Classic Mode    [2] Party Mode  ")
    print("[3] Multiplayer     [4] Timed")
    print("[5] Spam Check      [6] Leaderboard")
    print("[7] Campaign Mode   [8] Random")
    hangman_mode = input()


    while hangman_mode not in hangman_options:
        print("[1] Classic Mode    [2] Party Mode  ")
        print("[3] Multiplayer     [4] Timed")
        print("[5] Spam Check      [6] Leaderboard")
        print("[7] Campaign Mode   [8] Random")
        hangman_mode = input()

    if hangman_mode == '8':
        hangman_mode = str(random.randint(1,7))

    if hangman_mode == '1':
        difficulty = input("[1] Infinite Tries\n[2] Hangman with the man  ")
        if difficulty == '1':
            
            word = rand_word
            word_list = list(word.lower())
            for i,m in enumerate(word_list):
                if word_list[i] == " ":
                    word_list[i] = ""
                if word_list[i] == '-':
                    print("there's a hyphen in this word")
            blank_word = []
            missed_letters = []
            for char in word:
                blank_word.append("_ ")
            print(" ".join(blank_word))
            tries = 0
            while "_ " in blank_word:
                letter_or_word = input("Enter a letter or type an entire word:   ").lower()
                tries += 1
                
                if len(letter_or_word) == 1:
                    if letter_or_word not in word_list:
                        missed_letters.append(letter_or_word)
                    else:
                        for i,m in enumerate(word_list):
                            if letter_or_word in m:
                                blank_word[i] = letter_or_word
                    print("Missed Letters: ", end="")
                    print(" ".join(missed_letters))
                    print(" ".join(blank_word))
                elif len(letter_or_word) > 1:
                    if letter_or_word == word:
                        print("You WIN!")
                        print("You took",tries,"tries.")
                        possible_points = len(word_list)*5
                        missed_points = len(missed_letters)*5
                        final_points = possible_points-missed_points
                        if final_points == 0:
                            print("You got a perfect score!!")
                        else:
                            print("You got", final_points, "points out of",possible_points)
                        break
                if letter_or_word == "i give up":
                    print(word)
                    print("You lose.")
                    break
                if "_ " not in blank_word:
                    final_word = "".join(blank_word)
                    if final_word == word:
                        print("You WIN!")
                        print("You took", tries, "tries.")
                        possible_points = len(word_list) * 5
                        missed_points = len(missed_letters) * 5
                        final_points = possible_points - missed_points
                        if final_points == possible_points:
                            print("You got a perfect score!!")
                        else:
                            print("You got", final_points, "points out of", possible_points)
                        break
        if difficulty == '2':
            
            wrong_tries = 0
            print(drawing(wrong_tries))
            word = rand_word
            word.lower()
            word_list = list(word)
            for i, m in enumerate(word_list):
                if word_list[i] == " ":
                    word_list[i] = ""
                if word_list[i] == '-':
                    print("there's a hyphen in this word")
            blank_word = []
            missed_letters = []
            for char in word:
                blank_word.append("_ ")
            print(" ".join(blank_word))
            tries = 0
            while "_ " in blank_word:
                letter_or_word = input("Enter a letter or type an entire word:   ").lower()
                tries += 1
                if len(letter_or_word) == 1:
                    if letter_or_word not in word_list:
                        missed_letters.append(letter_or_word)
                        wrong_tries+= 1
                    else:
                        for i, m in enumerate(word_list):
                            if letter_or_word in m:
                                blank_word[i] = letter_or_word
                    print("Missed Letters: ", end="")
                    print(" ".join(missed_letters))
                    print(" ".join(blank_word))
                    print(drawing(wrong_tries))
                elif len(letter_or_word) > 1:
                    if letter_or_word == word:
                        print("You WIN!")
                        print("You took", tries, "tries.")
                        possible_points = len(word_list) * 5
                        missed_points = len(missed_letters) * 5
                        final_points = possible_points - missed_points
                        if final_points == 0:
                            print("You got a perfect score!!")
                        else:
                            print("You got", final_points, "points out of", possible_points)
                        break
                    else:
                        print("Incorrect")
                        wrong_tries += 1
                        print("Missed letters: ", end="")
                        print(" ".join(missed_letters))
                        print(" ".join(blank_word))
                        print(drawing(wrong_tries))
                if letter_or_word == "i give up":
                    print(word)
                    print("You lose.")
                    break
                if wrong_tries > 6:
                    print("You lose.")
                    print("The word was", word)
                    break
                if "_ " not in blank_word:
                    final_word = "".join(blank_word)
                    if final_word == word:
                        print("You WIN!")
                        print("You took", tries, "tries.")
                        possible_points = len(word_list) * 5
                        missed_points = len(missed_letters) * 5
                        final_points = possible_points - missed_points
                        if int(final_points) == int(possible_points):
                            print("You got a perfect score!!")
                        else:
                            print("You got", final_points, "points out of", possible_points)
                        break

    elif hangman_mode == '2':
        word = input("Enter a word:  ")
        word_list = list(word.lower())
        for i, m in enumerate(word_list):
            if word_list[i] == " ":
                word_list[i] = ""
            if word_list[i] == '-':
                print("there's a hyphen in this word")
        blank_word = []
        missed_letters = []
        for char in word:
            blank_word.append("_ ")
        print(" ".join(blank_word))
        tries = 0
        while "_ " in blank_word:
            letter_or_word = input("Enter a letter or type an entire word:   ").lower()
            tries += 1
            if len(letter_or_word) == 1:
                if letter_or_word not in word_list:
                    missed_letters.append(letter_or_word)
                else:
                    for i, m in enumerate(word_list):
                        if letter_or_word in m:
                            blank_word[i] = letter_or_word
                print("Missed Letters: ", end="")
                print(" ".join(missed_letters))
                print(" ".join(blank_word))
            elif len(letter_or_word) > 1:
                if letter_or_word == word.lower():
                    print("You WIN!")
                    print("You took", tries, "tries.")
                    possible_points = len(word_list) * 5
                    missed_points = len(missed_letters) * 5
                    final_points = possible_points - missed_points
                    if final_points == 0:
                        print("You got a perfect score!!")
                    else:
                        print("You got", final_points, "points out of", possible_points)
                    break
                else:
                    print("Incorrect")
            if letter_or_word == "i give up":
                print(word)
                print("You lose.")
                break
            if "_ " not in blank_word:
                final_word = "".join(blank_word)
                if final_word == word:
                    print("You WIN!")
                    print("You took", tries, "tries.")
                    possible_points = len(word_list) * 5
                    missed_points = len(missed_letters) * 5
                    final_points = possible_points - missed_points
                    if int(final_points) == int(possible_points):
                        print("You got a perfect score!!")
                    else:
                        print("You got", final_points, "points out of", possible_points)
                    break

    elif hangman_mode == '3':
        player_one = rand_word
        player_two = rand_word_two
        player_one_list = list(player_one)
        player_two_list = list(player_two)
        blank_word_one = []
        blank_word_two = []
        missed_letters_one = []
        missed_letters_two = []
        for char in player_one:
            blank_word_one.append("_ ")
        for char in player_two:
            blank_word_two.append("_ ")
        print("".join(blank_word_one),end="          ")
        print("".join(blank_word_two))
        p1 = True
        p2 = False
        game_over = False
        while game_over != True:
            while p1:
                word_guess = input("Player 1: Enter your guess:  ")
                word_guess.lower()
                word_guess.strip()
                if "_ " not in blank_word_one:
                    print("Player 1 WINS")
                    game_over = True
                    break
                if len(word_guess) == 1:
                    if word_guess not in player_one_list:
                        missed_letters_one.append(word_guess)
                    else:
                        for i,m in enumerate(player_one_list):
                            if word_guess in m:
                                blank_word_one[i] = word_guess
                    print("Missed Letters: [P1] ", end="")
                    print(" ".join(missed_letters_one),end="        [P2] ")
                    print(" ".join(missed_letters_two))
                    print(" ".join(blank_word_one), end="          ")
                    print("".join(blank_word_two))
                else:
                    if word_guess == player_one:
                        print("Player 1 WINS")
                        game_over = True
                        break
                    else:
                        print("Incorrect")
                    print("Missed Letters: [P1] ", end="")
                    print(" ".join(missed_letters_one),end="        [P2] ")
                    print(" ".join(missed_letters_two))
                    print(" ".join(blank_word_one), end="          ")
                    print("".join(blank_word_two))
                p1 = False
                p2 = True
            while p2:
                word_guess = input("Player 2: Enter your guess:  ")
                word_guess.lower()
                word_guess.strip()
                if "_ " not in blank_word_two:
                    print("Player 2 WINS")
                    game_over = True
                    break
                if len(word_guess) == 1:
                    if word_guess not in player_two_list:
                        missed_letters_two.append(word_guess)
                    else:
                        for i,m in enumerate(player_two_list):
                            if word_guess in m:
                                blank_word_two[i] = word_guess
                    print("Missed Letters: [P1] ", end="")
                    print(" ".join(missed_letters_one),end="        [P2] ")
                    print(" ".join(missed_letters_two))
                    print(" ".join(blank_word_one), end="          ")
                    print("".join(blank_word_two))
                else:
                    if word_guess == player_two:
                        print("Player 2 WINS")
                        game_over = True
                        break
                    else:
                        print("Incorrect")
                    print("Missed Letters: [P1] ", end="")
                    print(" ".join(missed_letters_one),end="        [P2] ")
                    print(" ".join(missed_letters_two))
                    print(" ".join(blank_word_one), end="          ")
                    print("".join(blank_word_two))
                p2 = False
                p1 = True

    elif hangman_mode == '4':
        word = rand_word
        word.lower()
        word_list = list(word)
        # for i, m in enumerate(word_list):
        #     if word_list[i] == " ":
        #         word_list[i] = ""
        #     if word_list[i] == '-':
        #         print("there's a hyphen in this word")
        blank_word = []
        missed_letters = []
        for char in word:
            blank_word.append("_ ")
        print(" ".join(blank_word))
        tries = 0
        expected_time = 5*len(word_list) #5 seconds per letter
        start_time = time.time()
        while "_ " in blank_word:
            letter_or_word = input("Enter a letter or type an entire word:   ").lower()
            tries += 1
            if len(letter_or_word) == 1:
                if letter_or_word not in word_list:
                    missed_letters.append(letter_or_word)
                else:
                    for i, m in enumerate(word_list):
                        if letter_or_word in m:
                            blank_word[i] = letter_or_word
                print("Missed Letters: ", end="")
                print(" ".join(missed_letters))
                print(" ".join(blank_word))
            elif len(letter_or_word) > 1:
                if letter_or_word == word:
                    print("You did it!")
                    end_time = time.time()
                    total_time = end_time - start_time
                    formatted_time = time_display(total_time)
                    print(formatted_time)
                    print(expected_time, "was your expected time")
                    break
                else:
                    print("Incorrect")
            if letter_or_word == "i give up":
                print(word)
                end_time = time.time()
                print("You lose.")
                break
            if "_ " not in blank_word:
                final_word = "".join(blank_word)
                if final_word == word:
                    print("You did it!")
                    end_time = time.time()
                    total_time = end_time - start_time
                    formatted_time = time_display(total_time)
                    print(formatted_time)
                    print(expected_time, "seconds was your expected time")
                    break

   
    elif hangman_mode == '5':
        spam = False
        skip = False
        print("Press enter to continue dialogue.")
        contin = input("We all know you can't play this game.")
        contin = input("Whenever you see empty spots, you just spam letters.")
        contin = input("What's that? You think you don't spam?")
        contin = input("Prove it in this Spam Check.")
        letter_speed = []
        word = rand_word
        word_list = list(word.lower())
        blank_word = []
        missed_letters = []
        for char in word:
            blank_word.append("_ ")
        print(" ".join(blank_word))
        
        while "_ " in blank_word:
            start_time = time.time()
            letter_or_word = input("Enter a letter or type an entire word:   ").lower()
            end_time = time.time()
            total_time = end_time - start_time
            letter_speed.append(total_time)
            if len(letter_or_word) == 1:
                if letter_or_word not in word_list:
                    missed_letters.append(letter_or_word)
                else:
                    for i,m in enumerate(word_list):
                        if letter_or_word in m:
                            blank_word[i] = letter_or_word
                print("Missed Letters: ", end="")
                print(" ".join(missed_letters))
                print(" ".join(blank_word))
            elif len(letter_or_word) > 1:
                if letter_or_word == word:
                    print("Calibration Complete.")
                    break
            if letter_or_word == "i give up":
                print(word)
                print("You lose.")
                print("You're not a spammer, you're just bad at the game")
                skip = True
                break
            if "_ " not in blank_word:
                final_word = "".join(blank_word)
                if final_word == word:
                    print("Calibration Complete")
                    break
        if skip == False:
            spam_letters = 0
            for i in letter_speed:
                if i < 0.95:
                    spam_letters += 1
            if spam_letters > 2:
                spam = True
            if spam:
                print("Our data shows that you actually spammed.")
                print(spam_letters, "times!")
                print("That's",spam_letters,"more times than it should be.")
                print("I am ashamed of you.")
            else:
                print("Conglatulations!")
                print("You are spam-free.")

    elif hangman_mode == '6':
        print("You will be timed and scored.")
        word = rand_word
        while len(word) < 8:
            word = RandomWords()
        word.lower()
        word_list = list(word)
        blank_word = []
        missed_letters = []
        for char in word:
            blank_word.append("_ ")
        print(" ".join(blank_word))
        start_time = time.time()
        while "_ " in blank_word:
            letter_or_word = input("Enter a letter or type an entire word:   ").lower()
            if len(letter_or_word) == 1:
                if letter_or_word not in word_list:
                    missed_letters.append(letter_or_word)
                else:
                    for i, m in enumerate(word_list):
                        if letter_or_word in m:
                            blank_word[i] = letter_or_word
                print("Missed Letters: ", end="")
                print(" ".join(missed_letters))
                print(" ".join(blank_word))
            elif len(letter_or_word) > 1:
                if letter_or_word == word:
                    end_time = time.time()
                    print("You did it!")
                    percent_letter = int(100/len(word))
                    final_percent = 100
                    for i in missed_letters:
                        final_percent -= percent_letter
                    print("You got", str(final_percent)+"%")
                    total_time = end_time - start_time
                    time_display(total_time)
                    update = False
                    with open("leaderboard.txt","r") as f:
                        read = f.readlines()
                        line = read[0].split(" ")
                        line_two = read[1].split(" ")
                        if final_percent > int(line[2]):
                            print("You got the high score!!")
                            update = True
                        elif final_percent == int(line[2]):
                            if int(total_time) < int(line_two[1]):
                                print("You got a high score!")
                                update = True
                        f.close()
                    if update == True:
                        update_name = input("What do you want people to remember you by?  ")
                        with open("leaderboard.txt","w") as f:
                            replacement = "Top Score: ",str(final_percent)," %\n"+"Time: ",str(int(total_time))," seconds\n"+update_name
                            f.writelines(replacement)
                            f.close()
                        update = False
                    break
                else:
                    print("Incorrect")
            if letter_or_word == "i give up":
                print(word)
                print("You lose.")
                break
            if "_ " not in blank_word:
                final_word = "".join(blank_word)
                if final_word == word:
                    end_time = time.time()
                    print("You did it!")
                    percent_letter = int(100/len(word))
                    final_percent = 100
                    for i in missed_letters:
                        final_percent -= percent_letter
                    print("You got", str(final_percent)+"%")
                    total_time = end_time - start_time
                    time_display(total_time)
                    update = False
                    with open("leaderboard.txt","r") as f:
                        read = f.readlines()
                        line = read[0].split(" ")
                        if final_percent > int(line[2]):
                            print("You got the high score!!")
                            update = True
                        elif final_percent == int(line[2]):
                            pass
                        f.close()
                    if update == True:
                        update_name = input("What do you want people to remember you by?  ")
                        with open("leaderboard.txt","w") as f:
                            replacement = "Top Score: ",str(final_percent)," %\n"+"Time: ",str(int(total_time))," seconds\n"+update_name
                            f.writelines(replacement)
                            f.close()
                        update = False
                    break
        print("Type '9' to check leaderboard standings")    

    elif hangman_mode == '7':
        print("Welcome to Campaign Mode!")
        name = input("Enter your account name:  ")
        newUser = False
        beatGame = False
        file_name = name+".txt"
        level = []
        try:
            with open(file_name, "r") as f:
                level = f.readlines()
        except FileNotFoundError:
            with open(file_name,"w"):
                newUser = True
        if newUser:
            with open(file_name,"w") as f:
                f.write("1")
                level.append('1')
        else:
            if int(level[0]) > 10:
                print("Congratulations, you beat the campaign mode!")
                beatGame = True
        f.close()

        if not beatGame:
            score = classic_hangman(level[0])
            if score >= 70:
                print("You passed! You can now move on to level", str(int(level[0])+1))
                with open(file_name,"w") as f:
                    f.write(str(int(level[0])+1))
            else:
                print("You got less than a 70%, try the level again.")

    elif hangman_mode == '9':
        with open("leaderboard.txt","r") as f:
            read = f.readlines()
            f.close()
        line_one = "".join(read[0])
        print(str(line_one) + read[1] + read[2])
        contin = input("Press Enter to continue")

    elif hangman_mode == '0':
        repeat = False

print("Thanks for playing!")