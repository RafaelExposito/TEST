import sys
import pathlib
import os


from pack import prog
from pack import folder
from pack import conf
from pack import development



#sys.path.append('C:\\Users\\usuario\\Desktop\\TEST\\pack')


#from prog import sumar

#from prog.sumar import suma

# cuando usas from pack import * estp es lo que se importa
#__all__ = ["folder","prog","conf","developtools"]



'''
print("helo")


print(dir(folder))
print(dir(prog))
print(dir(conf))
print(dir(sumar))



from folder import valores2
from prog import sumar
from prog import valores
from conf import *

from pack.folder import *
from pack.prog import *
from pack.conf import *
from pack.prog import sumar

import folder
import prog
import conf

from pack import folder
from pack import prog
from pack import conf




# defining variables to define path and others
file_parents = pathlib.Path(__file__).parents
#project_folder=file_parents[1].as_posix()
package_folder=file_parents[0].as_posix()
package_name=file_parents[0].name
'''

'''
project_folder=get_project_path(__file__,'pack')
add_path(project_folder)



sys.path.append('C:\\Users\\usuario\\Desktop\\TEST')
# import subpackages and others
from pack.folder import *
from pack.prog import *
from pack.conf import *


from pack import folder
from pack import prog
from pack import conf


'''


# definitions for get some attributes of the module
# __package__=file_parents[0].name
# __path__= package_folder


VERSION = (3, 2, 3, 'final', 0)
__name__="pack"
__version__ = '0.0.0'

def setup():
    print('HELLO!!!!!!!!!!!')