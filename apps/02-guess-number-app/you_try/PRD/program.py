import random

print('---------------------------------')
print('    GUESS THAT NUMBER GAME    ')
print('---------------------------------')
print()

name = input('What is your name? ')
the_number = random.randint(0, 100)
guess_int = -1

while guess_int != the_number:
    guess_text = input('Guess a number between 0 and 100: ')
    guess_int = int(guess_text)

    if guess_int < the_number:
        print('Sorry {1}, your guess of {0} is too LOW.'.format(guess_int, name))
    elif guess_int > the_number:
        print('Sorry {1}, your guess of {0} is too HIGH.'.format(guess_int, name))
    else:
        print('Excellent work {1}, you guessed {0} correctly.'.format(guess_int, name))

print('DONE!')
