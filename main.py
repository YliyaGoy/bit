def getmask(p, n):
    mask = (1 << n) - 1    # Создание маски из единиц по n битам
    mask = mask << (p - 1) # Сдвиг маски влево на (p-1) позиций
    return mask


def cut(u, p, n):
    mask = ((1 << n) - 1) << (p - 1) # Определение маски для вырезания n бит, начиная с p-ого
    result = u & ~mask               # Применение маски для вырезания бит
    return result


def del_(u, p, n):
    mask = ((1 << n) - 1) << (p - 1) # Определение маски для удаления n бит, начиная с p-ого
    result = u & ~mask               # Применение маски для удаления бит
    return result


def ins(u, u1, p, n):
    mask = ((1 << n) - 1)           # Создание маски для извлечения n бит из u1
    mask = mask & (u1 >> (p - 1))    # Извлечение n бит из u1, начиная с p-ого
    mask = mask << (p - 1)          # Сдвиг бит в позицию p-ого в u
    result = (u & ~mask) | mask     # Вставка извлеченных бит в u
    return result


def ins_at_position(u, p, u1, p1, n):
    mask = ((1 << n) - 1)           # Создание маски для извлечения n бит из u1
    mask = mask & (u1 >> (p1 - 1))  # Извлечение n бит из u1, начиная с p1-ого
    mask = mask << (p - 1)          # Сдвиг бит в позицию p-ого в u
    result = (u & ~mask) | mask     # Вставка извлеченных бит в u
    return result


def count_leading_zeros(num):
    if num == 0:
        return 32  # Если число равно 0, вся последовательность битов считается ведущими нулями
    count = 0
    while (num >> count) & 1 == 0:  # Проверка каждого бита, начиная с самого левого
        count += 1
    return count


# Битовые операции
def bit_operation():
    print("Битовые операции: ")

    # Операция И (AND)
    result_and = 5 & 3
    print(f'Результат операции И: {result_and}')

    # Операция ИЛИ (OR)
    result_or = 5 | 3
    print(f'Результат операции ИЛИ: {result_or}')

    # Операция исключающее ИЛИ (XOR)
    result_xor = 5 ^ 3
    print(f'Результат операции XOR: {result_xor}')

    # Операция инверсии (NOT)
    result_not_5 = ~5
    result_not_3 = ~3
    print(f'Результат инверсии числа 5: {result_not_5}')
    print(f'Результат инверсии числа 3: {result_not_3}')

    # Сдвиг влево
    result_shift_left = 5 << 2
    print(f'Результат сдвига влево: {result_shift_left}')

    # Сдвиг вправо
    result_shift_right = 5 >> 2
    print(f'Результат сдвига вправо: {result_shift_right}')

    # Установка единиц
    set_bits = 5 | (1 << 2)
    print(f'Установка единицы во втором разряде: {set_bits}')

    # Установка нулей
    clear_bits = 5 & ~(1 << 0)
    print(f'Установка нуля в нулевом разряде: {clear_bits}')

    # Изменение заданных разрядов на противоположные
    toggle_bits = 5 ^ (1 << 1)
    print(f'Изменение второго разряда на противоположный: {toggle_bits}')

    # Инверсия всех разрядов
    invert_bits = ~5
    print(f'Инверсия всех разрядов: {invert_bits}')
    print(" ")


def zeros():
    number = 12
    leading_zeros = count_leading_zeros(number)
    print(f'Количество ведущих нулей числа {number} в двоичном представлении: {leading_zeros}')
    print(" ")


def b_funk():
    print("Базовые функции битовых операций")
    p = 3
    n = 4
    u = 0b11011010
    u1 = 0b1010
    p1 = 2

    mask_result = getmask(p, n)
    cut_result = cut(u, p, n)
    del_result = del_(u, p, n)
    ins_result = ins(u, u1, p, n)
    ins_position_result = ins_at_position(u, p, u1, p1, n)

    print(f'Маска из единиц по {n} битам, начиная с {p}-ого: {bin(mask_result)}')
    print(f'Результат вырезания {n} бит, начиная с {p}-ого: {bin(cut_result)}')
    print(f'Результат удаления {n} бит, начиная с {p}-ого: {bin(del_result)}')
    print(f'Результат вставки {n} бит из u1 в u, начиная с {p}-ого: {bin(ins_result)}')
    print(f'Результат вставки {n} бит из u1 с позиции {p1}-ой в u, начиная с {p}-ого: {bin(ins_position_result)}')
    print(" ")

bit_operation()
b_funk()
zeros()



