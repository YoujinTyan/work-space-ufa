import tqdm
import time
from colorama import init
from art import tprint
from simple_term_menu import TerminalMenu
import tabulate
import models


body = []


def load_all_body():
  global body
  return body


def add_body(state):
  global body

  low_feed = ''
  for words in state:
    low_feed += state.lower()

  
  body.append(low_feed)


def verification(password):
  if password == "qwerty12345":
    return True
  return False


def get_sick():
  tmp = models.get_templates()[0]
  feeds = load_all_body()
  sick = []
  for feed in feeds:
    for word in tmp:
      if word == feed:
        sick.append(feeds)
        break
  return sick

def get_not_sick():
  tmp = models.get_templates()[1]
  feeds = load_all_body()
  not_sick = []
  for feed in feeds:
    for word in tmp:
      if word == feed:
        not_sick.append(feeds)
        break
  return not_sick

def menu_doc_choiser(name):
  if name == 'здоровые':
    feeds = get_not_sick()
    if len(feeds) > 0:
      print()
      for feed in feeds:
        print(feed, '\n\n')
    else:
        print("здоровых нет")


  elif name == "больные":
    feeds = get_sick()
    if len(feeds) > 0:
      print()
      for feed in feeds:
        print(feed, '\n\n')
    else:
      print("работы нет(((")

