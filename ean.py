def keyCalculate(code: int):
    code //= 10  # ignore the last digit
    pond = False
    s = 0

    while code != 0:
        mult = 1 if pond else 3
        s += mult * (code % 10)
        code //= 10
        pond = not pond

    return (10 - (s % 10)) % 10


def isValidKey(code: int):
    return len(str(code)) == 13 and keyCalculate(code) == code % 10


if __name__ == '__main__':
    n = 1294567890128
    if isValidKey(n):
        print(f'\'{n}\' est un code valide !')
    else:
        print(f'\'{n}\' est un code invalide !')
