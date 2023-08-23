class Person:
    def __init__(self, name, age):
        if self.validateInputs(name, age):
            self.name = name
            self.age = age
        else:
            print("Please enter supported values")

    def validateInputs(self, name, age):
        if type(name) == str and type(age) == int:
            return True
        else:
            return False

    pass


person1 = Person("Alice", 25)
person2 = Person("Bob", 30)

print(
    f"Person 1 - Name: {person1.name} Age: {person1.age}\n Person 2 - Name: {person2.name} Age: {person2.age}\n"
)
