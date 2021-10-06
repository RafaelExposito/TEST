"""This is docstring of test module"""
import os, sys

'''
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
'''

#sys.path.append(parentdir+'\\folder')
#print("SISTEMA",sys.path,"\n")

#sys.path.append('C:\\Users\\usuario\\Desktop\\TEST\\pack')

#sys.path.append('C:\\Users\\usuario\\Desktop\\TEST')




#import sys
#import pathlib

#PATH_USER = sys.path.append(pathlib.Path(__file__).parent.as_posix())
#print('PATH_USER',PATH_USER)




#sys.path.append('/pack/tests')
#sys.path.append('/pack/prog')
#print(pathlib.Path(__file__).as_posix())

#print(sys.path)

#import proy.pack.tests

#from proy.pack.tests.valores import *
#from pack.folder.valores import *
#from pack.folder.valores2 import resta


'''
from context import _conf
_conf()

sys.path.append('C:\\Users\\usuario\\Desktop\\TEST')

sys.path.append('C:\\Users\\usuario\\Desktop\\TEST')
sys.path.append('C:\\Users\\usuario\\Desktop\\TEST\\pack')

sys.path.append('C:\\Users\\usuario\\Desktop\\TEST')
sys.path.append('C:\\Users\\usuario\\Desktop\\TEST\\pack')

sys.path.append('C:\\Users\\usuario\\Desktop\\TEST')
sys.path.append('C:\\Users\\usuario\\Desktop\\TEST\\pack')


sys.path.append('C:\\Users\\usuario\\Desktop\\TEST')
sys.path.append('C:\\Users\\usuario\\Desktop\\TEST\\pack')

sys.path.append('C:\\Users\\usuario\\Desktop\\TEST')
from pack.folder.valores2  import *
'''


#import pack.folder.valores2

import pack
from pack.folder.valores2 import *
from pack.prog.valores import *

#numero=10
#print(setup.get_option_dict('install'))
#print(setup.__module__)



def suma(num1, num2):

    res = num1 + num2
    print(res)
    print(resta(num1,num2))

    return res


if __name__ == '__main__':
    print('DIIIIIIIIIIIIR', dir(pack))
    print(suma(1, 2))
    print(VALOR)


    print(pack.__all__)
    #print(pack.__builtins__)
    #print(pack.__cached__)
    print(pack.__doc__)
    print(pack.__file__)
    print(pack.__loader__)
    print(pack.__name__)
    print(pack.__package__)
    print(pack.__package__)
    print(pack.__spec__)
    print(pack.__version__)

    #print(os.environ)



    import os
    import pprint

    # Get the list of user's
    # environment variables
    env_var = os.environ

    # Print the list of user's
    # environment variables
    #print("User's Environment variable:")
    #pprint.pprint(dict(env_var), width=1)

    # Add a new environment variable
    os.environ['GeeksForGeeks'] = 'www.geeksforgeeks.org'
    os.environ['AAAA'] = 'AAAA'
    # Get the value of
    # Added environment variable
    print("GeeksForGeeks:", os.environ['GeeksForGeeks'])

    print("GeeksForGeeks:", os.environ['AAAA'])

    env=os.environ
    for items in env:
        print(items)


    #print(resta(1, 2))

    #conf_settings()

    #print(dir(VALOR))
    '''
    print("resta.__name__", resta.__name__)  #      resta
    print("__name__", __name__)  # __main__         __main__
    print("__file__", __file__)  # __file__         pack/prog/sumar.py
    print("__package__", __package__)  #            None
    print("__doc__", __doc__)  # return             This is docstring of test module

    
    __doc__
    __name__
    __package__
    __spec__
    __path__
    
    
    print(pack.__all__)
    print(pack.__builtins__)
    print(pack.__cached__)
    print(pack.__doc__)
    print(pack.__file__)
    print(pack.__loader__)
    print(pack.__name__)
    print(pack.__package__)
    print(pack.__package__)
    print(pack.__spec__)
    print(pack.__version__)
    
    
    
    '''
    from pack import prog
    from pack import folder

    print("--------------------------------------------------------------------------------")
    print("__package__", __package__)  # None
    print("__package__", prog.__package__)  # packacg name of the prog import
    print("__package__", prog.__name__)  # packacg name of the prog import
    print("__package__", dir(prog))
    print("__package__", folder.__package__)  # None
    print("__package__", __package__)  # None
    print("--------------------------------------------------------------------------------")
