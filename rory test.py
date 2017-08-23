import random

# import random for random.randint(number, to number) below
number = random.randint(1, 4)
name = input('what is your name: ')
name = name.capitalize()
if name == 'Rory' and number == 1:
    print('go away, ' + name)
if name == 'Rory' and number == 2:
    print(name + ", you sound like you're from london")
if name == 'Rory' and number == 3:
    print(name + ", UK isn't so bad")
if name == 'Rory' and number == 4:
    print(name + ", is Big Head from Silicon Valley")
else:
    print(name + ', I am getting better at this')
