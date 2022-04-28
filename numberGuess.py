from random import randint

run = True
difficulity = ['easy','normal','hard']
difficulity_input = input('easy  normal  hard ? ')
# -----------------------------------------------------------------------
if difficulity_input in difficulity:

    if difficulity_input == difficulity[0]:
        n = randint(1,10)
        numbers_of_chice = 0

        num = int(input('take a guess '))
        while run:
            if n> num:
                print('bigger')
                print('------------------------------')
                numbers_of_chice += 1
                if numbers_of_chice == 4:
                    print('Game Over')
                    run = False
                else:    
                    num = int(input('take a guess '))
            elif num>n:
                print('smaller')
                print('------------------------------')
                numbers_of_chice += 1
                if numbers_of_chice == 4:
                    print('Game Over')
                    run = False
                else:
                    num = int(input('take a guess '))
            elif num==n:
                print('you won🎉🎉')
                run = False
    elif difficulity_input == difficulity[1]:
        n = randint(1,100)
        numbers_of_chice = 0

        num = int(input('take a guess '))
        while run:
            if n> num:
                print('bigger')
                print('------------------------------')
                numbers_of_chice += 1
                if numbers_of_chice == 7:
                    print('Game Over')
                    run = False
                else:
                    num = int(input('take a guess '))
            elif num>n:
                print('smaller')
                print('------------------------------')
                numbers_of_chice += 1
                if numbers_of_chice == 7:
                    print('Game Over')
                    run = False
                else:
                    num = int(input('take a guess '))
            elif num==n:
                print('you won🎉🎉')
                run = False
    elif difficulity_input == difficulity[2]:
        n = randint(1,1000)
        numbers_of_chice = 0

        num = int(input('take a guess '))
        while run:
            if n> num:
                print('bigger')
                print('------------------------------')
                numbers_of_chice += 1
                if numbers_of_chice == 10:
                    print('Game Over')
                    run = False
                else:
                    num = int(input('take a guess '))
            elif num>n:
                print('smaller')
                print('------------------------------')
                numbers_of_chice += 1
                if numbers_of_chice == 10:
                    print('Game Over')
                    run = False
                else:
                    num = int(input('take a guess '))
            elif num==n:
                print('you won🎉🎉')
                run = False