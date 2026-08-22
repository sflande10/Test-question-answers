class Animal:
    def speak(self):
        print("The animal makes a noise")
class Cat(Animal):
    def speak(self):
        print("Meow")
class Dog(Animal):
    def speak(self):
        print("Woof")
cat = Cat()
dog = Dog()
cat.speak()
dog.speak()