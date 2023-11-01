# phonebook = {'Bobby': '87771232211'} # dict()
# dict()
# phonebook['Sandy'] = '1234567890'
# phonebook.update( {'key':'value'} )

# print(phonebook)
# phonebook['Bobby'] = True
# print(phonebook)

# for key in phonebook:
#   print(key, '-', phonebook[key])

##########################################################

# user = input(':::').lower()
# functions = {
#   'print': print,
#   'len': len,
# }

# function = functions[user]
# user_inp = input('data: ')

# function(user_inp)

# print('Длина строки:', function(user_inp) if user=="len" else len(user))

##########################################################

import requests

req = requests.get('https://jsonplaceholder.typicode.com/posts')
data = eval(req.text)
print(data)

# TODO: оформить 10 постов
# 
# 
# 1) Оформить вывод постов
# 2) Создать функции:
  # - добавление постов 
  # - удаление поста
  # - редактирование поста


"""
----------------------------------------------------------------------
Qui est esse

Est rerum tempore vitae\n
sequi sint nihil reprehenderit dolor beatae ea dolores neque\n
fugiat blanditiis voluptate porro vel nihil molestiae ut reiciendis\n
qui aperiam non debitis possimus qui neque nisi nulla.
----------------------------------------------------------------------
Qui est esse

Est rerum tempore vitae\n
sequi sint nihil reprehenderit dolor beatae ea dolores neque\n
fugiat blanditiis voluptate porro vel nihil molestiae ut reiciendis\n
qui aperiam non debitis possimus qui neque nisi nulla.
----------------------------------------------------------------------
...

"""

