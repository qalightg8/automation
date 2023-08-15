def method(arg: str | int):
    if type(arg) is str:
        print(f'{arg} + "*"')
    elif type(arg) is int:
        print(arg + 1)
    else:
        raise TypeError('Unknown data type')


