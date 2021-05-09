# list1 = [5, 10, 15, 20, 25, 50, 20]

# wented_index = list1.index(20)
# list1[3] = 200
# print(list1)

# a_tuple = (10, 20, 30, 40)
# a, b, c, d = a_tuple
# print(c)

# number = int(input("Enter a number "))
# for num in range(1, 11):
#     print(number, 'x', num, '=', number*num)

# number = 1
# while number <= 10:
#     print(number)
#     number += 1


# user_word = input("Enter a word which contains 10 characters : ")
# letter_num = 10
# def triangle_name(user_word):
#     counter = 0
#     constructed = ""
#     if letter_num == len(user_word):
#         for letter in user_word:
#             constructed += letters
#             print(constructed)
#             counter +=1
#             if counter == 10:
#                 rand_word = list(user_word)
#                 # [char for char in rand_word]
#                 random.shuffle(rand_word)
#                 shuffled = ''.join(rand_word)
#                 print(shuffled)
#     else:
#         print("not enough letters")
# triangle_name(user_word)


# Using A Flag
# active = True

# while active:
#     city = input(
#         "Please enter the name of a city you have visited (enter 'quit' when you are finished): ")
#     if city == 'quit':
#         active = False
#     elif city == 'leave me alone':
#         active = False
#     elif city == 'stop':
#         active = False
#     else:
#         print("I'd love to go to", city)

# print("Goodbye !")


# secret_number = 4

# while True:
#     user_number = input('Guess the secret number: ')
#     if int(user_number) == secret_number:
#         print('Congrats! You win!')
#         break
#     else:
#         print('Wrong guess...')
