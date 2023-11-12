import models as mod
import controller as ctrl
import time
import tabulate
from simple_term_menu import TerminalMenu



mod.start()


while True:
  break_menu = False

  
  print("\n")
  
  
  if mod.get_main_menu() == "врач":
    password = input("Введите пароль:")
    if ctrl.verification(password) is True:
      while break_menu == False:
        item = mod.get_doc_menu()
        break_menu = ctrl.menu_doc_choiser(item)
    else:
      print("xexe")
      
  else:
    print("напишите Имя , Фамилия , Состояние")
    messeg = input()
    ctrl.add_body(messeg)

