import pandas as pd
from enum import Enum
import os
import platform

makers = []
class Options(Enum):
    MAKERS = 1
    YEARS = 2
    MODELS = 3

def searchItem(list_to_search, item_to_search, collumName):
   try:
    if item_to_search.isdigit:
            
            item_to_search = int(item_to_search)
            print(f"Searching....{list_to_search[item_to_search]}")
            count = df[df[collumName] == list_to_search[item_to_search]].shape[0] 
            print(f"Found: {count}")

            filtered = df[df[collumName] == list_to_search[item_to_search]]
            print(filtered)
    else:
        print("Invalid input")
   except ValueError:
      print("Invalid input")
   except IndexError:
      print("Out of range!")
def clear_terminal():
   
   
   system = platform.system().lower()
   if system == 'windows':
        os.system('cls')
   else:
        os.system('clear')
    
if __name__ == "__main__":
    df = pd.read_csv('cars.csv')

    makers = list(df['make'].unique())
    years = list(df['year'].unique())
    models = list(df['model'].unique())

    while True:
        for option in Options:
            print(f"{option.value} - {option.name}")
        user_selection = input("Select an option: ")
        clear_terminal()
        try:
            if user_selection.isdigit():
                user_selection = Options(int(user_selection))
            else:
                print("Invalid option!")
        except ValueError:
           print("Out of range!")
        
        if user_selection == Options.MAKERS:
            print("MAKERS:")
            print("---------------------------------------------")
            for index, i in enumerate(makers):
             print(f"{index} - {i}")

            maker_to_search = input("Search maker (by index): ")
            searchItem(makers, maker_to_search, 'make')

        elif user_selection == Options.YEARS:
            print("YEARS:")
            print("---------------------------------------------")
            for index, i in enumerate(years):
             print(f"{index} - {i}")

            year_to_search = input("Select a year to search (by index): ")
            searchItem(years, year_to_search, 'year')

        elif user_selection == Options.MODELS:
            print("MODELS:")
            print("---------------------------------------------")
            for index, i in enumerate(models):
             print(f"{index} - {i}")

            model_to_search = input("Select a model to search (by index): ")
            searchItem(models, model_to_search, 'model')
    
    

    