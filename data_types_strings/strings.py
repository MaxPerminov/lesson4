# Strings , methods , slice , f'strings , """ """ , interpolation

string = "Hello world"
string = 'Hello world'
# mulyline strings
string = """
Hello world
Hello world
Hello world
"""

not_string = 23
# str() - method , get value and inteper it's as a string

# type
# ! X str = "u"

# "", '' , """ """

# print(type(str(not_string)))

# string = "We're #1"
# string = """"
#     "Somethimes i feal lonely and depressed , but than i remembered what once Winston Ch. said ... We'are " (c)meme
# """


# print(string)


# * methods
# len(<variable_name> / "string") - get lenght
# print(len("Hello world"))

# * f' method

first_name = "John"

# print(f"Hello {first_name}")

# * concat

# print("Hello " + first_name)
# print("Hello {}".format(first_name))
# print(f"Hello {first_name}")

# string = "Hello everyone!"
# string[0] = "A"


# |6| - distance
# -6 or 6
# print(string[-1])
# print(string[0])
# print(string[1])


# ! Practise
# string = "Hi , my name is John! ;)"

# find_last_character = len(string) - 1
# find_pre_last_character = len(string) - 2

# comma_with_fullstop = string[find_pre_last_character]
# rounded_bracket = string[find_last_character]

# print(comma_with_fullstop + rounded_bracket)

string = "Hi , my name is John! ;)"


# slice - means cut string by points [arg1(start) , arg2(end)]
# print(string[0:2])

# short hand
# print(string[:2])


sliced_string = string[-1:-8]
#
sliced_string = string[-8:]
# print(sliced_string)

# dummy methods

# print(string.lower())
# print(string.upper())

# input() - ineractive , to get something from user

# user_name = input("Enter your name : ")§

# print(user_name.lower())


# ? .rstrip , .lstrip , .strip - remove / slice / delete / cut whitespaces

# print(user_name.lower().strip())

#  startswith

role = "admin"

# print(role.startswith("ad"))
# print(role.endswith("in"))

# a[href="http://localhost:3000"] Home

# flwekjflskdfmlksdmflksdflksdflksdflksdflkdfsdlkfsdlkmsdlksdlksdflksdfmsdfklmsdflsfdkslsmldfkmsfdfsdsdfklmsfkldmsldfkfsdklsfdklmslmksfdkmdf

# * find

# greeting = "Hello everyone!"

# is_hello = greeting.lower().find("john")
# print(is_hello)