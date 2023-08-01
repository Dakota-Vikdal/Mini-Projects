import random

user_wins = 0
computer_wins = 0

options = ['rock', 'paper', 'scissors']

while True:
    user_input = input('Please enter either rock, paper, or scissors or Q to quit: ').lower()
    if user_input == 'q':
        break

    if user_input not in options:
        continue

    random_number = random.randint(0, 2)
    #0 = rock      #1 = paper       #2 = scissors

    computer_pick = options[random_number]
    print("Computer picked", computer_pick + '.')

    if user_input == "rock" and computer_pick == "scissors":
        print('You won that one!')
        user_wins += 1
        
    elif user_input == "paper" and computer_pick == "rock":
        print('You won that one!')
        user_wins += 1
        
    elif user_input == "scissors" and computer_pick == "paper":
        print('You won that one!')
        user_wins += 1

    else:
        print('Shoot, maybe next time.')
        computer_wins += 1
        


    if computer_pick == "rock" and user_input == "scissors":
        print('Oh shoot, maybe next time!')
        computer_wins += 1
        continue
    if computer_pick == "paper" and user_input == "rock":
        print('Oh shoot, maybe next time!')
        computer_wins += 1
        continue
    if computer_pick == "scissors" and user_input == "paper":
        print('Oh shoot, maybe next time!')
        computer_wins += 1
        continue
    
print(f'You won {user_wins} times.')
print('The computer scored', {computer_wins}, 'times.')

print('Goodbye!')
