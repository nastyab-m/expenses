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
#   читает json данныe из файла и создает его (если он отсутствует) в питон словарь со списками

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

def addExpense(category, name, cost):

#добавить растрату

    try:
        cost = float(cost)

        if cost <= 0:
            print("only positive")

            return
    except ValueError:
        print("only numbers")

        return
    
    data = loadData()

    if category not in data["categories"]:
        print(f"'{category}' not exepts")

        return
    
    expense = {
        "category": category,"name": name, "cost": cost
    }

    data["expenses"].append(expense)

    saveData(data)

    print("expense added")

#   добавляем растрату
#   try: exept:                             try блок обработки ошибок -> если ошибка то exept
#   cost = float(cost)                      float() преобразовавыает обычное число в число с плавающей точкой
#   if cost <= 0:                           провека на положительные
#   except ValueError:                      если ввод будет не того типа то выполнение идет сюда
#   
#   data = loadData()                       загружает текущие данные из файла
#   
#   if category not in data["categories"]:  проверка на отсутствие категорий в списке уже существующих категорий
#   
#   expense = {"cost": cost, "category": category, "name": name}
#   создание словаря расхода (создание словаряс тремя ключами)
#   результат:
#       {"cost": 12.0, "category": "еда", "name": "ужин"}
#   
#   data["expenses"].append(expense)        добавляет в "expenses" новую растрату expense
#   
#   saveData(data)                          сохранение обновленных данных

def listExpenses(category=None):

#вывод список расходов

    data = loadData()

    expenses = data["expenses"]

    if category:
        expenses = [e for e in expenses if e["category"] == category]

        if not expenses:
            print(f"'{category}' not found")

            return
        
    if not expenses:
        print("no expenses")

        return
    
    print("expenses:")
    print("-" * 60)

    for i, expense in enumerate(expenses, start=1):
        print(f"{i}. {expense['name']} - {expense['cost']} ({expense['category']})")

        print("-" * 60)

#   category=None                    аргумент по умолчанию (если не передать то будет None) 
#   пример:
#       listExpenses()          -> category = None
#       listExpenses("еда")     -> category = "еда"
#   
#   data = loadData()                загрузка данных из файла
#   expenses = data["expenses"]      получение списка расходов из данных
#   if category:                     проверка на наличие категории (если category не None то выполняется)
#
#   expenses = [e for e in expenses if e["category"] == category]
#   генератор списка (создает новый список из расходов которые принадлежат к заданной категории)
#   for e in expenses                перебирает все расходы в списке expenses
#   if e["category"] == category     проверяет принадлежность категории каждого расхода к заданной категории
#   
#   if not expenses:                 проверка на пустой список расходов (если нету расходов то выполняется)
#   print(f"'{category}' not found") вывод при отсутствии расходов в категории
#   if not expenses:                 проверка на общее отсутствие расходов (если нету расходов то выполняется)
#   
#   print("-" * 60)                  вывод разделительной линии из 60 символов "-"
#   
#   for i, expense in enumerate(expenses, start=1):
#   enumerate()                      позволяет получить индекс и элемент из списка одновременно
#   
#   print(f"{i}. {expense['name']} - {expense['cost']} ({expense['category']})") 
#   пример вывода:
#       1. Обед - 100.0 (Еда)
#       2. Кино - 200.0 (Развлечения)

def totalExpenses(category=None):

#вычисляет и выводит сумму расходов

    data = loadData()
    expenses = data["expenses"]

    if category:
        expenses = [e for e in expenses if e["category"] == category]

        if not expenses:
            print(f"'{category}' not found")

            return
        
    total = sum(e["cost"] for e in expenses)

    if category:
        print(f"total for '{category}': {total}")

    else:
        print(f"total: {total}")

#   data = loadData()                загрузка данных из файла
#   expenses = data["expenses"]      получение списка расходов из данных
#   
#   if category:                     проверка на наличие категории (если category не None то выполняется)
#   expenses = [e for e in expenses if e["category"] == category]
#   генератор списка (создает новый список из расходов которые принадлежат к заданной категории)
#   for e in expenses                перебирает все расходы в списке expenses
#   if e["category"] == category     проверяет принадлежность категории каждого расхода к заданной категории
#   
#   if not expenses:                 проверка на пустой список расходов (если нету расходов то выполняется)
#   print(f"'{category}' not found") вывод при отсутствии расходов в категории
#   total = sum(e["cost"] for e in expenses)
#   sum()                            функция для вычисления суммы
#   e["cost"] for e in expenses      генератор для получения стоимости каждого расхода из списка расходов
#
#   if category:                     проверка на наличие категории (если category не None то выполняется)
#   print(f"total for '{category}': {total}") 
#   вывод при наличии категории
#   else:                            вывод при отсутствии категории
#   print(f"total: {total}")

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
            print("error: 'add-catt' requires exactly one argument")

            return
        
        addCategory(sys.argv[2])
    
    elif command == "add":
        if len(sys.argv) != 5:
            print("error: 'add' requires exactly three arguments")

            return
        
        addExpense(sys.argv[2], sys.argv[3], sys.argv[4])

    elif command == "list":
        category = sys.argv[2] if len(sys.argv) > 2 else None

        listExpenses(category)

    elif command == "total":
        category = sys.argv[2] if len(sys.argv) > 2 else None

        totalExpenses(category)

    else:
        print(f"unknown command: {command}")

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
