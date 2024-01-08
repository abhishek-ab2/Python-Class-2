# class A:
#     address = 'asldkfjlsd'
#
#     def __init__(self):
#         self.a = 1
#         pass
#
#     def temp(self):
#         self.a = 9
#         pass
#
#     @classmethod
#     def k(cls):
#         cls.address = 96987
#         pass
#
#     @staticmethod
#     def method():
#         return 1
#
#
# a = A()
# a.a = 1
# a.temp() # Instance methods
# # print(a.a)
# A.k()
# print(A.address)
#
# print(A.method())



# class User:
#     storage_type = 'db'
#
#     def __init__(self, name, last_name=''):
#         self.name = name
#         self.last_name = last_name
#
#     def identify(self):
#         print(self.get_full_name(self.name, self.last_name))
#
#     def set_name(self, name):
#         self.name = name
#
#     @classmethod
#     def change_storage_type(cls):
#         cls.storage_type = 'cache'
#
#     @staticmethod
#     def get_full_name(first_name, last_name):
#         return f'Mr {first_name} {last_name}'
#
#
# User.storage_type = 'laskfjd'
#
# user1 = User('laskjfd')
# user1.set_name('new name')
# user1.identify()
# print(user1.storage_type)
#
# user2 = User('saldfk')
# user2.identify()
# print(user2.storage_type)

class Fish:
    number_of_fins = 2

    def __init__(self, color, name):
        self.color = color
        self.name = name

    def dance(self):
        print(f'{self.name} is dancing..')

    def introduce(self):
        print(f'I am {self.name}. I have {self.number_of_fins} fins')

    @classmethod
    def swim(cls):
        print(f'I am swimming')


class Shark(Fish):
    pass
    # def introduce(self):
    #     print(f'I am {self.name}. I am a shark')


class TigerShark(Shark):
    pass
    # number_of_fins = 4


# shark1 = TigerShark('Red', 'sharky')
# shark1.introduce()
# shark1.dance()
# shark1.swim()

class Amphibian:
    def fly(self):
        print('Flying')


class Frog(Amphibian):
    number_of_lungs = 8


class Bird:
    pass


class ModifiedCreature(Frog, Bird):
    pass


# c1 = ModifiedCreature('Blue', 'c1')
# c1.introduce()
# c1.swim()
# c1.fly()
# print(c1.number_of_lungs, c1.number_of_fins)

from abc import abstractmethod


class Human:
    address = 87098

    @abstractmethod
    def dance(self):
        raise NotImplementedError

    def dance_on_stage(self):
        self.dance()
        pass


class UrbanHuman(Human):
    def dance(self):
        print('Urban stlye')


class RuralHuman(Human):
    pass
    # def dance(self):
    #     print('Rural style')


h = RuralHuman()
h.dance()
h.dance_on_stage()
