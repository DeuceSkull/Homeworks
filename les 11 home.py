# 1.
# a = input('Birinchi: ')
# b = input('Ikkinchi: ')
# try:
#     a = int(a)
#     b = int(b)
# except ValueError:
#     a = str(a)
#     b = str(b)
# print('Natija:', a+b)
# 2.
# import re
# simple = 'Exercises number 1, 12, 13, and 345 are important 456'
# nums = re.findall('[0-9]{1,3}', simple)
# for n in nums:
#     print(n)
# 3.
# food = ["chocolate", "chicken", "corn", "sandwich", "soup", "potatoes", "beef", "lox", "lemonade"]
#
# fifth = []
#
# for x in food:
#     try:
#         fifth.append(x[4])
#     except IndexError:
#         pass
# print(fifth)
# 4.
# import re
#
#
# def color_test(color_code):
#     color_pattern = re.compile(r'^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$')
#     if color_pattern.match(color_code):
#         return True
#     else:
#         return False
#
#
# test_colors = ['#ABCDEF', '#123456', '#00F', '#GHIJKL', '123456']
#
# for color in test_colors:
#     if color_test(color):
#         print(f"{color} - Correct color code")
#     else:
#         print(f"{color} - Incorrect color code")
# 5.
# import re
#
# text = "Завтрак в 09:00"
# pattern = r"(?:[01]\d|2[0-3]):[0-5]\d"
#
# match = re.search(pattern, text)
#
# if match:
#     print(f"Found time: {match.group()}")
# else:
#     print("No valid time found in the text.")
