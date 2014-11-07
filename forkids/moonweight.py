def moonweight():
    print('How much do you weigh?')
    weight = int(sys.stdin.readline())
    for x in range(1, 16):
        print('Year %s you would weigh %slbs.' % (x, (weight * 0.25)))
        weight = weight + 2.5
        
moonweight()
## print(moonweight()) returns None -- just call the function directly here