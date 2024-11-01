numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим

numbers_2 = numbers[:4]+numbers[5:]
sred = sum(numbers_2)/len(numbers)
numbers[4] = sred
print("Измененный список:", numbers)



