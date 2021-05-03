# class Circle:
#     color = "red"


# class NewCircle(Circle):
#     color = "blue"


# nc = NewCircle
# print(nc.color)


# class Circle:
#     def __init__(self, diameter):
#         self.diameter = diameter

#     def grow(self, factor=2):
#         """grows the circle's diameter by factor"""
#         self.diameter = self.diameter * factor


# class NewCircle(Circle):
#     def grow(self, factor=2):
#         """grows the area by factor..."""
#         self.diameter = (self.diameter * factor * 2)


# nc = NewCircle(1)
# print(nc.diameter)

# nc.grow()

# print(nc.diameter)

#Exercise On Inheritance And Composition: Door Class
#http://learn.di-learning.com/courses/collection/18/course/13/section/62/chapter/309

class Door():
    def __init__(self, is_opened):
        self.is_opened = is_opened

    def open_door(self):
        print('door has been opened')
        self.is_opened = True

    def close_door(self):
        print('door has been closed')
        self.is_opened = False


class BlockedDoor(Door):
    def open_door(self):
        print('door is blocked and cannot be opened or closed')

    def close_door(self):
        self.open_door()
