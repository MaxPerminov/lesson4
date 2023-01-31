# practice


# students = [
#     [
#         "John", 2323
#     ],
#     [
#         "Mike", 3232
#     ],
#     [
#         "Mike", 6000
#     ],

# ]

# max payment
# total payment


# name of person with min payment

# i = 0
# prev_person = students[0]
# min_payment_person = ""
# max_val = 0
# total = 0

# for student in range(len(students)):
#     payment = students[student][1]

#     total += payment

#     prev_person = students[student]

#     if prev_person[1] > students[student][1]:
#         max_val = students[student][1]
#     else:
#         max_val = prev_person[1]

# print(max_val)
# print(total)

# print(students)


# students = [
#     [
#         "John", 2323
#     ],
#     [
#         "Mike", 3232
#     ],
#     [
#         "Mike", 6000
#     ],
#     [
#         "Bob", 1313
#     ]

# ]

# loop / cycle
# prev_value = students[0][1]

# for i in range(len(students)):
#     if students[i][1] < prev_value:
#         prev_value = students[i][1]
#     else:
#         continue

# print(prev_value)