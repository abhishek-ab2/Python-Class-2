# variable = 10
# #
# #
# # def func():
# #     global variable
# #     variable = 12
# #     print(variable)
# #
# # func()
# # print(variable)
# var = 12
# def f1():
#     var1 = 10
#     def f2():
#         nonlocal var1
#         global variable, var
#         var1 = 12
#         variable = 12
#         print(var1)
#         print(variable)
#         def f3():
#             nonlocal var
#             pass
#     f2()
# f1()
#
#
#
#
# for i in range(100):
#     print(i)
#     if i > 10:
#         break
# else:
#     print('no unnatural interruption')


try:
    dct = {
        1:2
    }
    var = dct[1]
except Exception:
    pass
else:
    print('No exception was raised')
finally:
    print('Runs in all scenarios')
