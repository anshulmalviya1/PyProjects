# calculate age using Python
while True:
# exception    
    try:
        age = int(input('Please enter the year you were born. for example = 2001  '))
        age = 2021-age
        print(f'You are {age} old')
    except ValueError:
         print('Please enter a number')
    except ZeroDivisionError:
         print('Please enter age value year heigher then 0')
    else:
         print('thankyou') 
    break
