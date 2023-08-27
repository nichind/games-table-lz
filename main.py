import sqlite3
from utils.consoleoperations import *
from utils.sqbase import database
from utils.liveval import *

if __name__ == '__main__':
    db = database(getconfig()['folders']['games'])

    try:
        games = db.select_data('games')
    except sqlite3.OperationalError:
        print('Таблица не была найдена, создана новая.')
        games = db.create_table('games', 'name, studio, year')

    print("""Консольное приложение, представляющее собой систему управления базой данных игр.\n@nichind""")

    while True:

        print('1: Добавить игру\n2: Поиск игры\n3: Удалить игру\n4: Редактирование данных о игре\n5: Вывод списка всех игр\n6: Закрыть программу')


        try:
            to = int(input('Действие: '))
            if to == 6: exit('finish')
            if isvalid(to): operation(db, to)
        except Exception as e: print(e)

