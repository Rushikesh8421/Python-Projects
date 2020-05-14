restart='Yes'
while restart=='Yes':
    age_bod=int(input('Please enter your age or birth date: '))
    present_age=2020-age_bod
    former_age=age_bod+100
    yr_old=present_age+100
    if 1870<age_bod<2020:
        print(f'Your present age is {present_age}')
        print(f'You will be 100 years old in {former_age} year')
    elif 0<age_bod<150:
        print(f'Your date of birth is {present_age}')
        print(f'you will be 100 years old in {yr_old} year')
    else:
        print('Please enter valid input')
        
           
