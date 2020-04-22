def information(name, family, year, email, phone):
    print(f'{name} {family}. Год рождения: {year}. Электронная почта: {email}. Телефон: {phone}')


input_name = input('Введите имя: ')
input_family = input('Введите фамилию: ')
input_year = input('Введите год рождения: ')
input_email = input('Введите email: ')
input_phone = input('Введите телефон: ')
print('Информация:')
information(family=input_family, name=input_name, phone=input_phone, email=input_email, year=input_year)
