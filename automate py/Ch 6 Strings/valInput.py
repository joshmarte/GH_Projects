while True:
    print('Enter your age')
    age = input()
    if age.isdecimal():
        break
    print('Please enter a number for you age.')

while True:
    print('Select a new password (letters and numbers only):')
    password = input()
    if password.isalbum():
        break
    print('Passwords can only have letters and numbers.')
