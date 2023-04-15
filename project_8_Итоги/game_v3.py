def game_core_v3(number: int = 1) -> int:
    """
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток

    игра методом сужения интервалов угадавает загаданное число
    """
    # Ваш код начинается здесь

    n=number  #Predict загаданное число
    x = 50    #предположительно отгаданное число
    count=0 
    min=1
    max=100   # задаем начальный интервал
              # в цикле уточняем интервал, 
              # получаем загаданное число
    while count < 20:
      count += 1
      if round(x,0) == n:
        break 
      if x>n:
        max = x
        x=x - (max-min)/2
      else :
        min = x
        x=x + (max-min)/2

    return count 

def score_game():
    '''
    args:
         отсутствуют
         
    returns:
        list: список попыток на на все числа
         
    проверочная функция запускает
    игру на каждое число которое может быть 
    загадано в рамках правил
    и сохраняет counter от каждого запуска в список
    видим что все они в пределах 10 
    '''
    
    counters_list = []
    for number in range(1,100):
        counters_list.append(game_core_v3(number))
        number += 1
    return counters_list
print (score_game())    