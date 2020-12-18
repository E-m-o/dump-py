from numpy import random as rand
while(True):
    print('Choose 1 for rock')
    print('Choose 2 for paper')
    print('Choose 3 for scissors')
    choice = {1:'rock', 2:'paper', 3:'scissor'}
    user_choice = int(input('Enter your choice:'))
    # print('You chose')
    computer_choice = rand.randint(1,4)
    print('User\'s choice:{}'.format(choice[user_choice]))
    print('Computer\'s choice:{}'.format(choice[computer_choice]))
    if computer_choice == user_choice:
        print('It\'s a tie!!!')
    if user_choice == 1:
        if computer_choice == 3:
            print('User wins!!!')
        elif computer_choice == 2:
            print('Computer wins!!!')
    elif user_choice == 2:
        if computer_choice == 1:
            print('User wins!!!')
        elif computer_choice == 3:
            print('Computer wins!!!')
    elif user_choice == 3:
        if computer_choice == 2:
            print('User wins!!!')
        elif computer_choice == 1:
            print('Computer wins!!!')
    else:
        print('Enter a valid number..')
    check = input('Do you want to continue(y/n):')
    if check != 'y':
        break