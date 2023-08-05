import random

top_of_range = input("Type a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    if top_of_range <= 0:
        print('Number must be between 1-10')
        quit()
    elif top_of_range > 10:
        print('Number must be between 1-10')
        quit()
else:
    print('Please make sure you input a number')



random_number = random.randint(0, top_of_range)
guesses = 0
while True:
    guesses += 1
    user_guess = input('Make a guess: ')
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print('Please type a number next time.')
        continue

    if user_guess == random_number:
        print('You got it! Nice job!')
        break
    elif user_guess > random_number:
        print('you guessed too high')
    else:
        print('you guessed too low')

print('It took you', guesses, 'guesses')
