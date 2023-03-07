""" Игра угадай число
Компьютер самостоятельно загадывает и угадывает число менее чем за 20 попыток"""

import numpy as np

def game_score_v3(number: int = 1) -> int:
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
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попыток")
    
    return score

print('Run benchmarking for game_score_v3: ', end='')

# RUN
if __name__ == '__main__':
    score_game(game_score_v3)