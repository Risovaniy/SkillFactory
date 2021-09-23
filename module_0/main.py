import numpy as np


def game_core_v1(number, minimum, maximum):
    """Просто угадываем на random, никак не используя информацию о больше или меньше.
       Функция принимает загаданное число и возвращает число попыток"""
    count = 0

    while True:
        count += 1
        predict = np.random.randint(minimum, maximum)  # предполагаемое число
        if number == predict:

            return count  # выход из цикла, если угадали


def score_game(game_core, minimum, maximum):
    """Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число"""
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(minimum, maximum, size=(1000))

    for number in random_array:
        count_ls.append(game_core(number, minimum, maximum))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")

    return (score)


def game_core_v2(number, minimum, maximum):
    """Сначала устанавливаем любое random число, а потом уменьшаем или
    увеличиваем его в зависимости от того, больше оно или меньше нужного.
       Функция принимает загаданное число и возвращает число попыток"""
    count = 1
    predict = np.random.randint(minimum, maximum)

    while number != predict:
        count += 1
        if number > predict:
            predict += 1
        elif number < predict:
            predict -= 1

    return (count)  # выход из цикла, если угадали


def binary_search_middle(secret_number, left_limit, right_limit):
    """The function guesses a mysterious number between () and () binary search
    (with "less", "more" and 2 division).
    The function returns the number of a successful attempt."""

    count = 1
    predict = int((right_limit + left_limit) / 2)

    while predict != secret_number:
        if predict > secret_number:
            right_limit = predict
            new_predict = int((left_limit + right_limit) / 2)
            predict = new_predict if predict != new_predict else (new_predict + 1)
        else:
            left_limit = predict
            new_predict = int((left_limit + right_limit) / 2)
            predict = new_predict if predict != new_predict else (new_predict + 1)

        count += 1

    return count


if __name__ == '__main__':
    count = 0  # счетчик попыток
    minimal, maximal = 1, 101

    number = np.random.randint(minimal, maximal)  # загадали число
    print("Загадано число от 1 до 100")

    # Start my version finding of secret number
    score_game(binary_search_middle, minimal, maximal)

    # запускаем
    score_game(game_core_v1, minimal, maximal)

    # Проверяем
    score_game(game_core_v2, minimal, maximal)

