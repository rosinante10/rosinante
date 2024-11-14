# TODO Напишите функцию find_common_participants


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"


def find_common_participants(s1, s2, sep = ','):
    sarr1 = s1.split(sep)
    sarr2 = s2.split(sep)
    all = []
    for i in sarr1:
        for j in sarr2:
            if i == j:
                all.append(i)
    all.sort()
    return all



a = find_common_participants(participants_first_group, participants_second_group,"|")
print("Общие участники:", a)
