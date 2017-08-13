import random

print('---------------------------------------------')
print('                 HELLO WORLD')
print('---------------------------------------------')
print()

#the_number = random.randit()
the_number = random.randint(0,100)
guess = -1 #initial value, start with a known incorrect value


while guess != the_number:
    guess_text = input('Guess a number between 0 and 100: ')
    guess = int(guess_text) #cast to a int

    if guess < the_number:
        print('Sorry, your guess of {0} is too low.'.format(guess))
    elif guess > the_number:
        print('Sorry, your guess of {0} is too high'.format(guess))
    else:
        print('Yes! You win!')

print('Game over. Have a nice day')