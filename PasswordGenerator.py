user_number = int(input('Enter length of your passsword: '))
print(user_number)

if user_number > 15: 
    print(' it seems like you have bigass password')
elif user_number < 4:
    print('WTF bro?')
