import random 
play_again='y'
while play_again=='y':
    answer=random.randint(1,10)
    
    chances=1
    count=0
    while 'guess' != answer:
        if count==3:
            print('you lost the game!')
            break
        guess=int(input('choose the no. between 1 to 10 '))    
        if guess < answer:
            print('your no. is small')
        elif guess > answer:
            print('your no. is large')
            
        
        else:
            print(f'you have guessed it correct and you tried for {chances} times')
            break
        chances += 1
        count += 1    
    play_again= input('continue? ')
            