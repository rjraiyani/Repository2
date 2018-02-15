#user_input = input('Add "oR wAs it??" (y/n)? ')
user_input = input('String to add to end of my_str: ')
my_str = 'This String was not Chosen Arbitrarily...'
#print(my_str.upper())
#print(my_str[14])
#my_str1 = my_str.replace("was not","wasn't")
#print(my_str1)
#my_str2 = my_str.lower()
#print(my_str2)
#my_str3 = 'oR wAs it??'
#if user_input == "y":
#    my_str = my_str + my_str3
#else:
#    pass
#print(my_str)
#print(my_str.lower())
#print(my_str[41:])
i = len(user_input)
if i < 10:
    my_str = my_str + user_input
print(my_str)
