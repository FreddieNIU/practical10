'''
get the number inputted by the user
if the number is a negative number then
    print the number should be greater than or equal to 0
else
    set up a counter i with the value 0
    for i from 0 to the number,step is 1
        if i is the square root of the number
            stop loop
    if i is the square root of the number then
        print the square root of the number
    elif i is equal to the number then
        print the number is not perfect square
program finish
'''

number = int(input('Please input an integer here: '))
if number < 0:
    print('The number should be >= 0')
else:
    i = 0
    for i in range(number+1):
        if i ** 2 ==number:
            break
    if i ** 2 == number:
        print('The square root of ',number,' is ',i)
    elif i == number:
        print('The number ',number,' is not a perfect square')
print('\nFinish !')