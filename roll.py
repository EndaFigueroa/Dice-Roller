import random

def dice_roller(tries,sides):
    for	i in range(tries):
        random_int = random.randint(1, sides)
        print(random_int)

print('one roll')
dice_roller(1,6)
print('two rolls')
dice_roller(2,20)
print('three rolls')
dice_roller(3,10)
#roll a "die" some number of times.
#roll - run it once and go into a loop
#roll 1 - produce a number 1-6 random and print it
#roll 2 - produce two numbers 1-6 and print them
#roll 3 - produce three numbers and print them.
#
