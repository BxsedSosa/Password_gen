import random
import string


print('Type "1" for password without special characters \nType "2" for password with speical characters')
choice = int(input('Type: '))
password_len = int(input('How long would you like your password?: '))
my_password = ''

if choice == 1:
    for i in range(password_len):
        my_password += random.choice(string.ascii_letters)
else:
    for i in range(password_len):
        my_password += random.choice(string.printable)

print('Your new password is:', my_password)