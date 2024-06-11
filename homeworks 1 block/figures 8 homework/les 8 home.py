# 1.
# def get_num(num):
#     summ = 0
#     while num != 0:
#         summ = summ + int(num % 10)
#         num = int(num / 10)
#
#     return summ
#
#
# num = 108
# print(get_num(num))

# 2.
# sec = int(input('Enter seconds: '))
#
# days = sec // (24 * 3600)
# time = sec % (24 * 3600)
#
# hours = time // 3600
# time %= 3600
#
# minutes = time // 60
#
# time %= 60
#
# seconds = time
# print(f'\n\t\t\t\t\t|{days}:{hours}:{minutes}:{seconds}|')
# 3.
from figures.circle import circle
from figures.square import square
from figures.triangle import triangle

default_radius = 5

a = int(input('Enter A length of triangle: '))
b = int(input('Enter B length of triangle: '))
c = int(input('Enter C length of triangle: '))
print(triangle(a, b, c))

print(square(int(input('Enter the perimeter of square: '))))

print(circle(int(input('Enter the radius of circle: '))))
