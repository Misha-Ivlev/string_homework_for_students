"""Домашнее задание 3.

Вам дан список предложений.
предложения содержит только слова, которые разделены единичными пробелами.
Необходимо вернуть максимальное количество слов, которое содержится в одном предложении.
sentences[i] - это одно предложение.
Если ни одно из предложений не содержит слов, то вернуть 0
Проверка:
pytest ./3_maximum_number_of_words/test.py
"""


def get_max_number_of_words_from_sentences(sentences: list[str]) -> int:
    """Return maximum number of words in list lines.

    Parameters:
        sentences (list[str]): The list of sentences we want to check

    Returns:
        max_words_number (int): maximum number of words in list lines
    """
    max_words_number = 0
    for sentence in sentences:
        empty_check = int(not bool(sentence))
        sentence_words_number = len(sentence.split(' ')) - empty_check
        max_words_number = max(sentence_words_number, max_words_number)

    return max_words_number
