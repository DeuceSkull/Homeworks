# 1.
# products = ['banan', 'kivi', 'olma', 'ananas']
#
# while True:
#     user_text = input('Komandani kiriting: ')
#     if user_text == 'stop':
#         break
#     if len(user_text.split(' ')) == 2:
#         command, product = user_text.split(' ')
#         if command == 'add':
#             if product in products:
#                 print(f'Product {product} spiskaga qoshildi {products}')
#             else:
#                 products.append(product)
#                 print(f'Qoshildi {product} spiskaga {products}')
#         elif command == 'delete':
#             if product in products:
#                 products.remove(product)
#                 print(f'Ochirildi {product} royxatidan {products}')
#             else:
#                 products == product
#                 print(f'Produktda {product} shundogam yoq edi {products} royxatida!')
#         elif command == 'clear':
#             products.clear()
#             print(f'Produktlar ochirildi bu royxatdan {products}')
#         elif command == 'search':
#             print(f"Ro'yxatingizda {products} lar bor")
#     else:
#         print('Komanda natogri berildi !!!')
# 2.
# deposit = 1000000
# years = 5
# percent = 10
# next_year = deposit // percent
# print(f"{deposit} ", end='')
# for i in range(1, years):
#     deposit += next_year
#     print(f"{deposit} ", end='')

# p = int(12000)
# r = .10
# n = 1
# t = 5
# for period in range(t):
#     amount = p * (pow((1 + r / n), n * (period + 1)))
#     print('Year:', period + 1, amount)

# 3.
# rows = 9
#
# for i in range(1, rows + 1):
#     for j in range(1, i + 1):
#         print(i, end=' ')
#     print('')
# 4.
# numbers = [12, 75, 150, 180, 145, 525, 50]
# numbers2 = []
#
# for i in numbers:
#     if i > 150:
#         if i > 500:
#             break
#         continue
#     if i % 5 == 0:
#         numbers2.append(i)
#
# print(numbers2)
# 5.
# num1, num2 = 0, 1
#
# n = 7
#
# print(num1, num2, end=' ')
#
# for i in range(n):
#     num1, num2 = num2, num1 + num2
#     print(num2, end=' ')
