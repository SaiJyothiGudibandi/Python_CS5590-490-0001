import random

nums = range(1,100,1)
rand = random.choice(nums) #Randomly select number between 1 to 100
random =int(rand) #converting string to integer
guess=int(input('Guess the random number:')) #Taking input from the user

if (random>guess): #if condition to check which num is greater
    print('Guessed number is greater than required')
elif (random<guess):
    print('Guessed number is lower than required')
else:
    print('Your guess is correct, Congratulations:-)')

print('System guessed number is:',random) #Printing the system random pic number

