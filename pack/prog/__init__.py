import os
import sys
import pathlib



'''
import sumar
import valores
sys.path.append('C:\\Users\\usuario\\Desktop\\TEST')
sys.path.append('C:\\Users\\usuario\\Desktop\\TEST\\pack')
'''

'''
from pack.prog.sumar import *
from pack.prog.valores import *

from pack.prog import *
from pack.prog import *

from pack.prog import sumar
from pack.prog import *


print("helo pack.prog")

print('DIR SUMAR',dir(sumar))
print('DIR VALORES',dir(valores))
'''



from pack.prog import sumar
from pack.prog import valores

#from pack.conf.module_managment import *

#mm_get_path(__file__)
#__all__=mm_find_modules(__file__)

__all__=["sumar","valores"]

'''
print(os.getcwd())
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
print(parentdir)
print(currentdir)

__all__=["sumar","valores"]

'''


'''
sys.path.append('C:\\Users\\usuario\\Desktop\\TEST')
from pack.prog.sumar import *
from pack.prog.valores import *
from pack.conf.file_managment import *

'''
# defining variables to define path and others
#file_parents = pathlib.Path(__file__).parents
#project_folder=file_parents[2].as_posix()
#package_folder=file_parents[0].as_posix()
#package_name=file_parents[0].name


#adding the project folder to path
#sys.path.append(project_folder)

# from <project package>.<sub package> import <module of sub package>


'''
project_folder=get_project_path(__file__,'pack')
add_path(project_folder)



from pack.conf.file_managment import *


print('BUSQUEDA',getSpecificParentDir(__file__,'TEST'))
print('BUSQUEDA',str(getSpecificParentDir(__file__,'TEST')))

# definitions for get some attributes of the module
__package__=package_name
__name__= package_name
__version__='0.0.0'
__path__=package_folder


sumar.__name__ = '__main__'


print("valores __path__",__path__)
print("valores __path__",__name__)
'''

