import random

BOARD_SIZE = 3
BLANK = "."
game_board = [[BLANK for column in range(BOARD_SIZE)] for row in range(BOARD_SIZE)]
next_turn = True


def main():
    """
    Интерфейс с пользователем
    Общая логика игры
    """
    print("Start game")
    global next_turn
    for current_turn in get_next_turn():
        print_board()
        sign, turn_result = current_turn()
        if turn_result == "e":
            print("Exit...")
            break
        next_turn = update_game_board(sign, turn_result)
        if next_turn:
            if check_win(sign):
                print("Player is win!!!")
                print_board()
                break
            if board_is_full():
                print("Draw !!!")
                print_board()
                break
        else:
            print("!!! Try again !!!")

    print("Game over")


def print_board():
    """
    Выводит игровое поле на экран
    """
    column_numbers = [str(column) for column in range(BOARD_SIZE)]
    print(' ', row_to_print(column_numbers))
    row_number = 0
    for row in game_board:
        print(row_number, row_to_print(row))
        row_number += 1


def row_to_print(row):
    """
    Фомирует строку игровой доски для печати
    :param row: данные строки игровой доски
    :return: строка для печати
    """
    return " ".join(row)


def turn_player_one():
    """
    Сделать ход первому игроку
    :return: Результат хода
    """
    data = input('Player X (cr): ("e"-exit): ')
    return 'X', data


def turn_player_two():
    """
    Сделать ход второму игроку
    :return: Результат хода
    """
    data = input('Player 0 (cr): ("e"-exit): ')
    return '0', data


def get_next_turn():
    """
    Генерирует последовательность ходов
    next_turn - передать ход следующему игроку, иначе, повтор хода
    :return: Результат очередного хода игрока
    """
    order = [turn_player_one, turn_player_two]
    current = int(random.randint(1, 10) <= 5)
    while True:
        yield order[current]
        if next_turn:
            current = 0 if current == 1 else 1


def update_game_board(sign, turn_result):
    """
    Проверяет корректность введенных данных
    Добавляет ход на доску
    :param sign: Х или 0
    :param turn_result: Данные хода игрока
    :return: Истина, если все успешно
    """
    result = False
    result_check, column, row = check_turn_result(turn_result)
    if result_check and cell_is_free(column, row):
        game_board[row][column] = sign
        result = True
    return result


def check_turn_result(turn_result):
    """
    Проверяет правильность координат, введенных пользователем
    :param turn_result: координаты
    :return: истина - успешно
    """
    result = False
    column = 0
    row = 0
    if turn_result.isdigit():
        if len(turn_result) == 2:
            column = int(turn_result[0])
            row = int(turn_result[1])
            if column < BOARD_SIZE and row < BOARD_SIZE:
                result = True
    return result, column, row


def cell_is_free(column, row):
    """
    Проверяет, свободна ли заданная клетка
    :param column: номер колонки
    :param row: номер строки
    :return: Истина, если клетка свободна
    """
    return game_board[row][column] == BLANK


def check_win(sign):
    """
    Возвращает истину, если текущий ход выигрышный
    """
    win = False
    # horizontal
    for row in range(BOARD_SIZE):
        count = 0
        for column in range(BOARD_SIZE):
            if game_board[row][column] == sign:
                count += 1
        if count == 3:
            win = True
            break
    # vertical
    if not win:
        for column in range(BOARD_SIZE):
            count = 0
            for row in range(BOARD_SIZE):
                if game_board[row][column] == sign:
                    count += 1
            if count == 3:
                win = True
                break
    # diagonal left to right
    if not win:
        count = 0
        for index in range(BOARD_SIZE):
            if game_board[index][index] == sign:
                count += 1
        win = count == 3

    # diagonal right to left
    if not win:
        count = 0
        for column, row in zip(range(BOARD_SIZE - 1, -1, -1), range(BOARD_SIZE)):
            if game_board[column][row] == sign:
                count += 1
        win = count == 3

    return win


def board_is_full():
    """
    Проверяет, есть ли еще свободные клетки на доске
    :return: Истина, если доска заполнена полностью
    """
    no_blank = True
    for row in range(BOARD_SIZE):
        for column in range(BOARD_SIZE):
            if game_board[row][column] == BLANK:
                no_blank = False
                break
    return no_blank


if __name__ == "__main__":
    main()

