print('Welcome to my quiz!')

playing = input('Would you like to play a game? ')

if playing.lower() != 'yes':
    quit()

print('Okay, let us begin. Below you will be asked questions, the answers must be one word or number.')
score = 0

answer = input("How many states are in New England? ")
if answer == '6':
    print('You are correct!')
    score += 1
else:
    print("Incorrect")

answer = input("How many stomachs do cows have? ")
if answer == '4':
    print('You are correct!')
    score += 1
else:
    print("Incorrect")

answer = input("Who is the fastest man alive? ")
if answer.lower() == 'usain bolt':
    print('You are correct!')
    score += 1
else:
    print("Incorrect")

answer = input("What has four legs in the morning, two in the afternoon and three in the evening? ")
if answer.lower() == 'humans':
    print('You are correct!')
    score += 3
else:
    print("Incorrect")

answer = input("Who was the first president of the United States of America? ")
if answer.lower() == 'george washington':
    print('You are correct!')
    score += 1
else:
    print("Incorrect")

answer = input("What is the most prominent self cultivation art in China? ")
if answer.lower() == 'qigong':
    print('You are correct!')
    score += 2
else:
    print("Incorrect")

print(f'You got {score} correct this time around.')
print(f'You scored {score/9 *100}%')

