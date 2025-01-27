"""Домашнее задание 1.

На вход даны два массива строк array_string1 и array_string2, верните True, если
они представляют одинаковые строки, и False в противном случае.
Пример:
1) array_string_1 = ['ab', 'c'], array_string_2 = ['a', 'bc'] => 'abc' == 'abc' (True)
1) array_string_1 = ['ab'], array_string_2 = ['a', 'bc'] => 'ab' != 'abc' (False)

Решение необходимо написать в функции, предоставленной ниже. Функция должна возвращать bool значение.
Строки в верхнем и нижнем регистре с одинаковыми символами считаются совпадающими.
Для проверки установите все необходимые библиотеки из файла requirements.txt и выполните команду из корня проекта:
pytest ./1_two_string_array_equivalent/test.py
"""


def is_array_string_are_equal(array_string1: list[str], array_string2: list[str]) -> bool:
    """Return the result of a string comparison.

    Parameters:
        array_string1 (list[str]): A list of strings
        array_string2 (list[str]): A list of strings

    Returns:
        bool(string1 == string2)
    """
    string1 = ''.join(array_string1).lower()
    string2 = ''.join(array_string2).lower()

    return string1 == string2
