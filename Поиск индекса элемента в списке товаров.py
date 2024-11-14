# TODO Напишите функцию для поиска индекса товара
def index(list, product):
    for i, c in enumerate(list):
        if c == product:
            return i



items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find in ['банан', 'груша', 'персик']:
    ind_item = index(items_list, find)  # TODO Вызовите функцию, что получить индекс товара

    if ind_item is not None:

        print(f"Первое вхождение товара '{find}' имеет индекс {ind_item}.")

    else:

        print(f"Товар '{find}' не найден в списке.")
