number = 0
while number <= 0:
    number = input('Введите количество товаров: ')
    if not number.isdigit():
        number = 0
    number = int(number)
products = []
for i in range(number):
    print(f'Товар #{i + 1}')
    product = {}
    product['название'] = input('Введите название товара: ')
    product['цена'] = 0
    while product['цена'] <= 0:
        product['цена'] = input('Введите цену товара: ')
        if not product['цена'].isdigit():
            product['цена'] = 0
        product['цена'] = int(product['цена'])
    product['количество'] = 0
    while product['количество'] <= 0:
        product['количество'] = input('Введите количество товара: ')
        if not product['количество'].isdigit():
            product['количество'] = 0
        product['количество'] = int(product['количество'])
    product['ед'] = input('Введите единицу измерения: ')
    products.append((i + 1, product))

print('Товары:')
for product in products:
    print(product)
print()

analyse = {
    'название': [],
    'цена': [],
    'количество': [],
    'ед': []
}

for product in products:
    for key, item in product[1].items():
        if item not in analyse[key]:
            analyse[key].append(item)

print('Аналитика:')
for key, item in analyse.items():
    print(f'{key}: {item}')
