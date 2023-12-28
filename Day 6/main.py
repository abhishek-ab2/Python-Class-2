# str1 = 'asjfsafs'
# str2 = 'asflsakdfj'
#
# str2 * str1


# class A:
#     pass
#
# a = A()
#
# print(a.name)

# expected_status = 200
# actual_status = 400
#
# assert expected_status == actual_status

# lst = [1,2,3,4]
#
# lst[45]

# dct = {1:2, 3:4}
# dct[9]

# print(var)

# def func():
#     print(var)
#     var = 12
#
# func()


# ------------------------------------
# Scopes

# global_var = 1
#
# def func():
#     local_var = 1
#     print(global_var)
#
# func()
#
# print(local_var)

# 1 / 0


# ------------
# Recursion
# When result of the function can be an argument function for performing same operation over and over

# def func():
#     var = func()
#     return 1


# def calc_exponent(number, exponent):
#     if exponent == 1:
#         return number
#
#     return number * calc_exponent(number, exponent-1)
#
# print(calc_exponent(4, 4))

