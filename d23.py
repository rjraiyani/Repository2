user_input1 = input('Enter a string ')

#if l == '!':
#    print(user_input1.upper())
#else:
#    print(user_input1.lower())
vowels = ['a','e','i','o','u','A','E','I','O','U']
for idx,letter in enumerate(user_input1):
    if letter in vowels:
        user_input1 = user_input1.replace(letter,'')
print(user_input1)
