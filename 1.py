def get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[0])
    if len(str_number) > 1:
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        return first

result = get_multiplied_digits(40203)
print(result)
result2 = get_multiplied_digits(402030)
print(result2)
'''В result2 получается 0, хотя в задании в примере результата выполнения программы: 
Вывод на консоль: 24. Можно в код добавить условие != 0,но про это не сказано в задании. 
Как будто бы этот результат '24' ошибка в задании'''