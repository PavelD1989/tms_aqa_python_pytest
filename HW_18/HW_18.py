from HW_18.HW_18 import *

import unittest
# Задание 1. Даны два целых числа A и B (A < B).
# Найти сумму всех целых чисел от A до B включительно.
"""
Чек-лист для проверки функции:

А и В - целые числа
A < B
1 < A <= 5
5 < B < 10

1.  Сумма целых чисел (А: целое число меньше В; В: целое число больше A).
    Ожидаемый результат: вывод суммы
2.  Сумма целых чисел (А: целое число на нижней границе; В: целое число на нижней границе).
    Ожидаемый результат: вывод суммы
3.  Сумма целых чисел (А: целое число выше нижней границы; В: целое число выше нижней границы).
    Ожидаемый результат: вывод суммы
4.  Сумма целых чисел (А: целое число на верхней границе; В: целое число на верхней границе).
    Ожидаемый результат: вывод суммы
5.  Сумма целых чисел (А: целое число ниже верхней границы; В: целое число ниже верхней границы).
    Ожидаемый результат: вывод суммы
6.  Сумма целых чисел (А: целое число больше В; В: целое число меньше A).
    Ожидаемый результат: вывод сообщения, что В должно быть числом, большим А.
7.  Сумма целых чисел (А: позитивное число; В: дробное число).
    Ожидаемый результат: вывод сообщения, число В должно быть целым числом в диапазоне 6 до 9.
8.  Сумма целых чисел (А: позитивное число; В: не число).
    Ожидаемый результат: вывод сообщения, что В должно быть целым числом.
9.  Сумма целых чисел (А: позитивное число; В: 0).
    Ожидаемый результат: вывод сообщения, что В должно быть целым числом в диапазоне от 6 до 9.
10. Сумма целых чисел (А: позитивное число; В: пусто).
    Ожидаемый результат: вывод сообщения, что В целым числом в диапазоне от 6 до 9.
11. Сумма целых чисел (А: дробное число; В: позитивное число).
    Ожидаемый результат: вывод сообщения, что число А должно быть целым числом в диапазоне от 2 до 5.
12. Сумма целых чисел (А: не число; В: позитивное число).
    Ожидаемый результат: вывод сообщения, что А должно быть целым числом в диапазоне от 2 до 5.
13. Сумма целых чисел (А: 0; В: позитивное число).
    Ожидаемый результат: вывод сообщения, что А должно быть целым числом в диапазоне от 2 до 5.
14. Сумма целых чисел (А: пусто; В: позитивное число).
    Ожидаемый результат: вывод сообщения, что А должно быть целым числом в диапазоне от 2 до 5.
"""


def sum_of_integers(number_1: int, number_2: int):
    if type(number_1) in [int]:
        if type(number_2) in [int]:
            if 1 < number_1 <= 5:
                if 5 < number_2 <= 10:
                    sum_numbers = 0
                    for i in range(number_1, number_2 + 1):
                        sum_numbers += i
                    return sum_numbers
                else:
                    return "B должно быть в диапазоне от 6 до 10"
            else:
                return "А должно быть в диапазоне от 2 до 5"
        else:
            return "В должно быть целым числом в диапазоне от 6 до 10"
    else:
        return "А должно быть целым числом в диапазоне от 2 до 5"


class TestSumOfIntegers(unittest.TestCase):

    def test_01(self):
        self.assertEqual(25, sum_of_integers(3, 7))

    def test_02(self):
        self.assertEqual(20, sum_of_integers(2, 6))

    def test_03(self):
        self.assertEqual(25, sum_of_integers(3, 7))

    def test_04(self):
        self.assertEqual(35, sum_of_integers(5, 9))

    def test_05(self):
        self.assertEqual(30, sum_of_integers(4, 8))

    def test_06(self):
        self.assertEqual("А должно быть в диапазоне от 2 до 5",
                         sum_of_integers(7, 5))

    def test_07(self):
        self.assertEqual("В должно быть целым числом в диапазоне от 6 до 10",
                         sum_of_integers(3, 7.1))

    def test_08(self):
        self.assertEqual("В должно быть целым числом в диапазоне от 6 до 10",
                         sum_of_integers(3, "6"))

    def test_09(self):
        self.assertEqual("B должно быть в диапазоне от 6 до 10",
                         sum_of_integers(3, 0))

    def test_10(self):
        self.assertEqual("В должно быть целым числом в диапазоне от 6 до 10",
                         sum_of_integers(3, ""))

    def test_11(self):
        self.assertEqual("А должно быть целым числом в диапазоне от 2 до 5",
                         sum_of_integers(3.1, 6))

    def test_12(self):
        self.assertEqual("А должно быть целым числом в диапазоне от 2 до 5",
                         sum_of_integers("3", 6))

    def test_13(self):
        self.assertEqual("А должно быть в диапазоне от 2 до 5",
                         sum_of_integers(0, 6))

    def test_14(self):
        self.assertEqual("А должно быть целым числом в диапазоне от 2 до 5",
                         sum_of_integers("", 6))



# Задание 2
def sum_of_natural_numbers(list_natural_numbers: list):
    sum_numbers = 0
    for i in range(len(list_natural_numbers)):
        if list_natural_numbers[i] > 0 and not isinstance(
            list_natural_numbers[i], float
        ):
            sum_numbers += list_natural_numbers[i]
    return sum_numbers


# Задание 3
def integer_operations(list_integers_numbers: list):
    multiplication_of_positive_num = 1
    sum_of_negative_num = 0
    count_of_negative_num = 0

    for i in range(len(list_integers_numbers)):
        if list_integers_numbers[i] > 0:
            multiplication_of_positive_num *= list_integers_numbers[i]
        else:
            sum_of_negative_num += list_integers_numbers[i]
            count_of_negative_num += 1
    return multiplication_of_positive_num, sum_of_negative_num, \
        count_of_negative_num


# Задание 4
def best_result(dict_swimmers: dict):
    for key, value in dict_swimmers.items():
        if value == max(dict_swimmers.values()):
            return f"Лучший результат заплыва: {key} - " \
                   f"{max(dict_swimmers.values())}"







# _________________Вторая часть____________________________



# Задание 1. Дано число N. Найти произведение всех чисел от 0 до N
"""
Уточнение требований:
1.  N целое число.
2.  1 <= N <= 10.

Чек-лист для проверки функции:
1.  Произведение чисел от 0 до N (N равно минимальному значению).
    Ожидаемый результат: вывод произведения чисел.
2.	Произведение чисел от 0 до N (N внутри класса эквивалентности).
    Ожидаемый результат: вывод произведения чисел.
3.	Произведение чисел от 0 до N (N равно максимальному значению).
    Ожидаемый результат: вывод произведения чисел.
4.	Произведение чисел от 0 до N (N отрицательное число).
    Ожидаемый результат: вывод сообщения, что N должно быть больше или равно 1
    и меньше или равно 10.
5.	Произведение чисел от 0 до N (N равно 0).
    Ожидаемый результат: вывод сообщения, что N должно быть больше или равно 1
    и меньше или равно 10.
6.	Произведение чисел от 0 до N (N больше максимального значения).
    Ожидаемый результат: вывод сообщения, что N должно быть больше или равно 1
    и меньше или равно 10.
7.	Произведение чисел от 0 до N (N пустое).
    Ожидаемый результат: вывод сообщения, что N должно быть числом целого типа.
8.	Произведение чисел от 0 до N (N - None).
    Ожидаемый результат: вывод сообщения, что N должно быть числом целого типа.
9.	Произведение чисел от 0 до N (N - несколько пробелов).
    Ожидаемый результат: вывод сообщения, что N должно быть числом целого типа.
10.	Произведение чисел от 0 до N (N символьное значение).
    Ожидаемый результат: вывод сообщения, что N должно быть числом целого типа.
"""


def multiplication_of_numbers(number: int):
    try:
        if type(number) not in [int]:
            raise TypeError(f"Вы ввели значение '{number}'. Вводимое значение "
                            f"должно быть числом целого типа")
        if number < 1 or number > 10:
            raise ValueError(
                f"Вы ввели число {number}. Вводимое число должно быть"
                f" от 1 до 10")

        multiplication = 1
        i = 1
        while i <= number:
            multiplication *= i
            i += 1
        return multiplication

    except TypeError as exc:
        print(exc)
    except ValueError as exc:
        print(exc)


class TestMultiplicationOfNumber(unittest.TestCase):

    def test_min_value(self):
        self.assertEqual(1, multiplication_of_numbers(1),
                         "Произведение чисел не равно 1")

    def test_internal_value(self):
        self.assertEqual(multiplication_of_numbers(5), 120,
                         "Произведение чисел не равно 120")

    def test_max_value(self):
        self.assertEqual(3628800, multiplication_of_numbers(10),
                         "Произведение чисел не равно 3628800")

    def test_negative_value(self):
        self.assertIsNone(multiplication_of_numbers(-1))

    def test_zero_value(self):
        self.assertIsNone(multiplication_of_numbers(0))

    def test_more_max_value(self):
        self.assertIsNone(multiplication_of_numbers(11))

    def test_empty_value(self):
        self.assertIsNone(multiplication_of_numbers(""))

    def test_none_value(self):
        self.assertIsNone(multiplication_of_numbers(None))

    def test_spaces_value(self):
        self.assertIsNone(multiplication_of_numbers("   "))

    def test_symbol_value(self):
        self.assertIsNone(multiplication_of_numbers("проверка"))


# Задание 2. Поле засеяли цветами двух сортов на площади S1 и S2.
# Каждый год площадь цветов первого сорта увеличивается вдвое,
# а площадь второго сорта увеличивается втрое.
# Через сколько лет площадь первых сортов будет составлять меньше 10%
# от площади вторых сортов.
""" 
Чек-лист для проверки функции:

Уточнение требований:
1.  S1, S2 - целые числа
2.  0 < S1 <= 5
3.  0 < S2 <= 3

1.  Вычисление количества лет (S1, S2: числа на нижней границе).
    Ожидаемый результат: вычисленное количество лет.
2.  Вычисление количества лет (S1, S2: числа внутри классов эквивалентности).
    Ожидаемый результат: вычисленное количество лет.
3.  Вычисление количества лет (S1, S2: числа на верхней границе).
    Ожидаемый результат: вычисленное количество лет.
4.  Вычисление количества лет (S1, S2: числа ниже верхней границы).
    Ожидаемый результат: вычисленное количество лет.
5.  Вычисление количества лет (S1, S2: числа выше верхней границы).
    Ожидаемый результат: сообщение, что введенные цифры вне разрешенных диапазонов.
6.  Вычисление количества лет (S1, S2: числа ниже нижней границы).
    Ожидаемый результат: вычисленное количество лет.
7.  Вычисление количества лет (S1, S2: числа на нижней границы).
    Ожидаемый результат: вычисленное количество лет.
8.  Вычисление количества лет (S1, S2: числа выше нижней границы).
    Ожидаемый результат: вычисленное количество лет.
9.  Вычисление количества лет (S1: 0; S2: позитивное число).
    Ожидаемый результат: вывод сообщение, что S1 должна быть в разрешенном диапазоне.
10. Вычисление количества лет (S1: не целое число; S2: позитивное число).
    Ожидаемый результат: вывод сообщение, что S1 должна быть числом в разрешенном диапазоне.
11. Вычисление количества лет (S1: позитивное число; S2: пусто).
    Ожидаемый результат: вывод сообщение, что S2 должна быть числом в разрешенном диапазоне.
12. Вычисление количества лет (S1: позитивное число; S2: 0).
    Ожидаемый результат: вывод сообщение, что S2 должна быть числом в разрешенном диапазоне.
13. Вычисление количества лет (S1: позитивное число; S2: не целое число).
    Ожидаемый результат: вывод сообщение, что S2 должна быть числом в разрешенном диапазоне.
"""


def calculation_of_years(area_1: int, area_2: int):
    if type(area_1) in [int]:
        if type(area_2) in [int]:
            if 0 < area_1 <= 5:
                if 0 < area_2 <= 3:
                    year = 1
                    while area_1 > area_2 * 0.1:
                        area_1 *= 2
                        area_2 *= 3
                        year += 1
                    return area_1, area_2, year
                else:
                    return "S2 должна быть в диапазоне от 1 до 3"
            else:
                return "S1 должна быть в диапазоне от 1 до 5"
        else:
            return "S2 должно быть целым числом в диапазоне от 1 до 3"
    else:
        return "S1 должно быть целым числом в диапазоне от 1 до 5"


class TestCalculationOfYears(unittest.TestCase):

    def test_01(self):
        self.assertEqual((64, 729, 7), calculation_of_years(1, 1))

    def test_02(self):
        self.assertEqual((384, 4374, 8), calculation_of_years(3, 2))

    def test_03(self):
        self.assertEqual((640, 6561, 8), calculation_of_years(5, 3))

    def test_04(self):
        self.assertEqual((1024, 13122, 9), calculation_of_years(4, 2))

    def test_05(self):
        self.assertEqual("S1 должна быть в диапазоне от 1 до 5",
                         calculation_of_years(6, 4))

    def test_06(self):
        self.assertEqual("S1 должна быть в диапазоне от 1 до 5",
                         calculation_of_years(-1, 0))

    def test_07(self):
        self.assertEqual((64, 729, 7), calculation_of_years(1, 1))

    def test_08(self):
        self.assertEqual((1024, 13122, 9), calculation_of_years(4, 2))

    def test_09(self):
        self.assertEqual("S1 должна быть в диапазоне от 1 до 5",
                         calculation_of_years(0, 2))

    def test_10(self):
        self.assertEqual("S1 должно быть целым числом в диапазоне от 1 до 5",
                         calculation_of_years("проверка", 2))

    def test_11(self):
        self.assertEqual("S2 должно быть целым числом в диапазоне от 1 до 3",
                         calculation_of_years(4, None))

    def test_12(self):
        self.assertEqual("S2 должна быть в диапазоне от 1 до 3",
                         calculation_of_years(4, 0))

    def test_13(self):
        self.assertEqual("S2 должно быть целым числом в диапазоне от 1 до 3",
                         calculation_of_years(4, 1.2))





# Задание 3
def count_and_sum_number(number: int):
    sum_of_numbers = 0
    count_of_numbers = 0
    while number > 0:
        sum_of_numbers += number % 10
        number //= 10
        count_of_numbers += 1
    return sum_of_numbers, count_of_numbers


# Задание 4
def difference_calculation(grandfather_age: int, grandson_age: int):
    year = 0
    while grandfather_age > grandson_age * 2:
        year += 1
        grandfather_age += 1
        grandson_age += 1
    return year, grandfather_age, grandson_age
