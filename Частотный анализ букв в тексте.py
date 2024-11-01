# TODO  Напишите функцию count_letters
def count_letters(str):
    alphabet = []
    strl = str.lower()
    k = 0
    for i in range(len(strl)):
        if strl[i].isalpha():
            k += 1
            if strl[i] not in alphabet:
                alphabet.append(strl[i])
    count_alphabet = []
    count = 0
    for j in alphabet:
        for s in range(len(strl)):
            if j==strl[s]:
                count += 1
        count_alphabet.append([j, count])
        count = 0
    count_alphabet.append(k)
    return count_alphabet


# TODO Напишите функцию calculate_frequency
def calculate_frequency(arr):


    keys = []
    values = []
    for i in arr:
        if type(i) == list:
            keys.append(i[0])
            value = str(round(i[1]/arr[-1], 2))
            if len(value)< 4:
                value += '0'
            values.append(value)

    final = {keys[j]: values[j] for j in range(len(keys)) }
    return final




main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

# TODO Распечатайте в столбик букву и её частоту в тексте
dictry = calculate_frequency(count_letters(main_str))
for alpha, value in dictry.items():
    print(f'{alpha}: {value}')
