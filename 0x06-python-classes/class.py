class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound."

dog = Animal("Dog")
print(dog.speak())
