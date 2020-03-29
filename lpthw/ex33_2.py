x = int(input("How long would you like to run this loop?\n>"))

y = int(input("By how much would you like to increment?\n>"))

def while_func(length, increment):
    i = 0
    numbers = []
    while i < length:
        print(f"At the top i is {i}")
        numbers.append(i)

        i += increment
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")

print(while_func(x, y))
