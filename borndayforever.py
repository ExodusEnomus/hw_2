year = 0
day = 0

while year != 1799:
    year = int(input('Enter Pushkin year of birth?'))

    if year == 1799:
        while day != 26:
            day = int(input('Enter Pushkin day of birth?'))

            if day == 26:
                print('Right answer!')
            else:
                print('Wrong day!!!')
    else:
        print('Wrong year !!!')