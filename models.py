from simple_term_menu import TerminalMenu
from art import tprint


sick = [
	"шизофрения",
	"галюцинации",
	"звуки",
]
not_sick = ["здоров","впорядке","жалоб"]


def get_main_menu():
  main_menu = ["врач","посититель"]

  print("Кто ты?")
  menu = TerminalMenu(main_menu)
  # i = 0
  i = menu.show()
  return main_menu[i]


def start():
  tprint("welcome")
  tprint("to the")
  tprint("durka")


def get_doc_menu():
  doc_menu = ["больные",
             "здоровые",
             "все жалобы",
             "выход"]

  menu = TerminalMenu(doc_menu)
  i = 0
  i = menu.show()
	
  return doc_menu[i]


def show_body(all_body):
  for body in all_body:
    print(body)


def get_templates():
  global sick, not_sick
  return sick, not_sick