x = int(input('Please enter a number x '))
y = str(x)
l = len(y)
num1 = x
rem = 0
if l == 1:
  print('This is a good number')
elif l == 2:
  rem = num1%2
  if rem == 0:
    print('This is the best number')
  else:
    print('This is a better number')
else:
  print('This is a horrible number')
