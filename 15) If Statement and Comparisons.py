def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3


print(max_num(200, 50, 5))


def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3


print(max_num(200, 5000, 5))


def max_num(num1, num2, num3):
    if num1 == num2 and num1 >= num3:  # equal
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3


print(max_num(500, 900, 1500))


def max_num(num1, num2, num3):
    if num1 != num2 and num1 >= num3:  # not equal
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3


print(max_num(2000, 500, 5))
