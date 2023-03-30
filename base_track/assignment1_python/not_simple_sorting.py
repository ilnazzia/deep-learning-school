# Пусть у нас есть следующий список, в котором элементы -- tuple из строк:
items = [('one', 'two'), ('three', 'four'), ('five', 'six'), ('string', 'a')]

# Мы хотим отсортировать этот список по последней букве второго элемента каждого tuple, т.е. получить такой список:
# sorted_items = [ ('string', 'a'), ('one', 'two'), ('three', 'four'), ('five', 'six'),]

sorted_items = sorted(items, key=lambda x: x[1][-1])

print(sorted_items)