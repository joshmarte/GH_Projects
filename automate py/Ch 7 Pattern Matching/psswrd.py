# Strong Password Detection

import re

pass_ = input('Please enter your desired password \n>> ')

def passTest(password):

    test_Regex = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$')
    test = test_Regex.search(password)

    if test == None:
        print('Please create a stronger password')
        pass_ = input('Please enter your desired password \n>> ')
        passTest(pass_)
    else:
        y = test.group()
        return print('Thank you, your password ' + y + ' has been saved'), y

passTest(pass_)
