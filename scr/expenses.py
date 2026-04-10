import sys

DATA_FILE = "expenses.json"

def loadData():

#загрузить данные из json файла

def saveData():

#сохранить данные в json файл

def addCategory():

#добавить категорию

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


    coomand = sys.argv[1]

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
