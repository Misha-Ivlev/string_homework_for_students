"""Домашнее задание 2.

Панграмма - предложение, которое использует каждую букву алфавита (в нашем случае - английского).
Необходимо реализовать код, который скажет, является предложение панграммой или нет.
Буквы в верхнем и нижнем регистрах считаются эквивалентными.
Предложения содержат только буквы английского алфавита, без пробелов и т.п.
Проверка:
pytest ./2_sentence_is_pangram/test.py
"""


def is_sentence_is_pangram(sentence: str) -> bool:
    """Return the conclusion that this is a pangram sentence.

    Parameters:
        sentence (str): The string we want to check

    Returns:
        True if the sentense is pangram else - False
    """
    alphabet = [False for _ in range(26)]
    for word in sentence:
        alphabet[ord(word.lower()) - 97] = True

    return False not in alphabet
