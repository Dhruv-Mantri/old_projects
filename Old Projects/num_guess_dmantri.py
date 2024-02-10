import random
import time

#ranges
min = 1
max = 1000

# keep track of high scores, for two files, tries and times
def records(new_score, mode):
    if mode == 1:
        my_file = "time_records.txt"
        description = "seconds"
    elif mode == 2:
        my_file = "try_records.txt"
        description = "tries"
    # get old high score
    with open(my_file ,"r") as f:
        old_score = float(f.readline().split(" ")[2])
    f.close()

    # do this if a new high score is made
    if old_score > new_score:
        with open(my_file, "w") as f:
            highscore = f"High Score: {new_score} {description}"
            f.write(highscore)
        f.close()
        return True

# guessing algorithm for computer guesses
def guessing(min, max):
    guess = int((max+min)/2)
    print("My guess was:", str(guess))
    decision = input("Was this \n[1] Too Low\n[2] Equal\n[3] Too High           ")
    return decision, guess


mode = input("Choose a mode to play:\n[1] Computer Guesses\n[2] You Guess      ")

while mode not in ["1","2"]:
    mode = input("Choose a mode to play:\n[1] Computer Guesses\n[2] You Guess      ")

# first game mode where computer guesses your number
if mode == "1":
    start_time = time.time() # start the timer

    # user input and how that changes the range
    for i in range(10): # runs 10 times for 10 guesses
        choice, my_guess = guessing(min, max)

        while choice not in ['1','2','3']:
            choice = input("Was this \n[1] Too Low\n[2] Equal\n[3] Too High         ")
        if choice == '1':
            min = my_guess
        elif choice == '2':
            end_time = time.time()
            total_time = round(end_time - start_time, 2)
            # Victory Statement
            print(f"Aha! I got it in {str(i+1)} tries and {total_time} seconds! Your number is {my_guess}.")
            new_record_bool = records(total_time, 1)
            if new_record_bool:
                print(f"The computer got a highscore of {total_time} seconds!")
            quit()
        elif choice == '3':
            max = my_guess

# second game mode where you guess computer's number
elif mode == "2":
    number = random.randint(0,1000)

    guessed = False
    tries = 0

    while guessed == False:
        user_guess = int(input("Enter a guess: "))
        tries += 1
        if user_guess == number:
            break
        elif user_guess > number:
            print("Your guess was too large!")
        elif user_guess < number:
            print("Your guess was too small")

    print(f"You win! You took {tries} tries!")
    new_record_bool = records(tries, 2)
    if new_record_bool:
        print(f"You got a new highscore of {tries} guesses!")
