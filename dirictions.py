import requests

req = requests.get('https://jsonplaceholder.typicode.com/posts')
data = eval(req.text)

def pnt_hyphen():
    for i in range(35):
        print("-", end="")
    print("\n")

# TODO: оформить 10 постов
# 
# 
# 1 Оформить вывод постов
# 2 Создать функции:
  # - добавление постов 
  # - удаление поста
  # - редактирование поста




def show_post():
    global data
    pnt_hyphen()
    for i in range(10):
        print(data[i]["title"].capitalize() ,end='\n\n')
        print(data[i]["body"].capitalize() , end = "\n\n")
        pnt_hyphen()


def delete_post():
    global data
    number_post = int(input())
    data.pop(number_post - 1)

def create_post():
    global data
    title = input()
    body = input()
    phone = {}
    phone['title'] = title
    phone['body'] = body
    data = data + [phone]

def change_post():
    global data
    number_post = int(input())
    title = input()
    body = input()
    phone = {}
    phone['title'] = title
    phone['body'] = body
    data[number_post - 1] = phone




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