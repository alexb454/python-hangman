import random
import time

# Start of game to put user aka your name
print("\nWelcome to Alex's make of classic Hangman, with Python\n")
user = input("Enter your name or make one: ")
print("Good morning, evening and afternoon " + user + "! Hope you enjoy!")
time.sleep(4)
print("Game starts in 5!\n Lets Play!!!")
time.sleep(5)

# To start and run the game
def main() :
    global count
    global display
    global word
    global already_tried
    global length
    global play_me
    my_words = ["pokemon", "lake", "roosterteeth", "wrecking", "honorificabilitudinitatibus", "deadpool", "birthday", "clubhouse", "nintendo"]
    word = random.choice(my_words)
    length = len(word)
    count = 0
    display = '_' * length
    already_tried = []
    play_me = ""

# A loop so as to start the game again
def loop_main() : 
    global play_me
    play_me = input("Would you like to play again? y = yes, n = no \n")
    while play_me not in ["y", "n"]:
        play_me = input("Would you like to play again? y = yes, n = no \n")
    if play_me == "y" :
        main()
    elif play_me == "n" :
        print("Thanks For Playing! Hope you enjoyed it!")
        exit()

# Setting up all conditions for this game
def hang_the_man() :
    global count
    global display
    global word
    global already_tried
    global play_me
    limit = 5
    guess = input("This is the Hangmans Word: " + display + " \nEnter your guess please or this poor soul is doomed: \n")
    guess = guess.strip()
    if len(guess.strip()) == 0 or len(guess.strip()) >= 2 or guess <= "9":
        print("Invalid Input, Try a letter\n")
        hang_the_man()

    elif guess in word:
        already_tried.extend([guess])
        index = word.find(guess)
        word = word[:index] + "_" + word[index + 1:]
        display = display[:index] + guess + display[index + 1:]
        print(display + "\n")

    elif guess in already_tried:
        print("Try another letter.\n")
    
    else:
        count += 1
        if count == 1:
            time.sleep(2)
            print("   _____ \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess 1. " + str(limit - count) + " guesses remaining\n")

        elif count == 2:
            time.sleep(2)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess 2. " + str(limit - count) + " guesses remaining\n")

        elif count == 3:
           time.sleep(1)
           print("   _____ \n"
                 "  |     | \n"
                 "  |     |\n"
                 "  |     | \n"
                 "  |      \n"
                 "  |      \n"
                 "  |      \n"
                 "__|__\n")
           print("Wrong guess 3. " + str(limit - count) + " guesses remaining\n")

        elif count == 4:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess 4. " + str(limit - count) + " last guess remaining, this guys toast\n")

        elif count == 5:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |    /|\ \n"
                  "  |    / \ \n"
                  "__|__\n")
            print("Wrong guess. You are hanged! The sadness!!\n")
            print("The word was: ",already_tried,word)
            loop_main()

    if word == '_' * length:
        print("Congrats! You won and got the word! Dope!")
        loop_main()

    elif count != limit:
        hang_the_man()


main()


hang_the_man()