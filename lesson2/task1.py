a = ['string', 1, 1.5, False, [0, 1], (3, 4), {1: 'one', 2: 'two'}, None, b'text', bytearray(b'text')]
for item in a:
    print(f'Элемент: {item} -- Тип: {type(item)}')
