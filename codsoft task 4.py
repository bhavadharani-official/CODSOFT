import random
def get_user_choice():
    print("\nChoose one: Rock, Paper, or Scissors")
    choice = input("Your choice: ").lower()
    while choice not in ['rock' , 'paper' , 'scissors']:
        print("Invalid choice! Please choose rock, paper, or scissors.")
        choice = input("Your choice: ").lower()
    return choice

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user, computer):
    if user == computer:
        return "It's a Tie!"
    elif (user == 'rock' and computer == 'scissors') or \
    (user =='scissors' and computer == 'paper') or \
     (user == 'paper' and computer == 'rock'):
        return "You Win!"
    else:
        return "Computer Wins!"
def play_game():
    user_score = 0
    computer_score = 0
    round_num = 1

    while True:
        print(f"\n--- Round {round_num} ---")

        user = get_user_choice()
        computer = get_computer_choice()

        print(f"You chose:{user.capitalize()}")
        print(f"Computer chose:{computer.capitalize()}")
        result = determine_winner(user , computer)
        print("Result:", result)

        if result == "You Win!":
            user_score += 1
        elif result == "Computer Wins!":
            computer_score += 1

        print(f"Score => You:{user_score} | Computer:{computer_score}")
        play_again = input("Do you  want to play another round?(Yes/No): ").lower()
        if play_again != 'Yes':
            print("\nThanks for playing!")
            print(f"Final Score => You:{user_score} | Computer:{computer_score}")
            break
        round_num += 1

play_game()
                              
              
