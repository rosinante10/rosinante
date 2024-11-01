# TODO Напишите функцию find_common_participants


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
def find_common_participants(s1, s2, sept = ','):
    sarr1 = s1.split(sept)
    sarr2 = s2.split(sept)
    all = []
    for i in sarr1:
        for j in sarr2:
            print(i, j)
            if i == j:
                all.append(i)
    all.sort()
    return all
print(find_common_participants(participants_first_group, participants_second_group, "|"))
