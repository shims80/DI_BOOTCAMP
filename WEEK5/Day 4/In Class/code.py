with open('test.txt', mode='w') as my_file:
    text = my_file.write('moshe')

    # print(my_file.readlines())
    print(text)


# with open('file.json', 'r') as f:
#     family = json.load(f)
# for child in family['children']:
#     print(
#         f'{family["firstName"]}\'s child {child["firstName"]} is {child["age"]} years old')
#     child['favorite_color'] = random.choice(['blue', 'yellow', 'green'])
# with open('file.json', 'w') as f:
#     json.dump(family, f, indent=2)
# print(family)
