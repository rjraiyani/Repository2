#user_input = input('Add the number 4 to mylist (y/n)? ')
user_input = input('Enter a string ' )
n = len(user_input)
my_list = [1, 'hello', 2, 'there', 3, 'list']
#print(my_list[1])
#print(my_list[0])
#print(my_list[1:6:2])
#if user_input == 'y':
#    my_list.append(4)
#print(my_list)
#print(my_list[0::2])
#my_list.remove('list')
#print(my_list)
#print(my_list[1::2])
if n < 8:
    my_list.append(user_input)
else:
    my_list.append(4)
print(my_list)
