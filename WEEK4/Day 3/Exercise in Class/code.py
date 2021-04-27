# sampleDict = {
#     "class": {"student": {"name": "Mike", "marks": {"physics": 70, "history": 80}}}
# }
# sampleDict["class"]["student"]["marks"]["history"]

# for key, value in person_dict.items():
#     print(f'{key}:{value}')





#Building dictionaries with zip and multiple lists

# names = ['Rick', 'Morty', 'Summer']
# grades = [10,20,30,40,50]
# ages = [15,25,40,60,70,30]
# print(list(zip(names, grades, ages)))
# people = []
# for name, grade, age in zip(names, grades, ages):
#     people.append({'name':name, 'grade':grade, 'age':age})
# print(people)
            

#list comprehension
# letters = 'abcde'
# output = [letter * 3 for letter in letters]
# print(output)
# # no list comprehension
# letters = 'fghijkl'
# output = []
# for letter in letters:
#     output.append(letter * 3)
# print(output)
