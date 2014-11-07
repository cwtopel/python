age = 26

for x in range(1, 100):
    if x == age: # it's critical that this if statement is first, otherwise the script won't stop until it reaches the end of the range.
        print('Found it! You\'re %s!' % x)
        break
    elif x % 2 == 0:
        print('Are you %s?' % x)
