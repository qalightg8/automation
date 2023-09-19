def tag(tag_name):
    def real_decorator(func):
        def wrapped():
            s = func()
            return f'<{tag_name}>{s}</{tag_name}>'

        return wrapped

    return real_decorator


def decorator(func):
    def wrapped():
        s = func()
        return f'<sdgsdg>{s}</sdgsdg>'

    return wrapped


@decorator
@tag('html')
def f():
    return 'Hello world!'


# x = decorator(tag(f()))

# print(f())


def get_word(word):
    return word


print(get_word(word='Hello'))
