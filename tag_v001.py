
"""вывод упорядоченного поля"""
def print_field(field):
    cnt = 0
    print("----" * 4)
    print_str(cnt)
    print_str(cnt + 4)
    print_str(cnt + 8)
    print_str(cnt + 12)
    print("----" * 4)
"""вывод одной строки поля"""
def print_str(cnt):
    for pos in field[0 + cnt : 4 + cnt]:
        if field[cnt] in range(10) or field[cnt] == " ":
            print("| " + str(field[cnt]) + "|", end="")
        else:
            print("|" + str(field[cnt]) + "|", end="")
        cnt += 1
    print()
"""смена позиции пустого квадрата"""
def change_pos(empty_pos, direct):
    field[empty_pos], field[empty_pos + direct] = field[empty_pos + direct], field[empty_pos]
    return field


tag = [int(i) for i in range(1, 16)] + [" "]
field = [1, 3, 2, 4, " ", 5, 6, 10, 13, 11, 12, 15, 14, 9, 8, 7]
motion_dict = {"a": -1, "d": 1, "s": 4, "w": -4}


def the_tag():
    print("The game is Tag.")
    print_field(field)
    while tag != field:
        empty_pos = field.index(" ")
        user_input = input("input direct: ")
        if user_input not in motion_dict:
            print("Error of motion, try one more time, please.")
            continue
        else:
            direct = motion_dict[user_input]

        if direct == -1 and empty_pos not in [0, 13, 4] or direct == 1 and empty_pos not in range(3, 16, 4):
            change_pos(empty_pos, direct)

        try:
            if direct == -4 and empty_pos not in range(0, 4) or direct == 4 and empty_pos not in range(13, 17):
                change_pos(empty_pos, direct)
        except IndexError:
            print("This is the Wall, one more time, please.")

        print_field(field)

the_tag()



