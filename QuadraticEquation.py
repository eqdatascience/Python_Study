# Implement the function find_roots to find the roots of the quadratic equation: ax2 + bx + c = 0.
# The function should return a tuple containing roots in any order.
# If the equation has only one solution, the function should return that solution as both elements of the tuple.
# The equation will always have at least one solution.


def find_roots(a, b, c):
    # The equation will always have at least one solution. dis > = 0
    dis = b ** 2 - 4 * a * c
    if dis > 0:
        return (-b + dis ** 0.5) / (2 * a), (-b - dis ** 0.5) / (2 * a)
    return -b / (2 * a), -b / (2 * a)


print(find_roots(2, 10, 8))
