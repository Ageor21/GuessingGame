# Defines a list of values for the variables num_sum
num_sum = [10, 20, 30, 40]
final_num = 10

# Creates a conditional number guessing game
def guess_num_game():
    while True:
        try:
            result = int(input("Chose a number from 1 - 20: "))
            if result == 20:
                print("\nYou guessed correctly!")
                break
            elif result > 20:
                print("\nThat is greater than the value expected. Try again")
            elif result < 20:
                print("\nYou guessed wrong! Try again")
        except:
            print("\ninvalid value, expected a number!")


guess_num_game()

# If user passes game 1 they proceed to game 2. Multiple chances are given to the user if guess is wrong
def guess_num_game_2():
    while True:
        try:
            result_2 = int(input("\n(Round 2) What number am I thinking of? from 1 - 40: "))
            if result_2 in [10, 20, 30, 40]:
                print("You knew! You win this round, congrats!")
                break
            elif result_2 not in [10, 20, 30, 40]:
                print("You failed the game, Thank you for playing")
                return guess_num_game_2()
        except:
            print("\ninvalid value, expected a number!")


guess_num_game_2()

# If the player guesses the right equation the player moves on to the next game
def final_num_game():
    while True:
        try:
            result_3 = int(input("\n(Final round) what is the equation of (100/20) + (3+2): "))
            if result_3 == final_num:
                print("Congratulations, you won the game! Pat yourself on the back :)")
                break
            elif result_3 != final_num:
                print("\nYou were incorrect. I'm sorry, you lose")
                return final_num_game()
        except:
            print("\nInvalid value, expected a number!")
            pass
final_num_game()


