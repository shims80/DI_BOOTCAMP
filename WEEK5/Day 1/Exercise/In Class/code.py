# class Point():
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y


# # create an instance of the class
# p = Point(3, 4)

# # access the attributes
# print("p.x is:", p.x)
# print("p.y is:", p.y)


# class Robot():
#     def __init__(self, name, color, weight):
#         self.name = name
#         self.color = color
#         self.weight = weight

#     def introduce_self(self):
#         print(
#             f'hey im the robot {self.name}, i am painted {self.color} and weigh {self.weight}')

#     def rename(self, new_name):
#         self.name = new_name
#         print('my name ')


# r1 = Robot('Tom', 'Red', 30)
# r2 = Robot('Jerry', 'Blue', 40)
# r1.introduce_self()
# r2.introduce_self()


# class Person():
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def show_details(self):
#         print("Hello my name is " + self.name)

#     def modify_name(self, name='john'):
#         self.name = name


# first_person = Person("John", 36)
# first_person.show_details()
# first_person.modify_name('shimon')
# first_person.show_details()

# Exercise 9 : Tall Enough To Ride A Roller Coaster

# user = int(input("Enter height"))
# if user >= 145:
#     print("ok to ride")
# else:
#     print("not ok to ride")
