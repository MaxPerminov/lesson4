# key / value

# john = {
#     "name": "John",
#     "age": 23,
#     "pocket": 2323,
#     "isClerk": True,
#     "reletive": {
#         "name": "Mike",
#         "age": 13,
#         "pocket": "Twix"
#     }
# }

# mike = john["reletive"]

# mike["age"] = 32  #### age changes in both john and mike - vars reffers to one object

# print(mike)
# print(john)

# key_value_pairs = (
#     ("name", "John"),
#     ("surname", "Doe")
# )

# print(dict(key_value_pairs)["name"])

# john = {
#     "name": "John",
#     "age": 23,
#     "surname": "Doe"
# }

# john["name"] = "Mike"

# print(john)

# for key in john:
#     print(key, john[key])




# def run():

#     data_base = []

#     def createQuestion(str):
#         return str + " 'y/Y' if not 'n/N'"

#     def appendToDB(db, obj):
#         db.append(obj)

#     def createUser():
#         return {}

#     def createUserProperties(user):

#         while True:

#             if input(createQuestion("If you wanna continue press")).lower() == "y":
#                 key = input("Enter key name: ")
#                 user[key] = input(f"Enter your {key} : ")

#             else:
#                 appendToDB(data_base, user)
#                 print(data_base)
#                 break

#     print("Hello , user")

#     while True:

#         if input(createQuestion("Do you want to create a user")).lower() == "y":
#             user = createUser()

#             if input(createQuestion("Do you want to add some props")).lower() == "y":
#                 createUserProperties(user)
#         else:
#             print(data_base)
#             break


# run()

# CREATE PROGRAM

# Animals

# 1) Add new animal into animals array []
# 2) Add property to animal
# 3) Append animal into  array []
# 4) Drop (delete) animal from array []
# 5) Edit animals prop