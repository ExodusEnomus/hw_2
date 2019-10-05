year = int(input('Enter Pushkin year of birth?'))

if year == 1799:
    day = int(input('Enter Pushkin born day'))
    if day == 26:
        print('Right answer!!!')
    else:
        print('Wrong day!')
else:
    print('Wrong year!!!')