def is_very_long(password):
    return any(len(pwd) > 10 for pwd in password)


def has_digit(password):
    return any(digit.isdigit for digit in password)


def has_letters(password):
    return any(letters.isalpha for letters in password)


def has_upper_letters(password):
    return any(upper.isupper for upper in password)


def has_lower_letters(password):
    return any(lower.islower for lower in password)


def has_symbols(password):
    return any(symbols in "$@#%()!&" for symbols in password)


def main():
    password = input("Введите пароль: ")
    def_list = [
        is_very_long,
        has_digit,
        has_letters,
        has_upper_letters,
        has_lower_letters,
        has_symbols
    ]
    score = 0
    for func in def_list:
        if func(password):
            score += 2
    print(score)


if __name__ == '__main__':
    main()