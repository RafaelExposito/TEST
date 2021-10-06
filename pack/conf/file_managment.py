import os
import sys
import pathlib
import inspect
import inspect
sys.path.append('C:\\Users\\usuario\\Desktop\\TEST')
def get_project_path(__file__,find):
    parents = pathlib.Path((__file__)).parents
    final_parent=''
    for i in range(0, len(parents)):
        if parents[i].name==find:
            final_parent=parents[i]
            break
    return final_parent.as_posix()

def add_path(path):
    sys.path.append(path)


def get_Childrens(__file__,find):
    file_path = pathlib.Path(__file__)
    file_path_parent = file_path.parents
    file_child=[]
    for child in file_path_parent:
        file_child.append(child)
    print(file_child)

    return file_child





res2=get_project_path(__file__,'pack')

add_path(res2)
print(sys.path)


sys.path.append(res2)
file_path = pathlib.Path(__file__)
file_path_parent= pathlib.Path(__file__).parents

print('FILEPATH',file_path)
print('FILEPATH',type(file_path_parent))

file_child = []



for child in file_path_parent:
    file_child.append(child)

print('__file__',file_child)

p = pathlib.Path(os.getcwd())
print('p',p)
for child in p.iterdir():
    print('child',child)


print(file_child)


print(get_project_path(__file__,'TEST'))



os.chdir(os.getcwd())
print(os.getcwd())


search=pathlib.Path((__file__)).parent.parent

print('SEARCH',search)

#print(getSpecificParentDir(__file__,'TEST'))



p = pathlib.WindowsPath(os.getcwd())

for child in p.iterdir():
    print('child',child)

for parents in p.parents:
    print(parents.parents)

print('parents', p)
print('parents', p.parents)
print('parents', len(p.parents))

for i in range (0,len(p.parents)):
    print('ITEMS',p.parents[i])

#Se establece durante el inicio de Python, antes de que se ejecute site.py, en el mismo valor que exec_prefix.
print('ITEMS',sys.base_exec_prefix)
#Se establece durante el inicio de Python, antes de que se ejecute site.py, al mismo valor que prefix
print('ITEMS',sys.base_prefix)
#Una cadena de caracteres que proporciona el prefijo de directorio específico del sitio donde están instalados los archivos Python dependientes de la plataforma

print('ITEMS',sys.exec_prefix)

#Una cadena de caracteres que proporciona la ruta absoluta del binario ejecutable para el intérprete de Python
#None or string
print('ITEMS',sys.executable)

print('ITEMS',sys.getwindowsversion())

#Un objeto que contiene información sobre la implementación del intérprete de Python en ejecución.
print('ITEMS',sys.implementation)

#Este es un diccionario que asigna los nombres de los módulos a los módulos que ya se han cargado.
print('ITEMS',sys.modules)

#Una lista de cadenas de caracteres que especifica la ruta de búsqueda de módulos. Inicializado desde la variable de entorno PYTHONPATH, más un valor predeterminado que depende de la instalación.
print('ITEMS',sys.path)
print('ITEMS','----------------------------------------')
#Un diccionario que actúa como caché para objetos finder.
print('ITEMS',sys.path_importer_cache)

#Una cadena de caracteres que proporciona el prefijo de directorio específico del sitio donde se instalan los archivos Python independientes de la plataforma
print('ITEMS',sys.prefix)

#Una cadena de caracteres que contiene el número de versión del intérprete de Python más información adicional sobre el número de compilación y el compilador utilizado.
print('version',sys.version)

print('version_info',sys.version_info)
print('api_version',sys.api_version)
print('_xoptions',sys._xoptions)

import sysconfig


print('_xoptions',sysconfig.get_scheme_names())

print('_xoptions',sysconfig.get_python_version())

print('get_platform',sysconfig.get_platform())

import os

print('get_exec_path',os.get_exec_path())

print('pathconf_names',os.pardir)

import ensurepip



print('ensurepip.version()',ensurepip.version())

ensurepip.bootstrap(root=None, upgrade=False, user=False, altinstall=False, default_pip=False, verbosity=0)



'''
for root, dirs, files in os.walk(top=search, topdown=True, followlinks=True):
   for name in files:
      print(os.path.join(root, name))
   for name in dirs:
      print(os.path.join(root, name))

print('-------------------------------------------------------------------')

for root, dirs, files in os.walk(top=search, topdown=False, followlinks=True):
   for name in files:
      print(os.path.join(root, name))
   for name in dirs:
      print(os.path.join(root, name))

print('-------------------------------------------------------------------')



for root, dirs, files in os.walk(top=".", topdown=True, followlinks=True):
   for name in files:
      print(os.path.join(root, name))
   for name in dirs:
      print(os.path.join(root, name))

'''

'''
print(getSpecificParentDir2(__file__,'Desktop'))
for i in range(0,10):
    getParents2(__file__,'Desktop')
    print(i)




print(listPath())
print(getSpecificParentDir(__file__,'TEST'))
print(__file__)
print(getSpecificChildDir(__file__,'Desktop'))
print(__file__)
print(getRootByName(__file__,'Desktop'))
print(__file__)
print(getRootByName(__file__,'Desktop'))
'''