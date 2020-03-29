# the variables in your function are not are not connected
#to the variables in your script

def chesse_and_crackers(chesse_count, boxes_of_crackers):
    print(f"You have {chesse_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket. \n")

print("We can just give the function numbers directly")
chesse_and_crackers(20, 30)

print("Or we can use variables from our script")
amount_of_cheese = 10
amount_of_crackers = 50

chesse_and_crackers(amount_of_cheese, amount_of_crackers)

print("We can even do math inside too:")
chesse_and_crackers(10+20, 5+6)

print("And we can combine the two, varibles and math:")
chesse_and_crackers(amount_of_cheese+100, amount_of_crackers+1000)
