#Comma Code
food = ['apples',
        'bananas',
        'tofu',
        'cats'
        ]

def comma(list):
    string = ''
    for item in list:
        if int(list.index(item)) == int(len(list)- 1):
            string = string + 'and ' + item
        else:
            string = string + item + ', '

    return print(string)

comma(food)
