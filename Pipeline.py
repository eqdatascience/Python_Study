# Refactored code

def pipeline(*funcs):
    def helper(arg):
        temp = arg
        for func in funcs:
            temp = func(temp)
        return temp

    return helper


fun = pipeline(lambda x: x * 3, lambda x: x + 1, lambda x: x / 2)
print(fun(3))
# print(fun(3))
