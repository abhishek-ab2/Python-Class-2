
# file_obj = open('log.txt', 'w')
#
# # lines = file_obj.readlines()
#
# # line = file_obj.readline()
#
# data = file_obj.read()
# file_obj.close()
# print(data)


# file_obj = open('log-byte.txt', 'rb')
#
# # file_obj.write(b'aslkdfjasldfjlksdf')
# data = file_obj.read()
# file_obj.close()
#
# print(data)

# try:
#     file_obj = open('log.txt', 'r')
#     # operations which might raise exception
#
# except Exception:
#     pass
#
# finally:
#     file_obj.close()


# with open('log.txt', 'r') as file_obj:
#     data = file_obj.readlines()
#     print(data)

with open('log2.txt', 'r') as file:
    file.readlines()
    file.write()
