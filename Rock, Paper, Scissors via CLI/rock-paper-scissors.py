import random

print('\nLet\'s play a game :)')

win = 0
loss = 0

while True:
    possible_moves = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(possible_moves)
    user_move = input('\nrock, paper, scissors or quit? ').lower()

    if user_move == computer_choice:
        print(f'You both picked {user_move}. It\'s a tie!')
    elif user_move == 'rock':
        if computer_choice == 'paper':
            print(f'You picked {user_move}. Computer picked {computer_choice}. LOSER!')
            loss += 1
        else:
            print(f'You picked {user_move}. Computer picked {computer_choice}. WINNER!')
            win += 1
    elif user_move == 'paper':
        if computer_choice == 'scissors':
            print(f'You picked {user_move}. Computer picked {computer_choice}. LOSER!')
            loss += 1
        else:
            print(f'You picked {user_move}. Computer picked {computer_choice}. WINNER!')
            win += 1
    elif user_move == 'scissors':
        if computer_choice == 'rock':
            print(f'You picked {user_move}. Computer picked {computer_choice}. LOSER!')
            loss += 1
        else:
            print(f'You picked {user_move}. Computer picked {computer_choice}. WINNER!')
            win += 1
    elif user_move == 'quit':
        print(f'\nW/L:\n{win}/{loss}\n')
        break
    else:
        print('Input error, try again.')