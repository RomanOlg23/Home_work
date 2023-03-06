import numpy as np

def random_predict(number: int = 1) -> int:
    """Просто угадываем на random, никак не используя информацию о больше или меньше.
       Функция принимает загаданное число и возвращает число попыток

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0

    while True:
        count += 1
        predict_number = np.random.randint(1, 101)  # предполагаемое число
        if number == predict_number:
            break  # выход из цикла если угадали
    
    return count
print(random_predict())

def game_core_v3(number: int = 1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Колличество попыток
    """
    count = 0
    begin = 1
    finish = 100
    
    while True:
        count += 1
        aver_num = (begin + finish)//2 # чтобы сократить кол-во попыток, делим диапазон на 2
        if aver_num == number:
            print (f'Число {aver_num} найдено за {count} попыток')
            break # выйти, если число найдено
        elif aver_num > number:
            finish = aver_num 
        else:
            begin = aver_num

    return count
print(game_core_v3())

def score_game(random_predict) -> int:
    """За какое количество попыток в среднем за 10000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(10000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попытки")
    
#Run benchmarking to score effectiveness of algorithm

print('Run benchmarking for game_core_v3: ', end='')
score_game(game_core_v3)