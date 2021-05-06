import requests


def get_categories(request_url='https://api.chucknorris.io/jokes/categories'):
    response = requests.get(request_url)
    print('getting categories')
    if response.status_code == 200:
        return response.json()
    else:
        print('bad request or server failure')


def get_joke_by_category():
    categories = get_categories()
    print('got categories about to ask user for input')
    user_choice = input('pick a category:\n' + '\n'.join(categories))
    while user_choice not in categories:
        print('bad choice try again')
        user_choice = input('pick a category' + categories)
    url = f'https://api.chucknorris.io/jokes/random?category={user_choice}'
    response = requests.get(url)
    if response.status_code == 200:
        print(response.json()['value'])


get_joke_by_category()
