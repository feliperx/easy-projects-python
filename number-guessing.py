'''
Number Guessing Game
-------------------------------------------------------------
Jogo para adivinhar um numero inteiro em um determinado range
'''

import random

attempts_list = []
attempts_list.clear()
print(attempts_list)

def show_score():
    if not attempts_list:
        print('There is currently no high score, it\'s yours for the taking!')

    else:
        print(attempts_list)
        print(f'The current high score is {min(attempts_list)} attempts')


def start_game():
    attempts = 0
    rand_num = random.randint(1, 20)
    print('Hello traveler! Welcome to the game of guesses!')
    player_name = input('What is your name? ')
    wanna_play = input(
        f'Hi, {player_name}, would you like to play the guessing game?'
        '(Enter Yes/No): ')

    if wanna_play.lower() != 'yes':
        print('That\'s cool, Thanks!')
        exit()
    else:
        show_score()

    while wanna_play.lower() == 'yes':
        try:
            guess = int(input('Pick a number between 1 and 20: '))
            if guess < 1 or guess > 20:
                raise ValueError(
                    'Please guess a number within the given range')

            attempts += 1

            if guess == rand_num:
                attempts_list.append(attempts)
                print('Nice! You got it!')
                print(f'It took you {attempts} attempts')
                wanna_play = input(
                    'Would you like to play again? (Enter Yes/No): ')
                if wanna_play.lower() != 'yes':
                    print('That\'s cool, have a good one!')
                    break
                else:
                    attempts = 0
                    rand_num = random.randint(1, 20)
                    show_score()
                    continue
            else:
                if guess > rand_num:
                    print('It\'s lower')
                elif guess < rand_num:
                    print('It\'s higher')

        except ValueError as err:
            print('Oh no!, that is not a valid value. Try again...')
            print(err)


if __name__ == '__main__':
    start_game()
