import json # Импорт библиотеки


def task() -> float:  # Определяем функцию, которая возвращает тип float
    f = "input.json"
    with open(f) as a:  #Открываем файл json
        data = json.load(a)  # Используем load для парсинга JSON данных из файла и сохраненяем их в переменную data
    sm = sum([i["score"] * i["weight"] for i in data])   # Создаем список, где для каждого элемента `i` в данных data перемножаются score и weight
    return round(sm, 3)  #  Округляем до трех знаков после запятой


print(task())

