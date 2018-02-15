number = int(input('Please enter a number ' ))
n = number
factorial = 1
if number > 0:
    while n > 0:
        factorial *= n
        n -= 1
elif number == 0:
    factorial = 1
else:
    print ('Number is negative')
if number >= 0:
  print (factorial)
