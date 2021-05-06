# http://learn.di-learning.com/courses/collection/18/course/12/section/53/chapter/231

# Exercise 1 : Favorite Numbers:

# my_fav_numbers = {5, 7, 9, 20, 41, 42}
# my_fav_numbers.add(4)
# my_fav_numbers.add(8)
# my_fav_numbers.pop()
# friend_fav_numbers = {10, 5, 12, 22}
# our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
# print(our_fav_numbers)

# Exercise 2: Tuple

# Given a tuple which value is integers, is it possible to add more integers to the tuple?
# answer: no you can't add number to tuple as its immutable


# Exercise 3: Print A Range Of Numbers

# for i in range(1, 21):
#     print(i)


# Exercise 4: Floats

# Recap – What is a float? What is the difference between an integer and a float?
# Floats represent numbers that are written with a decimal point
# and integers is a round number

# Can you think of another way to generate a sequence of floats?
# by using a for loop to generat a sequence of floats

# for i in range(1, 5):
#     print(i + 0.5)
#     print(i + 1)


# Exercise 5: Shopping List

# basket = ["Banana", "Apples", "Oranges", "Blueberries"]
# basket.remove("Banana")
# basket.remove("Blueberries")
# basket.append("Kiwi")
# basket.append("Apples")
# print(basket.count("Apples"))
# basket.clear()
# print(basket)

# Exercise 6 : Loop

# my_name = "shimon"
# user_names = input("Enter your name: ")
# while user_names != my_name:
#     user_names = input("Enter your name ")


# Exercise 7

# user_list = [1, 3, 4, 5, 6, 7, 8, 9]
# for i in user_list:
#     if user_list.index(i) % 2 == 0:
#         print(i)


# Exercise 8

# for i in range(1500, 2501):
#     if i % 5 == 0 and i % 7 == 0:
#         print(i)

# Exercise 9: Favorite Fruits
# user = input("please enter fruits ").split(" ")
# fav_fruits = input("Enter a fruit ")
# if fav_fruits in user:
#     print("You chose one of your favorite fruits! Enjoy ")
# else:
#     print("You chose a new fruit. I hope you enjoy")

# Exercise 9: Favorite Fruits

# user = input("Please enter your favorit fruits with space btw each fruit ")
# convarting_str_to_a_list = list(user)
# user = input("enter a fruit ")
# if user in convarting_str_to_a_list:
#     print("you chose one of your favorit fruits! enjoy! ")
# else:
#     print("You chose a new fruit. I hope you enjoy")


# Exercise 10: Who Ordered A Pizza ?
# print("topping available :onion, mushrooms,papers,corn,green olives,black olives")
# topping = input("Please type a pizza topping (type 'quit' to stop): ")
# all_topping = []
# price = 10
# while topping != "quit":
#     print(f'{topping} has being added to your pizza.')
#     price += 2.5
#     all_topping.append(topping)
#     topping = input("Please type a pizza topping (type 'quit' to stop): ")
#
# print(f'your topping are :\n {all_topping}')
# print(f'your price is {price}')

# Exercise 11: Cinemax:

# age = int(input("what is ur age ? (type '0' to stop)"))
# sum = 0
# while age != 0:
#     ticket = input("Please type 1 if you wants a ticket or 0 if he doesn't")
#     if ticket == "1":
#         if age > 12:
#             sum += 15
#         elif age > 3:
#             sum += 10
#     age = int(input("please type the age(type'0' to stop)"))
# print(f"ticket price is{sum}")
# age = int(input("please type the age(type '0' to stop):"))
# teens = []
# while age != 0:
#     name = input("please typr your name")
#     if age > 16 and age < 21:
#         teens.append(name)
#     age = int(input("please type the age(type '0' to stop)"))
# print(f"the teens are :{teens}")


# Exercise 12: Who Is Under 16?
# users = ("moshe", "shimon", "yossi", "david")
# for i in users
# if i < 17 and i

# Exercise 13

# sandwich_orders = ["tuna", "chesse", "falafel"]
# finished_sandwiches = []
# new_send_list = send_list.copy()
# print(f'new_send_list)

# d = "ddar astronaut. pldase, stop drasing md!"
# new_d = d[0] + d[1:].replace(replacement, 'e')
