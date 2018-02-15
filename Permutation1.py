num1 = int(input('Please enter first number ' ))
num2 = int(input('Please enter second number ' ))

n1 = num1
n2 = num2

factorial1 = 1
factorial2 = 1

if num1 > 0:
    while n1 > 0:
        factorial1 *= n1
        n1 -= 1
elif number1 == 0:
    factorial = 1
else:
    print ('Number is negative')
if num2 > 0:
   while n2 > 0:
        factorial2 *= n2
        n2 -= 1
elif number2 == 0:
        factorial2 = 1
else:
        print ('Number is negative')

per1 = int(factorial1 /factorial2)
print ('Permutation of number1 and number2 is ', per1)
