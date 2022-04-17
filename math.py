import random
name = input('what is your name ')
print(f'hi {name}, this is a math test')
numquestword =  input('how many questions do you want ')
numquest=int(numquestword)
numdone = 0
points=0
while numdone < numquest:
    num1 = random.randint(1,10)
    num2 = random.randint(1,10)
    # 1 = + 2 = - 3 = x 4 = /
    midthing = random.randint(1,4)
    if midthing == 1:
        answerword = input(f'what is {num1} + {num2} ')
        answer = int(answerword)
        if answer == num1 + num2:
            print('yay you got it correct')
            points+1
        else:
            print('oof')
    elif midthing == 2:
        answerword = input(f'what is {num1} - {num2} ')
        answer = int(answerword)
        if answer == num1 -  num2:
            print('yay you got it correct')
            points+1
        else:
            print('oof')
    elif midthing == 3:
        answerword = input(f'what is {num1} x {num2} ')
        answer = int(answerword)
        if answer == num1 *  num2:
            print('yay you got it correct')
            points+2
        else:
            print('oof')
    elif midthing == 4:
        answerword = input(f'what is {num1} / {num2} ')
        answer = float(answerword)
        if answer == num1 / num2:
            print('yay you got it correct')
            points+2
        else:
            print('oof')
    numdone+1
print('your done')
        
    
