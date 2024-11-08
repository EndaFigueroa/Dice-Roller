import random

def dice_roller(tries):
    for	i in range(tries):
        random_int = random.randint(1, 6)
        print(random_int)

print('one roll')
dice_roller(1)
print('two rolls')
dice_roller(2)
print('three rolls')
dice_roller(3)
#roll a "die" some number of times.
#roll - run it once and go into a loop
#roll 1 - produce a number 1-6 random and print it
#roll 2 - produce two numbers 1-6 and print them
#roll 3 - produce three numbers and print them.
#
