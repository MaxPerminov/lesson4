# def constructor(n, s):
#     return {
#         "name": n,
#         "surname": s ,
#     }


# john = constructor("John", "Doe")
# john = constructor("Mike", "Bibby")

# print(john)

# class Dog:
#     legs = 4

#     def __init__(self, name="Jack", age=23):
#         self.name = name
#         self.age = age

#     def desc(self):
#         print(f"{self.name} , {self.age}")


# dog = Dog("John", "Hello")
# dog2 = Dog("John", 13)

# dog.desc()
# dog2.desc()
# dog.show_self()
class Product:

    def __init__(self, label, price):
        self.label = label
        self.price = price


class Human:

    is_alive = True

    def __init__(self, name, age, money, profession):
        self.name = name
        self.age = age
        self.money = money
        self.profession = profession

    def speak(self, sound):
        print(sound)

    def buy(self, goods):
        self.money -= goods
        print(self.money)


class Admin(Human):
    def __init__(self, name, age, money, profession, isAdmin):
        super().__init__(name, age, money, profession)
        self.isAdmin = isAdmin

    def speak(self, sound="Helllooooo , immmmm adminnn"):
        return super().speak(sound)


admin_john = Admin("John", 23, 2323, "admin", True)

admin_john.speak()

# john = Human("John", 23, 2323, "admin")
# snikers = Product("Snikers", 23)

# john.speak("Hello world")

# john.buy(snikers.price)

class Person:

    surname = "Doe"

    def __init__(self, n, a):
        self.self_skills = ("HTML", "PHP", "SQL")
        self.name = n
        self.age = a

    def describe(self):
        return f"NAME : [{self.name}] , AGE : [{self.age}]"

    def skills(self):
        print(self.self_skills)
        for skill in range(len(self.self_skills)):
            print(self.self_skills[skill])

john = Person("John", 23)
mike = Person("Mike", 32)

johnsData = john.describe()
mikesData = mike.describe()

john.skills()

# print(johnsData)
# print(mikesData)

# print(john.name)
# print(mike.name)

# print(john.surname)
# print(mike.surname)

# print(john == mike)  ## not(diferent objects)