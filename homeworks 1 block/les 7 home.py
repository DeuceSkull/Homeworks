# 1.
# def max_num(a, b, c):
#     return max(a, b, c)
#
#
# print(max_num(a=5, b=8, c=2))
# 2.
# nums = [8, 2, 3, 0, 7]
# index = 0
# for i in nums:
#     index += i
# print(index)

# 3.
# nums = [8, 2, 3, -1, 7]
# index = 1
# for i in nums:
#     index *= i
# print(index)
# 4.
# a = '1234abcd'
# print(a[::-1])
# 5.
# def factorial(numm):
#     if numm == 0:
#         return 1
#     else:
#         return numm * factorial(numm - 1)
#
#
# num = int(input("Enter the factorial number : "))
# print(factorial(num))
# 6.
# text = input('Write: ')
# isup = 0
# islower = 0
# for i in text:
#     if i.islower():
#         islower += 1
#     elif i.isupper():
#         isup += 1
#     else:
#         pass
# print(f'Your text: {text}\nUppercase letters: {isup}\nLowercase letters: {islower}')
# 7.
# def palindrome(word):
#     return word == word[::-1]
#
#
# word = input('Enter the palindrome word: ')
# ans = palindrome(word)
#
# if ans:
#     print("True")
# else:
#     print("False")
# 8.
# p = int(input('Enter the amount in rub: '))
# r = .10
# n = 1
# t = int(input('Enter the period in years: '))
# for period in range(t):
#     amount = p * (pow((1 + r / n), n * (period + 1)))
#     print('Year:', period + 1, amount)
# 9.
# nums = [45, 55, 60, 37, 100, 105, 220]
# for i in nums:
#     if i % 15 == 0:
#         print(i)
