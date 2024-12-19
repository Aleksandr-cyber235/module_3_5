ef get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[0])

    # Если длина строки больше 1, продолжаем рекурсию
    if len(str_number) > 1:
        # Рекурсивно вызываем функцию, пропуская нули
        if first == 0:
            return get_multiplied_digits(int(str_number[1:]))
        else:
            return first * get_multiplied_digits(int(str_number[1:]))
    else:
        # Если оставшаяся цифра только одна, возвращаем ее
        return first if first != 0 else 1  # Вернем 1, чтобы корректно умножить на остальные цифры


result1 = get_multiplied_digits(40203)
print(result1)
result2 = get_multiplied_digits(402030)
print(result2)
