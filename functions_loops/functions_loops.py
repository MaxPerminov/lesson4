# custon functions
# def greeting():
#     print("Hello world")


# greeting()

# params , args
# def greeting(first_name, surname="Doe"):
#     print(f"Hello, {first_name}")
#     print(surname)


# greeting("John")
# greeting("Kir", "Bibby")

# def add(x, y):

#     retsult = x + y
#     # return - get back data
#     print(retsult)


# result = add(13, 10)

# None is nothing

# print(result)
# scope

# name = "Bob"


# def sayHello(name):
#     person = "John"

#     updated_name = name + "!"

#     def sayHelloTo(name):
#         return [name, person, updated_name]

#     def reEvaluete(callback):
#         list_of_users = callback(person)

#         for i in range(len(list_of_users)):
#             print(list_of_users[i])

#         return list_of_users

#     return reEvaluete(sayHelloTo)


# def createUser(age=23):

#     name = "Mike"
#     obj = {}
#     obj['name'] = name
#     obj['age'] = age
#     obj['sayHello'] = sayHello

#     return obj


# user1 = createUser()

# greeting = user1['sayHello'](user1['name'])


# counter
# i = 0

# cycles
# while i < 10:
#     i += 1
#     print(i)

# counter ; end
# i = 0

# for i in range(len("Hello")):
#     print("Hello")