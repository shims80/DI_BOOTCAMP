dob = input("Please input your birthdate: (format: DD/MM/YYYY)")
day, month, year = list(map(int, dob.split("/")))
currentdate = list(map(int, "27/4/2021".split("/")))
age = currentdate[2] - year
birthday_flag = False
if month >= currentdate[1]:
    if currentdate[0] > day:
        age -= 1
if month == currentdate[1] and day == currentdate[0]:
    print("happy birthday!!!")
    birthday_flag = True
print_string = f"you are {age} years old"
if birthday_flag:
    print_string += " today"
print(print_string)
candles = int(age / 10)
candle_string = "i" * candles
while len(candle_string) < 10:
    candle_string += "_"
    candle_string = "_" + candle_string
if len(candle_string) % 2 == 1:
    candle_string = candle_string[0:-1]
cake = f"""
  _{candle_string}_
__|          |__
|Happy Birthday|
|______________|
"""
print(cake)

