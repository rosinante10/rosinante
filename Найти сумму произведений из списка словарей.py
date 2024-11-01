# TODO решите задачу
import json
def task() -> float:
    f = open("input.json")
    data = json.load(f)
    sum = 0
    for i in data:
        n = i["score"]*i["weight"]
        sum += n
    newsum = round(sum, 3)
    f.close()
    return newsum
print(task())

