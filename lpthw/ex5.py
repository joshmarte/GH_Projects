#format string
name     = 'James'
age      = 25
height   = 80 #inches
height_c = height * 2.54
weight   = 180 # pounds
weight_kilo = round(weight / 2.205)
eyes     = 'Brown'
teeth    = 'White'
hair     = 'Black'

print(f"Let's talk about {name}.")
print(f"He's {height} inches tall.")
print(f"He's {weight} pounds heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")

print(f"{height} in inches is equal to {height_c} centemeters.")
print(f"{weight} in pounds is equal to {weight_kilo} in kilograms.")
