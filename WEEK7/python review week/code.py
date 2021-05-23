# exrcise 1

# import random
# import threading

# color = ["red", "green", "yellow"]

# color = random.choice(color)

# if color == "red":
#     print("stop")
# elif color == "green":
#     print("go")
# else:
#     print("get ready")

# exrcise 2

# import threading
# counter = 0


# def traffic_light():
#     colors = ['green', 'yellow', 'red']
#     global counter
#     print(colors[counter])
#     counter += 1
#     if counter == 3:
#         counter = 0


# def set_interval(func, sec):
#     def func_wrapper():
#         set_interval(func, sec)
#         func()
#     t = threading.Timer(sec, func_wrapper)
#     t.start()
#     return t


# set_interval(traffic_light, 5.0)

# exrcise 3

# for i in range(1000, 3001,):
#     if i % 7 == 0:
#         print(i)

# exrcise 4

# loop through a list

# names = ['chaim', 'shimon', 'lila', 'ronny',
#          'micheal', 'jonathan', 'eliyahu', 'shmuel']


# # names.sort
# for i in names:
#     for x in i:
#         if 'a' in x:
#             print(i)

# exrcise 5

# list_1 = ['chaim', 1, 'shimon', 2, 'lila', 4, 'ronny', 5,
#           'micheal', 6, 'jonathan', 7, 'eliyahu', 8, 'shmuel', 9]

# stringList = []
# numberList = []


# for i in list_1:
#     if isinstance(i, int):
#         numberList.append(i)
#     else:
#         stringList.append(i)
# print(f'nums: {numberList}, string: {stringList}')

# exrcise 6

# counter = 0
# while counter != 21:
#     print(f'{counter}: still runnning')
#     counter += 1
# print('complete')


# Exercise 3: Print :A Range Of Numbers
# Instructions
# Use a for loop to print all numbers from 1 to 20, inclusive.

# for i in range(21):
#     print(i)


# Exercise 6: Loop
# Instructions
# Write a while loop that will continuously ask the user for their name, unless the input is
# equal to your name.

# my_name = 'shimon'
# user = input("what is ur name")
# while user != my_name:
#     user = input("what is ur name")

# Exercise 7
# Instructions
# Given a list, use a loop to print out every
# element which has an even index.

# user_list = [1, 3, 4, 5, 6, 7, 8, 9]
# for i in user_list:
#     if user_list.index(i) % 2 == 0:
#         print(i)

# Exercise 8
# Instructions
# Create a loop that goes from 1500 to 2500
# and prints all multiples of 5 and 7.

# for i in range(1500, 2501):
#     if i % 5 == 0 and i % 7 == 0:
#         print(i)


# Exercise 9: Favorite Fruits
# Instructions
# Ask the user to input their favorite fruit(s)(one or several fruits).
# Hint: Use the built in input method. Ask the user to separate the fruits with a single space, eg. "apple mango cherry".
# Store the favorite fruit(s) in a list(convert the string of words into a list of words).
# Now that we have a list of fruits, ask the user to input a name of any fruit.
# If the user’s input is in the favorite fruits list, print “You chose one of your favorite fruits! Enjoy!”.
# If the user’s input is NOT in the list, print, “You chose a new fruit. I hope you enjoy”.

# user = input("please enter your favorite fruit").split(" ")
# favorite_fruit = user
# user = input("enter any fruit ")
# if user in favorite_fruit:
#     print("same fruit")
# else:
#     print("not the same fruit ")


# Exercise 10: Who Ordered A Pizza ?
# Instructions
# Write a loop that asks a user to enter a series of pizza toppings,
# when the user inputs ‘quit’ stop asking for toppings.
# As they enter each topping, print a message saying
# you’ll add that topping to their pizza.
# Upon exiting the loop print all the toppings
# on the pizza pie and what the total price is (10 + 2.5 for each topping).

# print("topping available :onion, mushrooms,papers,corn,green olives,black olives")

# topping = input("Please type a pizza topping (type 'quit' to stop): ")

# all_topping = []
# price = 10

# while topping != "quit":
#     print(f'{topping} has being added to ur pizza ')
#     price += 2.5
#     all_topping.append(topping)
#     topping = input("Please type a pizza topping (type 'quit' to stop): ")

# print(f'your topping are :\n {all_topping}')
# print(f'your price is {price}')


# Exercise 11: Cinemax
# Instructions
# A movie theater charges different ticket prices
# depending on a person’s age.
# if a person is under the age of 3, the ticket is free.
# if they are between 3 and 12, the ticket is $10.
# if they are over the age of 12, the ticket is $15.
# Ask a family the age of each person who wants a ticket.
# Store the total cost of all the family’s tickets and print it out.
# A group of teenagers are coming to your movie theater and want
# to watch a movie that is restricted for people
# between the ages of 16 and 21.
# Write a program that asks every user for their age,
# and prints a list of the teens who are permitted to watch the movie.

# age = int(input("please enter ur age (type '0' to stop) "))
# sum = 0

# while age != 0:
#     if age > 12:
#         sum += 15
#     elif age > 3:
#         sum += 10


# Exercise 12: Who Is Under 16?
# Instructions
# Given a list of names, write a program that asks every user
# for their age, if they are less than 16 years
# old remove them from the list.
# At the end, print the final list.

# names = ['chaim', 'shimon', 'lila', 'ronny',
#          'micheal', 'jonathan', 'eliyahu', 'shmuel']

# allowed_names = []
# for name in names:
#     age = int(input(f'{name} how old are you ? '))
#     if age > 16:
#         allowed_names.append(name)
# print(allowed_names)


# Exercise 13
# Instructions
# Make a list called sandwich_orders and fill it with
# the names of various sandwiches .
# Then make an empty list called finished_sandwiches.
# As each sandwich is made, move it to the list of finished sandwiches.
# After all the sandwiches have been made,
# print a message listing each sandwich that was made,
# such as I made your tuna sandwich.


# sandwich_orders = ['burger', 'cheese', 'salami']
# finished_sandwiches = []
# for sandwich in sandwich_orders:
#     finished_sandwiches.append
#     print(f'{sandwich} was just made ')


# *args = tuple
# **kargs = dictionary


# class Vehicle:
#     def __init__(self, vehicle_type):
#         self.vehicle_type = vehicle_type
#         self.parts = []

#     def tires(self, amount):
#         amount_of_tires = f'{amount} tires'
#         self.parts.append(amount_of_tires)

#     def body(self):
#         if self.vehicle_type == 'car':
#             self.parts.append('car body')
#         elif self.vehicle_type == 'truck':
#             self.parts.append('truck body')
#         elif self.vehicle_type == 'motorcycle':
#             self.parts.append('motorcycle body')
#         elif self.vehicle_type == 'plane':
#             self.parts.append('plane body')

#     def engine(self):
#         if self.vehicle_type == 'car':
#             self.parts.append('car engine')
#         elif self.vehicle_type == 'truck':
#             self.parts.append('truck engine')
#         elif self.vehicle_type == 'motorcycle':
#             self.parts.append('motorcycle engine')
#         elif self.vehicle_type == 'plane':
#             self.parts.append('plane engine')

#     def front_lights(self, amount):
#         amount_of_light = f'{amount} lights'
#         self.parts.append(amount_of_light)

#     def remove_part(self,par_to_remove):
#         self.parts.remove(par_to_remove)

#     def display(self):
#         print(f'Parts needed to build your {self.vehicle_type}')
#         for part in self.parts:
#             print(f'{self.parts.index(part) + 1}: {part}')

#     def __repr__(self):
#         return f'type: {self.vehicle_type} parts: {self.parts}'


# v1 = Vehicle('car')
# v2 = Vehicle('motorcycle')
# v3 = Vehicle('plane')


# create a class called cat which has 3 methods called eat jump and play
# then create a class of a specific type of cat which has inherits
# from cat and has its own additional methods(2)
# instanciate with a name and color
# instanciate with fur type


# class Cat:
#     def __init__(self, name, color):
#         self.name = name
#         self.color = color

#     def eat(self):
#         print(f'{self.name} eating only fish&chips !')

#     def jump(self):
#         print(f'whene {self.name} jumps all we see is {self.color}')

#     def play(self):
#         print(f'{self.name} is playing around')

#     def __repr__(self):
#         return self.name


# class Persian(Cat):
#     def __init__(self, name, color, fur, height):
#         super().__init__(name, color)
#         self.fur = fur
#         self.height = height

#     def jumping_height(self, num):
#         print(f'{self.name} jumps {self.height * num} cm high')


# class Dog:
#     def __init__(self, name, color, ):
#         self.name = name
#         self.color = color
#         self.items = []
#         self.bread = ''
#         # if self.bread == 'Dog':
#         #     self.bread.append(Dog)

#     def dog_hous(self):
#         self.items.append('dog_hous')

#     def dog_bread(self, bread):
#         self.bread = bread

#     def __repr__(self):
#         return self.name


# c1 = Cat('mizi', 'pink')
# spc = Persian('pizi', 'blue', 'curly', 30)
# dog1 = Dog('leo', 'white')


# Exercise 3: Restaurant Menu Manager
# Instructions
# The purpose of this exercise is to create a restaurant menu.
# The code will allow a manager to add and delete dishes.
# Create a python file called menu_manager.py.
# Create a class called MenuManager.
# Create a method __init__ that instantiates an attribute called menu.
# The menu attributes value will be all the current dishes(list of
# dictionaries). Each dish will be stored in a dictionary where the
# keys are name, price, spice level and gluten
# index(which value is a boolean).


# menu = [
#     {
#         'name': 'Soup',
#         'price': 10,
#         'spice_level': 'B',
#         'gluten_index': False
#     },
#     {
#         'name': 'Hamburger',
#         'price': 15,
#         'spice_level': 'A',
#         'gluten_index': True
#     },
#     {
#         'name': 'Salad',
#         'price': 18,
#         'spice_level': 'A',
#         'gluten_index': False
#     },
#     {
#         'name': 'French fries',
#         'price': 5,
#         'spice_level': 'C',
#         'gluten_index': False
#     },
#     {
#         'name': 'Beef bourguignon',
#         'price': 25,
#         'spice_level': 'B',
#         'gluten_index': True
#     },
# ]


# class MenuManager:
#     def __init__(self, menu):
#         self.menu = menu

#     def add_item(self, **new_item):
#         self.menu.append(new_item)

#     def update_item(self, **item_to_update):
#         for item in self.menu:
#             if item_to_update['name'] == item['name']:
#                 item['price'] = item_to_update['price']
#                 item['spice_level'] = item_to_update['spice_level']
#                 item['gluten_index'] = item_to_update['gluten_index']
#                 return
#         print('The item you want to update does not exist.')

#     def remove_item(self, name):
#         for item in self.menu:
#             if item['name'] == name:
#                 self.menu.pop(self.menu.index(item))
#                 return
#         print('The item you want to remove does not exist')

#     def display_menu(self):
#         for item in self.menu:
#             print(f'{self.menu.index(item) + 1}: {item}')


# m1 = MenuManager(menu)


# class Phone:
#     def __init__(self, phone_number, full_name):
#         self.phone_number = phone_number
#         self.full_name = full_name
#         self.call_history = []
#         self.messages = []
#         self.contacts = []

#     def call(self, other_phone_number, caller):
#         if caller:
#             for contact in self.contacts:
#                 if contact['phone_number'] == other_phone_number:
#                     call_info = f'{self.full_name} called {contact["full_name"]}'
#                     self.call_history.append(call_info)
#                     print(call_info)
#                     return
#             call_info = f'{self.full_name} called {other_phone_number}'
#             self.call_history.append(call_info)
#             print(call_info)
#         else:
#             for contact in self.contacts:
#                 if contact['phone_number'] == other_phone_number:
#                     call_info = f'{contact["full_name"]} called {self.full_name}'
#                     self.call_history.append(call_info)
#                     print(call_info)
#                     return
#             call_info = f'{other_phone_number} called {self.full_name}'
#             self.call_history.append(call_info)
#             print(call_info)

#     def show_call_history(self):
#         for call in self.call_history:
#             print(f'{self.call_history.index(call) + 1}: {call}')

#     def send_message(self, **message_info):
#         self.messages.append(message_info)

#     def show_messages(self):
#         for message in self.messages:
#             print(f'{self.messages.index(message) + 1}: {message}')

#     def show_outgoing_messages(self):
#         counter = 1
#         for message in self.messages:
#             if message['sent_from'] == self.phone_number:
#                 print(f'{counter}: {message}')
#                 counter += 1

#     def show_incoming_messages(self):
#         counter = 1
#         for message in self.messages:
#             if message['to'] == self.phone_number:
#                 print(f'{counter}: {message}')
#                 counter += 1

#     def add_contact(self, **contact_info):
#         self.contacts.append(contact_info)

#     def __repr__(self):
#         return self.phone_number


# p1 = Phone('123456789', 'chaim wiesner')


# class Farm:
#     def __init__(self, farm_name):
#         self.farm_name = farm_name
#         self.animals = []

#     def add_animal(self, animal, amount=1):
#         animal_details = {
#             'animal': animal,
#             'amount': amount
#         }
#         for animal_info in self.animals:
#             if animal_info['animal'] == animal:
#                 animal_info['amount'] += amount
#                 return
#         self.animals.append(animal_details)

#     def get_info(self):
#         print(f'{self.farm_name}\'s farm ')
#         for animal_info in self.animals:
#             print(f'{animal_info["animal"]} : {animal_info["amount"]}')


# f1 = Farm('Macdonald')



# day = int(input("Input birthday: "))
# month = input("please enter the month of your birth (example: march): ")
# if month == 'december':
#     astro_sign = 'Sagittarius' if (day < 22) else 'capricorn'
# elif month == 'january':
#     astro_sign = 'Capricorn' if (day < 20) else 'aquarius'
# elif month == 'february':
#     astro_sign = 'Aquarius' if (day < 19) else 'pisces'
# elif month == 'march':
#     astro_sign = 'Pisces' if (day < 21) else 'aries'
# elif month == 'april':
#     astro_sign = 'Aries' if (day < 20) else 'taurus'
# elif month == 'may':
#     astro_sign = 'Taurus' if (day < 21) else 'gemini'
# elif month == 'june':
#     astro_sign = 'Gemini' if (day < 21) else 'cancer'
# elif month == 'july':
#     astro_sign = 'Cancer' if (day < 23) else 'leo'
# elif month == 'august':
#     astro_sign = 'Leo' if (day < 23) else 'virgo'
# elif month == 'september':
#     astro_sign = 'Virgo' if (day < 23) else 'libra'
# elif month == 'october':
#     astro_sign = 'Libra' if (day < 23) else 'scorpio'
# elif month == 'november':
#     astro_sign = 'scorpio' if (day < 22) else 'sagittarius'
# print("Your Astrological sign is :", astro_sign)










