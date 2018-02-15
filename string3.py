# Example input() statement
s = input('Please enter a string: ')
l = len(s)
if l < 5:
# Use this error message if the string is too short
   print('String too short.')
else:
    my_str = s[2:5]
    print(my_str)
