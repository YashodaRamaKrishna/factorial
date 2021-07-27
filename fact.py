


def fact(num):
    result = 1
    for i in range(2, num + 1):
        result *= i
    return result


print(fact(4))
















# def fact(num):
#     if num == 0:
#         return 1

#     else:
#         out = fact(num - 1) * num
#     return out


# print(fact(5))