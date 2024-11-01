# TODO импортировать необходимые молули
import json
import csv


INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    with open(INPUT_FILENAME) as file:
        reader = csv.reader(file)
        arr = []
        for row in reader:
            arr.append(list(row))
        newarr = []
        for i in arr[1:]:
            dictry = {}
            for value in range(len(i)):
                dictry[arr[0][value]] = i[value]
            newarr.append(dictry)  # TODO считать содержимое csv файла

    with open(OUTPUT_FILENAME, 'w') as file:
        json.dump(newarr, file, indent=4)  # TODO Сериализовать в файл с отступами равными 4



if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
