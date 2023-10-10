def decorate(func):
    def wrapper():
        print('I like only alcohol beer')
        func()

    return wrapper


@decorate
def real_function():
    print('I am real')


real_function()
