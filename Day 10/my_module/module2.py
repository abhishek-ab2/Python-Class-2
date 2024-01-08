# from . import module1
from .module1 import func_of_m1
from .nested_module.nested1 import CONFIG

def module2():
    print('Running module 2')
    func_of_m1()
