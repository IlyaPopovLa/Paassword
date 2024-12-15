password = input("Введите пароль: ")

if len(password) <= 12:
    print('Короткий')
else:
    print('Длинный')


for letter in password:
    boolResult = letter.isdigit()
    if boolResult:
        print(letter, 'Цифра')
    else:
        print(letter, 'Буква')


found_digit = 'Нет цифр'
for digit in password:
    if digit.isdigit():
        found_digit = 'Есть цифры'
print(found_digit)