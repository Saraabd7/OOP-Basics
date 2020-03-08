
# Define our animal class
# Sudo code:
# Looks / characteristics of every animal
    # name, age, colour heart, brain
# Behaviours / Methods of every animal
    # Eat, sleep, reproduce, potty, make_sound

class Animal():
    # define behaviours and characteristics
    def __init__(self, name, age, color):
    # define the characteristics of every animal
        self.name = name
        self.age = age
        self.colour = color
        self.heart = True
        self.brain = True
    # defining the method .eat(), .sleep(). .reproduce(), .potty(), .make_sound()
    def eat(self):
        return 'Nom nom nom'
    def sleep(self):
        return 'zzzZzZZzZZZz'
    def reproduce(self):
        return 'Need some privacy'
    def potty(self):
        return 'About to let last night\'s food out'
    def make_sound(self):
        return 'woof'
# To call methods, we need an object of this class
# creating an instance of class animal
ringo = Animal('Ringo', 44, 'Green') #creates instance of class animal and assigns to variable ringo
# checking and printing the instance
print(ringo)
print(type(ringo))
# calling methods on instance of animal
print(ringo.eat())
print(ringo.potty())
print(ringo.sleep())
# Check the attribute of an instance
print(ringo.name, ringo.age)

# second animal
mini = Animal('John', 92, 'Pink')
print(mini.name, mini.age, mini.sleep())
