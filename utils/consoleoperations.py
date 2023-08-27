from utils.sqbase import database
from utils.liveval import *

def operation(database, num: int) -> bool:
    if num == 1:
        print('(cancel) для отмены')
        while True:
            name = str(input('Название игры: '))
            if name == 'cancel': return
            if len(name) >= 2: break
            print('Некорректное название игры!')

        while True:
            studio = str(input('Разработчик игры: '))
            if studio == 'cancel': return
            if len(studio) >= 2: break
            print('Некорректный разработчик игры!')

        while True:
            year = str(input('Год выхода игры: '))
            if year == 'cancel': return
            if year.isdigit() and len(year) == 4: break
            print('Некорректный год выхода!')

        database.insert_data('games', [name, studio, year])

    if num == 2:

        while True:
            filter = int(input('Поиск игры по названию (1); разработчику (2); году выхода (3), отмена (4): '))

            if filter in [1, 2, 3, 4]:
                if filter == 4: return
                break

        while True:

            param = str(input('Поиск: '))

            if len(param) >= 1: break

        try:
            result = database.select_data('games', f"{getconfig()['filters'][str(filter)]} LIKE '%{param}%'")

            print(f'Найдено(а) {len(result)} игр(а)')
            for row in result:
                print(f'\nНазвание: {row[0]}\nстудия: {row[1]}\nгод выхода: {row[2]}\n')

        except Exception as e: print(e)

    if num == 3:

        while True:
            filter = int(input('Удаление игры по названию (1); разработчику (2); году выхода (3), отмена (4): '))
            if filter in [1, 2, 3, 4]:
                if filter == 4: return
                break

        while True:

            param = str(input('Поиск: '))

            if len(param) >= 1:

                result = database.select_data('games', f"{getconfig()['filters'][str(filter)]} LIKE '%{param}%'")

                if len(result) == 1:
                    break
                elif len(result) == 0:
                    print(f'Было найдено 0 совпадений.')
                else:
                    print(f'Найдено {len(result)} игр, попробуйте уточнить поиск.')

        for row in result:
            print(f'Вы точно хотите удалить игру?\nНазвание: {row[0]}\nстудия: {row[1]}\nгод выхода: {row[2]}')

            while True:

                to = str(input('Удалить (Y/N): ')).upper()

                if to in ['Y', 'N']:
                    if to == 'Y':
                        database.delete_data('games', f"{getconfig()['filters'][str(filter)]} LIKE '%{param}%'")
                        print('Игра удалена.')
                    break

    if num == 4:

        while True:
            filter = int(input('Поиск игры по названию (1); разработчику (2); году выхода (3), отмена (4): '))
            if filter in [1, 2, 3, 4]:
                if filter == 4: return
                break

        while True:

            param = str(input('Поиск: '))

            if len(param) >= 1:
                search = getconfig()['filters'][str(filter)]
                result = database.select_data('games', f"{search} LIKE '%{param}%'")

                if len(result) == 1:
                    break
                elif len(result) == 0:
                    print(f'Было найдено 0 совпадений.')
                else:
                    print(f'Найдено {len(result)} игр, попробуйте уточнить поиск.')

        for row in result:
            print(f'\nОтредактировать игру?\n\nНазвание: {row[0]}\nстудия: {row[1]}\nгод выхода: {row[2]}\n')
            game = list(row)

        while True:
            filter = int(input('Изменить название (1); студию (2); год выхода (3), отмена (4): '))
            if filter in [1, 2, 3, 4]:
                if filter == 4: return
                break

        game[filter-1] = str(input("Новое значение: "))

        database.update_data('games', {
            f"{getconfig()['filters']['1']}": f"{game[0]}",
            f"{getconfig()['filters']['2']}": f"{game[1]}",
            f"{getconfig()['filters']['3']}": f"{game[2]}",
        }, f"{search} LIKE '%{param}%'")

        print('Успешное редактирование!')

    if num == 5:

        games = database.select_data('games')
        print(f'Всего {len(games)} игр(ы) в базе данных.\n')
        for game in games:
            print(f'Название: {game[0]}, Студия: {game[1]}, Год выхода: {game[2]}')

    print('\n')

def isvalid(num: int) -> bool:
    if num in [1, 2, 3, 4, 5]:
        return True
    else: return False