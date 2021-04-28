# Exercise 1: Convert Lists Into Dictionaries
# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]

# num = dict(zip(['ten', 'Twenty', 'Thirty'], [10, 20, 30]))
# print(num)


# Exercise 2 : Cinemax #2 :

# family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
# price = 0

# for age, name family.items():
#     if age <= 3:
#         price = 0
#         print(f'{name} pays {price}$')
#     elif age = > 3 and age = < 12:
#         price += 10
#     elif age >= 12:
#         price += 15
# print(f'{name} pays {price}$')


# Exercise 3: Zara


# brand = {
#     "name": "Zara",
#     "creation_date": 1975,
#     "creator_name": "Amancio Ortega Gaona",
#     "type_of_clothes": ["men", "women", "children", "home"],
#     "international_competitors": ["Gap", "H&M", "Benetton"],
#     "number_store": 7000,
#     "major_color": {"France": "blue", "Spain": "red", "US": ["pink", "green"]}
# }
# brand["number_store"] = 2

# for client in brand['type_of_clothes']:
#     print(f'the type of clients are {client}')
#     brand['country_creation'] = 'Spain'
#     print(brand)

# if 'international_competitors' in brand:
#     brand['international_competitors'].append('Desigual')
#     print(brand)
# else:
#     print('not in dictionary')

# del brand['creation_date']
# print(brand)

# last_competitor = brand['international_competitors'][-1]
# print(last_competitor)

# print(f"the major clothes' colors in the US are {brand['major_color']['US']}")
# print(len(brand))
# print(brand.keys)

# more_on_zara = {
#     'creation_date': 1975,
#     'number_stores': 10000
# }

# print(brand[number_store])

# Exercise 4: Disney Characters

# users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]

# disney_user_a = {users[i]: i for i in range(0, len(users))}
# print(disney_user_a)

# disney_user_b = dict(enumerate(users))
# print(disney_user_b)

# users = sorted(users)
# disney_user_c = {users[i]: i for i in range(0, len(users))}
# print(disney_user_c)

# for i_characters in users:
#     if 'i' in i_characters:
#         print(i_characters)

# disney_user_e = {users[i]: i for i in range(
#     0, len(users)) if 'M' or 'P' in users[i][0]}
# print(disney_user_e)

# for name in users:
#     if name[0] in ["M", "P"]:
#         print(name)

# for mp_characters in users:
#     if 'M' or 'P' in mp_characters[0]:
#         print(mp_characters)
