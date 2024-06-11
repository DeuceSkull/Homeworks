# 1.
# person = int(input('Yoshingizni kiriting: '))
#
# if person <= 18:
#     print("Siz o'qishingiz kerak.")
# elif person > 18 and person <= 50:
#     print("Siz ishlashingiz kerak")
# elif person > 50 and person <= 59:
#     print("Siz yaqinda nafaqaga chiqasiz")
# elif person > 59 and person <= 110:
#     print("Siz pensionersiz")
# else:
#     print("Siz haqiqiy bo'lmagan yosh kiritingiz")

# 2.
# numbers = int(input("Oy nomerini kiriting:  "))
#
# if numbers == 1:
#     print("Oy nomi: Yanvar. Kunlar soni: 31.")
# elif numbers == 2:
#     print("Oy nomi: Fevral. Kunlar soni: 28.")
# elif numbers == 3:
#     print("Oy nomi: Mart. Kunlar soni: 31.")
# elif numbers == 4:
#     print("Oy nomi: Aprel. Kunlar soni: 30.")
# elif numbers == 5:
#     print("Oy nomi: May. Kunlar soni: 31.")
# elif numbers == 6:
#     print("Oy nomi: Iyun. Kunlar soni: 30.")
# elif numbers == 7:
#     print("Oy nomi: Iyul. Kunlar soni: 31.")
# elif numbers == 8:
#     print("Oy nomi: Avgust. Kunlar soni: 31.")
# elif numbers == 9:
#     print("Oy nomi: Sentyabr. Kunlar soni: 30.")
# elif numbers == 10:
#     print("Oy nomi: Aktyabr. Kunlar soni: 31.")
# elif numbers == 11:
#     print("Oy nomi: Nayabr. Kunlar soni: 30.")
# elif numbers == 12:
#     print("Oy nomi: Dekabr. Kunlar soni: 31.")
# else:
#     print("Faqat 1 dan 12 gacham bo'lgan sonlarni kiritishingiz mumkin!")

# 3.
# num1 = int(input("Birinchi sonni kiriting: "))
# num2 = int(input("Ikkinchi sonni kiriting: "))
# num3 = int(input("Uchinchi sonni kiriting: "))
#
# if num1 == num2 != num3:
#     print(f"1 va 2 sonlar teng 2ta son teng")
# elif num1 == num3 != num2:
#     print(f"1 va 3 sonlar teng 2ta son teng")
# elif num2 == num3 != num1:
#     print(f"2 va 3 sonlar teng 2ta son teng")
# elif num1 == num2 and num1 == num3 and num2 == num3:
#     print(f"3 ta sonlar teng")
# else:
#     print(f"sonlar teng emas")

# 4.
# son1 = int(input("Birinchi sonni kiriting: "))
# son2 = int(input("Ikkinchi sonni kiriting: "))
#
# if son2 * son1 > 1000:
#     print(son1 * son2)
# else:
#     print(son1 + son2)

# 5.
# num = int(input('Son kiriting: '))
#
# if num % 5 == 0:
#     print('Hello')
# else:
#     print("Bye")


# 6.
# year = int(input("Enter the year: "))
#
# if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#     print("Leap year")
# else:
#     print("It is not leap year")

# 7.
# parts = int(input("Parts: "))
# length = int(input("Length: "))
# width = int(input("Width: "))
#
# if length * width == parts:
#     if parts % length == 0 and parts % width == 0:
#         print("YES")
# else:
#     print("NO")
