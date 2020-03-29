# Alter Before or After

class Parent():

    def altered(self):
        print("PARENT altered() ")

class Child(Parent):

    def altered(self):
        print("CHILD, BEFORE PARENT altered()")
        super(Child, self).altered()
        print("CHILD, AFTER PARENT altered()")

dad = Parent()
son = Child()

dad.altered()
print('-'*10)
son.altered()
