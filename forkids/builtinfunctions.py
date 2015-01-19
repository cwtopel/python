############################
# abs = absolute value
############################
print(abs(10),'equals',abs(-10))

steps = -3
if abs(steps) > 0:
    print('Character is moving')
# same as this:
# steps = -3
# if steps < 0 or steps > 0:
#   print('Character is moving')

############################
# bool = boolean
# type of data that can have one of two possible values (true/false)
############################
print(bool(0))
#False
print(bool(1))
#True
print(bool(1123.23))
#True
print(bool(-500))
#True

print(bool(None))
#False
print(bool('a'))
#True
print(bool(' '))
#True
print(bool('What do you call a pig doing karate? Pork Chop!'))
#True

my_silly_list = []
print(bool(my_silly_list))
#False
my_silly_list = ['s', 'i', 'l', 'l', 'y']
print(bool(my_silly_list))
#True

year = input('Year of birth: ')
if not bool(year.rstrip()):
    print('You need to enter a value for your year of birth')

############################
#eval = evaluate function
############################
your_calculation = input('Enter a calculation: ')
#eval(your_calculation)

my_small_program = '''print('ham')
print('sandwich')'''
exec(my_small_program)

############################
# FLOAT - real numbers with decimals
############################
your_age = input('Enter your age: ')
age = float(your_age)
if age > 13:
    print('You are %s years too old' % (age - 13))

############################
# int = converts string or number into whole number/integer (drop the decimal)
############################
int(123.456)
int('123')
#int('123.456')
#Traceback (most recent call last):
#   File "<pyshell>", line 1, in <module>
#       int('123.456')
#ValueError: invalid literal for int() with base 10: '123.456'

############################
# len - object length
############################
len('this is a a test string')
#21
creature_list = ['unicorn', 'cyclops', 'fairy', 'elf', 'dragon',
'troll']
print(len(creature_list))
#6
enemies_map = {'Batman' : 'Joker',
'Superman' : 'Lex Luthor',
'Spiderman' : 'Green Goblin'}
print(len(enemies_map))

fruit = ['apple', 'banana', 'clementine', 'dragon fruit']
length = len(fruit)
for x in range(0, length):
    print('the fruit at index %s is %s' % (x, fruit[x]))

############################
# max/min 
############################
numbers = [5, 4, 10, 30, 22]
print(max(numbers))
#30
strings = 's,t,r,i,n,g,S,T,R,I,N,G'
print(max(strings))
#t
print(max(10, 300, 450, 50, 90))
#450
numbers = [5, 4, 10, 30, 22]
print(min(numbers))
#4
guess_this_number = 61
player_guesses = [12, 15, 70, 45]
if max(player_guesses) > guess_this_number:
    print('Boom! You all lose')
else:
    print('You win')

############################
#range
############################
for x in range(0, 5):
    print(x)

print(list(range(0, 5)))
#[0, 1, 2, 3, 4]

count_by_twos = list(range(0, 30, 2))
print(count_by_twos)
#[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28]

count_down_by_twos = list(range(40, 10, -2))
print(count_down_by_twos)
#[40, 38, 36, 34, 32, 30, 28, 26, 24, 22, 20, 18, 16, 14, 12]

############################
# sum
############################
my_list_of_numbers = list(range(0, 500, 50))
print(my_list_of_numbers)
#[0, 50, 100, 150, 200, 250, 300, 350, 400, 450]
print(sum(my_list_of_numbers))
#2250

############################
# FILES
############################
test_file = open('C:\\Users\chris\Desktop\derf.txt')
text = test_file.read()
print(text)

test_file = open('C:\\Users\chris\Desktop\derf.txt', 'w')
test_file.write('this is my test file')
test_file.close()