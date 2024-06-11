# 1.
# n = int(input('Raqam kiriting: '))
# dictionary = dict()
# for i in range(1, n + 1):
#     dictionary[i] = i * i
# print(dictionary)
# 2.
# my_dict = {
#     'apples': 100,
#     'pears': 50,
#     'peaches': 75
# }
# result = sum(my_dict.values())
# average = result // 3
# print(average)
# 3.
# names = [
#     'Alisher',
#     'Ibrohim',
#     'Malika'
# ]
# grades = [
#     10,
#     8,
#     9
# ]
# res = {}
# for key in names:
#     for value in grades:
#         res[key] = value
#         grades.remove(value)
#         break
# print(res)
# 4.
# cities = {
#     'Moscow': (550, 370),
#     'London': (510, 510),
#     'Paris': (480, 480)
# }
# x1, y1 = 550, 370
# x2, y2 = 510, 510
# x3, y3 = 480, 480
#
# distance = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
# distance2 = ((x1 - x3) ** 2 + (y1 - y3) ** 2) ** 0.5
# distance3 = ((x2 - x3) ** 2 + (y2 - y3) ** 2) ** 0.5
# print("Distance between cities Moscow ({}, {}) and London ({}, {}) is {}".format(x1, y1, x2, y2, distance))
# print("Distance between cities Moscow ({}, {}) and Paris ({}, {}) is {}".format(x1, y1, x3, y3, distance2))
# print("Distance between cities London ({}, {}) and Paris ({}, {}) is {}".format(x2, y2, x3, y3, distance3))
# 5.
# goods = {
#     'Lampa': '12345',
#     'Stol': '23456',
#     'Divan': '34567',
#     'Stul': '45678'
# }
# store = {
#     '12345': [
#         {
#             'quantity': 27,
#             'price': 42
#         },
#     ],
#     '23456': [
#         {
#             'quantity': 22,
#             'price': 510
#         },
#         {
#             'quantity': 32,
#             'price': 520
#         },
#     ],
#     '34567': [
#         {
#             'quantity': 2,
#             'price': 1200
#         },
#         {
#             'quantity': 1,
#             'price': 1150
#         },
#     ],
#     '45678': [
#         {
#             'quantity': 50,
#             'price': 42
#         },
#         {
#             'quantity': 12,
#             'price': 510
#         },
#         {
#             'quantity': 43,
#             'price': 510
#         },
#     ],
# }
#
# for key, value in goods.items():
#
#     product_quantity = 0
#     product_value = 0
#
#     for position in store[value]:
#         product_quantity += position['quantity']
#         product_value += position['quantity'] * position['price']
#
#     print(key, '-', product_quantity, 'ta, narxi', product_value, "so'm")

# 6.
# student1 = {
#     'name': 'Alisher',
#     'age': 20,
#     'courses': ['Math', 'Physics'],
#     'grades': {'Math': 90, 'Physics': 85}
# }
# student2 = {
#     'name': 'Ibrohim',
#     'age': 21,
#     'courses': ['Math', 'Chemistry'],
#     'grades': {'Math': 70, 'Physics': 80}
# }
#
# merged_dict = student1.copy()
#
# for key, value in student2.items():
#     merged_dict[key] = value
#
# print(merged_dict)
