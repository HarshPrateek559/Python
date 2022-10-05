import random

maxn = 100
tries = 8
n = random.randint(1, maxn)
print('Welcome to guess the number game!')
print('Guess the number from 1 to %d in %d tries' %( maxn,tries))
guess = None
while guess != n and tries!=0:
    tries-=1
    guess = int(input('Your try: '))
    if guess > n:
        print('Too high, Chances remaining:',tries)
    if guess < n:
        print('Too low, Chances remaining:', tries)

if tries!=0:
	print('Congratulations, you won!')
else:
	print("Sorry but you have ran out of tries")
