while True:
    right_answers = 0

    # Esenin year of birth = 1895
    answer_1 = int(input('Enter Esenin year of birth?'))
    # Mayakovsky year of birth = 1893
    answer_2 = int(input('Enter Mayakovsky year of birth?'))
    # Akhmatova year of birth = 1889
    answer_3 = int(input('Enter Akhmatova year of birth?'))
    # Blok year of birth = 1880
    answer_4 = int(input('Enter Blok year of birth?'))
    # Pasternak year of birth = 1890
    answer_5 = int(input('Enter Pasternak year of birth?'))

    if answer_1 == 1895:
        right_answers += 1
    if answer_2 == 1893:
        right_answers += 1
    if answer_3 == 1889:
        right_answers += 1
    if answer_4 == 1880:
        right_answers += 1
    if answer_5 == 1890:
        right_answers += 1

    print('Right answers', right_answers)
    print('Wrong answers', 5 - right_answers)
    print('Right answers %', right_answers / 5 * 100)
    print('Wrong answers %', (5 - right_answers) / 5 * 100)

    answer = input('Do you want to start again? yes/no')

    if answer == 'no':
        break
