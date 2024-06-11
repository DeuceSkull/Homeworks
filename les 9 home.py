# 1.
# def capitalize(names):
#     return names
#
#
# names = ['alfred', 'tabitha', 'william', 'arla']
# print(list(map(lambda a: a.capitalize(), names)))


# 2.
# def higher_numbers(scores):
#     return scores
#
#
# scores = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]
#
# print(list(filter(lambda a: a > 75, scores)))
# 3.
# def palindrome(words):
#     return words
#
#
# words = ['anna', 'alexey', 'alla', 'kazak', 'dom']
# print(list(filter(lambda x: (x == ''.join(reversed(x))), words)))
# 4.
# import time
#
# n = int(input('Son kiriting: '))
#
# s = time.time()
# lst = [i for i in range(n)]
# f = time.time()
#
# print(len(lst))
# print(f - s)
# 5.
# def length(words):
#     return words
#
#
# words = ['apple', 'banana', 'cherry']
# print(list(map(lambda a: len(a), words)))

# 6.
# def fruits(a, b):
#     return a + b
#
#
# a = map(fruits, ('apple', 'banana', 'cherry'), ('orange', 'lemon', 'pineapple'))
# print(list(a))
