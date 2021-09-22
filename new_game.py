# importing both the random and num_game module
import random
import num_game

# creates a list of values the user will choose from
player_choice = ["rock", "paper", "scissors"]


def choice_game():
    while True:
        try:
            # asking user to input their selection in player_choice
            user_type = input(str("\nPick a selection from the menu: " + str(player_choice)))

            # defines a conditional event for the rock, paper, scissors battle
            game_selection = random.choice(player_choice)
            if user_type == game_selection:
                print(f"{user_type} and {game_selection} are the same. It's a tie")
                return choice_game()
            elif user_type == "rock":
                if game_selection == "scissors":
                    print(f"Rock beats {game_selection}! You win!")
                else:
                    print(f"{game_selection} wins, you lose.")
            elif user_type == "paper":
                if game_selection == "rock":
                    print("paper covers rock. You Win!")
                else:
                    print(f"{game_selection} beats paper. You lose")
            if user_type == "scissors":
                if game_selection == "paper":
                    print("scissors cuts paper. You Win!")
                else:
                    print(f"{game_selection} beats scissors. You lose")
            elif user_type not in player_choice:
                print("Not the choice that was expected")

            # asking the player if they wish to continue, if not, the game aborts
                play_again = input("\nDo you want to play again? (y/n): ")
                if play_again == "y":
                    return choice_game()
                elif play_again == "n":
                    print('\nGoodbye :)')
                    break
                if play_again != "y" or "n":
                    print("\nThat is an invalid input")
                    break
        except Exception as e:
            print("That is an invalid input",  e)


# displays the choice_game function
choice_game()

