my_num = int(input('Enter a number to find the sum up to '  ))
result = 0
current = my_num
while current >= 0:
  result += current
  current -= 1
print (result)
