try :
    number = float(input('Enter a number : '))
    if number > 0 :
        print('The number is positive ')
    elif number < 0 :
        print('The number is negetive ')
    else :
        print('The number is zero ')
except ValueError :
    print('wrong input')