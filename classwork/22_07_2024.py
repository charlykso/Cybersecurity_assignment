from user import User

class Person:
    def __init__(self, fullName, phoneNumber):
        self.name = fullName
        self.phoneNumber = phoneNumber

    def __str__(self):
        return f"{self.name} {self.phoneNumber}"
    
    def getName(self):
        return f"Hello, my name is {self.name}"

person1 = Person("Remigius", "08077663355")
print(person1.name)
person1.name = "Charles"
print(person1.phoneNumber)
print(person1)
print(person1.getName())

Esther = Person("Esther", "09088664433")
print(Esther)
print(Esther.phoneNumber)
print(Esther.getName())

user1 = User("Prince", "Igwe", "prince@gmail.com", "prince123")
print(user1)
print(user1.greet())
print(user1.getLoginDetails())
print(user1.created_at)