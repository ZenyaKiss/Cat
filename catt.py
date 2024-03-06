class Cat():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(self.name.title() + "is now eating")

    def sleep(self):
        print(self.name.title() + "sleeping")


my_cat = Cat("keks", 12)
your_cat = Cat("lucy", 3)
his_cat = Cat("Max", 9)
print("My cat's name is " + my_cat.name.title() + ".")
print("My cat is " + str(my_cat.age) + "years old.")
my_cat.eat()

print("Your cat's name is " + your_cat.name.title() + ".")
print("Your cat is " + str(my_cat.age) + "years old.")
your_cat.eat()

print("His cat's name is " + his_cat.name.title() + ".")
print("His cat is " + str(his_cat.age) + "years old.")
his_cat.eat()