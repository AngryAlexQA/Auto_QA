# home_work/2_hw.py - `Alexandra Bujor`

def task_1() -> None:
    """
    Решение задачи 1.
    Создает 5 переменных разных типов и выводит их тип в консоль.
    """
    # i-iii. Создание переменных с произвольными именами и значениями
    integer_value = 42
    float_value = 3.14159
    string_value = "Hello, World!"
    list_value = [1, 2, 3, 4, 5]
    boolean_value = True

    # iv. Вывод типа данных каждой переменной в консоль
    print(f"Тип переменной integer_value: {type(integer_value)}")
    print(f"Тип переменной float_value: {type(float_value)}")
    print(f"Тип переменной string_value: {type(string_value)}")
    print(f"Тип переменной list_value: {type(list_value)}")
    print(f"Тип переменной boolean_value: {type(boolean_value)}")


def task_2() -> None:
    """
    Решение задачи 2.
    Выводит первые 3 значения заданного списка.
    """
    # a.i. Заданный список
    a = [1, 2, 3, 5, 8, 13, 21]

    # a.ii. Вывод первых 3 значений списка
    # Используется срез (slice) списка от индекса 0 до индекса 3 (не включая его)
    print("Первые три значения списка:", a[0:3])

    # d.* Эта последовательность чисел называется "числа Фибоначчи".
    # Каждое последующее число равно сумме двух предыдущих.
    # Для данного списка: 1+2=3, 2+3=5, 3+5=8, 5+8=13, 8+13=21.


def task_3(number: int | float) -> int | float:
    """
    Решение задачи 3.
    Принимает число и возвращает его квадрат.

    Args:
        number (int | float): Входное число.

    Returns:
        int | float: Квадрат входного числа.
    """
    return number ** 2


# c. Добавление вызова функций

# Вызов функции task_1()
print("Задача 1:")
task_1()
print()  # Пустая строка для читаемости вывода

# Вызов функции task_2()
print("Задача 2:")
task_2()
print()  # Пустая строка для читаемости вывода

# Вызов функции task_3() и печать результата
print("Задача 3:")
input_number = 5
result = task_3(input_number)
print(f"Квадрат числа {input_number} равен {result}")
