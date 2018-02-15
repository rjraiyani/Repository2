total = 0
m = 0
n = 0
for idx,num in enumerate(range(1,101)):
    m = num % 3
    n = num % 5
    if (m == 0) and (n == 0):
        num = str('fizz buzz')
    elif m == 0:
        num = str('fizz')
    elif n == 0:
        num = str('buzz')
    print(num)
