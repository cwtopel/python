import sys

def moonweight():
    print('How much do you weigh?')
    weight = int(sys.stdin.readline())
    
    print('How long are you staying?')
    years = int(sys.stdin.readline())
    
    print('How much do you plan to gain per year?')
    addlbs = int(float(sys.stdin.readline()))
    
    for x in range(1, years):
        print('Year %s you would weigh %slbs.' % (x, (weight * 0.25)))
        weight = weight + addlbs
        
moonweight()
## print(moonweight()) returns None -- just call the function directly here

