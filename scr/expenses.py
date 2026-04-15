import sys
import os
import json

DATA_FILE = "expenses.json"

def loadData():

#загрузить данные из json файла

    if not os.path.exists(DATA_FILE):
        return {"categories" : [], "expenses" : []}
    
    with open(DATA_FILE, "r", encoding="utf-8") as file:
        return json.load(file)
    
#   if not os.path.exists(DATA_FILE):               проверка на существование файла DATA_FILE (врзвращает true если файл есть и false если файла нету)
#   
#   return {"categories" : [], "expenses" : []}     создание словаря
#   пример:
#   {
#       "categories": [],
#       "expenses": []
#   }
#   
#   with open(DATA_FILE, "r", encoding="utf-8") as file:
#   "r"                     для чтения
#   encoding="utf-8"        для работы с русской раскладкой
#   
#   return json.load(file)
#   читает json данный из вайла и создает их в питон словарь со списками

def saveData(data):
    
#сохранить данные в json файл

    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=2, ensure_ascii=False)

#   with open(DATA_FILE, "w", encoding="utf-8") as file:    
#   "w"                     для записи
#   encoding="utf-8"        для работы с русской раскладкой
#   
#   json.dump(data, file, indent=2, ensure_ascii=False)
#   json.dump()             записывает в питон обьект в json файл
#   data                    то что записываем
#   file                    куда
#   indent=2                отступы для читаемости (2 - два пробела)
#   ensure_ascii=False      позволяет писать русские буквы в виде букв а не \u0435\u0441....

def addCategory(category):

#добавить категорию

    data = loadData()

    if category in data["categories"]:
        print(f"'{category}' already exists")
        return
    
    data["categories"].append(category)

    saveData(data)

    print(f"category '{category}' available")

#   data = loadData()                       загрузка текущих файлов (создает пустые если нету)
#   
#   if category in data["categories"]:      проверка - есть ли уже такая категория (если есть то return)
#   
#   data["categories"].append(category)     добавление новой категории в конец списка data["categories"] и .append() в конец
#   
#   saveData(data)                          сохраняет обновленные данные в файл
#   
#   print(f"category '{category}' available")
#   вывод при успехе успешно

def addExpense():

#добавить растрату

def listExpanses():

#вывод список расходов

def totalExpenses():

#вычисляет и выводит сумму расходов

def main():

#основная команда

    if len(sys.argv) < 2:
        print("directional input")
    #   неправильный ввод
        sys.exit()
    #   проверка на кол-во аргументов


    command = sys.argv[1]

    if command == "add-catt":
        if len(sys.argv) != 3:
            print("")

            return
        
        add_category(sys.argv[2])
    
    elif command == "add":
        if len(sys.argv) != 5:
            print("")

            return
        
        addExpense(sys.argv[2], sys.argv[3], sys.argv[4])

    elif command == "list":
        category = sys.argv[2] if len(sys.argv) > 2 else None

        listExpanses(category)

    elif command == "total":
        category = sys.argv[2] if len(sys.argv) > 2 else None

        total_expenses(category)

    else:
        print("unknown command: {command}")

#   len(sys.argv) < 2               проверка на количество аргументов
# 
#   coomand = sys.argv[1]           второй элемент из списка
# 
#   дальше идем по проверке ввода на заданые слова  -> add-catt add list total
# 
#   category = sys.argv[2] if len(sys.argv) > 2 else None
#   if len(sys.argv) > 2 else None          проверка на ввод третьего аргумента
#   если был совершен ввод третьего агрумента то присваиваем categoty этот аргумент
#   
#   ну и просто используем

main()
