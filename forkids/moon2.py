def moon_weight(years, modifier):
    weight = 200
    for years in range(1,16):
        weight = weight + 1
        print('Year %s = %slbs' % (years, (weight*modifier)))

moon_weight(15, 0.25)