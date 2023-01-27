# if 1 > 29:
#     print("Hello")
# elif 5 > 10:
#     print("World")
# else:
#     print("Heh")

# if 1 > 0:
#     print("Hello")

# if 1 >= 1:
#     print("World")

# and | or | not

# strict
# if 1 < 2 and 4 < 4:
#     print("Correct equation")

# print(not not True == False)

john = {
    "name": "John",
    "age": 23,
    "gender": "robot"
}

isJohn = john["name"] == "John"
isAdult = john["age"] == 23
isAdmin = john["gender"] == "admin"

if isJohn and isAdult and not isAdmin:
    print("hello John")

print(john)