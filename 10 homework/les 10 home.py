# 1.
# count = 0
# with open('mbox-short.txt', mode='r', encoding='utf-8') as file:
#     for line in file:
#         if line.startswith('From '):
#             lst = line.split(' ')
#             count += 1
#             print(count, lst[1])
#
# 2.
#
# fh = open('romeo.txt')
# lst = []
# for line in fh:
#     word_split = line.split(' ')
# for word in word_split:
#     lst.append(word)
#
# print(sorted(lst))
# 3.
# with open('article.txt', 'r') as file:
#     lines = file.readlines()
#
# last_line = (lines[7])
#
# content = last_line
#
# print(content)

# 4.
# with open('article.txt', mode='r', encoding='utf-8') as file:
#     for words in file:
#         print(max(words.split(), key=len))
# 5.
# with open('Poems.txt', 'r') as file:
#     poem_lines = file.readlines()
#
# reversed_poem = reversed(poem_lines)
#
# combined_poems = list(reversed_poem)
#
# with open('the_road_not_taken.txt', 'w') as combined_file:
#     combined_file.writelines(combined_poems)
