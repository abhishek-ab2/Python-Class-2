import os
import stat


# os.chdir('temp')

current_path = os.getcwd()
# print(current_path)

# os.chmod('temp', stat.S_IWRITE)
# os.chown('lskjdfl', uid, gid)

print(current_path)
# print(list(os.walk(current_path)))

# filename = 'temp.txt'
# new_path = os.path.join(current_path, 'temp/temp.txt')
#
# print(os.path)

print(os.listdir(current_path))

