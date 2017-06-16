"""
file: news.py 
author: Petri Lamminaho 
The news app's main program 
"""
from  console_view import View as Console
from find_ent import find_ent


def main():
    #print("Persons:",find_ent("Singers Tom Jones and Serj Tankian "))
    view = Console()
    while(True):
        view.show_main_menu()
if __name__ == '__main__':
    main()
