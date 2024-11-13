import csv  #Импорт библиотек
import json


INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:  #Функция которая не возвращает никакого значения
    with open(INPUT_FILENAME) as f:  #  Открываем входной файл
        lines = [l for l in csv.DictReader(f)]  #  Создаем список из строк прочитанных из csv файла

    with open(OUTPUT_FILENAME, "w") as f:  #Открываем выходной файл для записи в режиме "w"
        json.dump(lines, f, indent=4)    #Преобразуем список словарей в формат json и записываем его в файл с отступом в 4 пробела


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")

