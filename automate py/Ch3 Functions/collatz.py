# Collatz Sequence

def collatz(number):

    if number % 2 == 0:
        print(number // 2)
        return number // 2
    else:
        print(number * 3 + 1)
        return number * 3 + 1

print('Please enter any integer value.')

while True:
    try:
        x = int(input())
        break
    except:
        pass
    print('Please enter a valid integer value.')


while x != 1:
    x = collatz(x)
    
