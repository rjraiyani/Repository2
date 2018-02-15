x = int(input('Please enter a number '))
m = x % 2
n = x % 3
if m == 0: #Even number
    if n == 0:
        print('Even and Divisible by 2')
    else:
        print('Even')
else:
    if n == 0:
        print('odd and divisible by 3')
    else:
        print('odd') 
