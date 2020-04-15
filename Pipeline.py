def pipeline(*funcs):
    funcs = [i for i in funcs[::-1]]

    def helper(arg):
        if funcs:
            arg = funcs.pop()(arg)
            if funcs:
                return helper(arg)
            else:
                return arg


    return helper


fun = pipeline(lambda x: x * 3, lambda x: x + 1, lambda x: x / 2)
print(fun(3))
# print(fun(3))
