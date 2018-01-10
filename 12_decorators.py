# The outer function (which is the name of the decorator) takes only the function
# itself as an argument, which is the function it's decorating. The inner takes the
# arguments of the called function, does any sort of processing it needs, and generally
# called the wrapped function with whatever arguments it wants
def ten_more(func):
    def inner(arg):
        return func(arg + 10)
    return inner

@ten_more
def add_5(num):
    return num + 5

print(add_5(10))


# Why use them?
def check_string(func):
    def inner(arg):
        if not type(arg) == str:
            raise Exception
        return func(arg)
    return inner


@check_string
def strfunc1(string):
    pass

@check_string
def strfunc2(string):
    pass

@check_string
def strfunc3(string):
    pass
