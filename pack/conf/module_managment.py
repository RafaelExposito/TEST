import os
import sys
import pathlib
import inspect


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


'''

file_path = pathlib.Path(__file__)
file_path_parent= pathlib.Path(__file__).parents

print('FILEPATH',file_path)
print('FILEPATH',type(file_path_parent))

file_child = []
for child in file_path_parent:
    file_child.append(child)
    print(child)

file_path_parent=file_path.parent.parent
dirs = [e for e in file_path_parent.iterdir() if e.is_dir()]
print(dirs)

file_path_parent=file_path.parent
print(file_path_parent)

files = [e for e in file_path_parent.iterdir() if e.is_file() ]
print("FILES",files)

for e in file_path_parent.rglob('*__.py'):
    print("EEE",e)


for e in file_path_parent.iterdir():
    if e.is_file():
        print("AAAAAAA",e,type(e))
        if e.rglob('*__.py')!='':
            print("BBBBBB", e)

num=0
print("CCCCCCCCCC", files[num].glob('*__.py'))

files_to_exclude=[]
for items in file_path_parent.rglob('*__.py'):
    files_to_exclude.append(items)
    print ("DDDDDDD",items)

print('files_to_exclud',files_to_exclude)

print("FILE",(files[2] in files_to_exclude))

for items in file_path_parent.iterdir():
    print ("FFFFFF",items,type(items))
    if (items.rglob('*__.py') in files_to_exclude)==True:
        print("items",(items))
    elif (items in files_to_exclude)==False:
        print("NO",items)

for items in file_path_parent.rglob('__init__.py'):
    print ("DDDDDDD",items)
'''

file_path = pathlib.Path(__file__)
file_path_parent = file_path.parent
files_to_exclude=[]

for items in file_path_parent.rglob('*__.py'):
    files_to_exclude.append(items)
    print ("DDDDDDD",items)



'''
for items in file_path_parent.iterdir():
    if (items in file_path_parent.rglob('*__.py'))==True:
        print ("AABABABABA",items)
'''

exclude=['*__.py']

def mm_find_modules(__file__):
    file_path = pathlib.Path(mm_get_path(__file__))
    file_path_parent = file_path

    excluded_files=[]
    included_files=[]

    for items in file_path_parent.iterdir():

        if items.is_file():
            for i in range(0, len(exclude)):
                if (items in file_path_parent.rglob(exclude[i])) == True:
                    print("items correcto", items)
                    excluded_files.append(items.stem)
                else:
                    print("item erroneo", items)
                    included_files.append(items.stem)
    print("included_files",included_files)
    print("excluded_files",excluded_files)
    return included_files


def mm_get_path(__file__):
    currentdir = os.path.dirname(os.path.realpath(__file__))
    print("currentdir", currentdir)
    return currentdir


'''
import inspect
import file_managment


#print(inspect.getmembers(__file__)) #module members

#print(inspect.getmodulename(__file__)) #module name

print(inspect.getmodulename(__file__)) #module name

print(inspect.signature(mm_get_path)) #function arguments


print(inspect.getmembers(file_managment))
members_file=inspect.getmembers(file_managment)

for items in members_file:
    print(items,'\t',type(items),'\t',inspect.isbuiltin(items),'\n')

for keys in members_file:
    print(keys,'\t',type(keys),'\t',inspect.isbuiltin(keys),'\n')

def ismodulefunction(module, member):
#    eval("import "+str(module))

    module_member = getattr(module, member)

    member_type = type(module_member).__name__
    print(member)
    return member_type == "function" or member_type == "builtin_function_or_method"
'''
'''

function_list = [member for member in dir(file_managment) if ismodulefunction(file_managment, member)]
print("function",function_list)



members_file=file_managment
print(members_file)

print(dir(members_file))

members_file=dir(members_file)


import  pip
import  build


print(pip.__version__)
print(build.__version__)

'''

import sys
import subprocess
import pkg_resources

required = {'pip', 'gTTS'}
installed = {pkg.key for pkg in pkg_resources.working_set}
missing = required - installed

print(missing)

if missing:
    python = sys.executable
    #subprocess.check_call([python, '-m', 'pip', 'install', *missing, "--version"], shell=True)

    #subprocess.run(' python -m pip --version', shell=True)


import platform

'''
list_exe=[
    platform.machine(),
    platform.node(),
    platform.platform(),
    platform.processor(),
    platform.python_build(),
    platform.python_compiler(),
    platform.python_branch(),
    platform.python_implementation(),
    platform.python_revision(),
    platform.python_version(),
    platform.python_version_tuple(),
    platform.release(),
    platform.system(),
    platform.version(),
    platform.win32_ver(release='', version='', csd='', ptype=''),
    platform.win32_edition()
]
'''


print(platform.python_version_tuple())
print(platform.node())
import pkgutil


print(pkgutil.get_loader("winnt"))



'''
for items in list_exe:
    print(items)
import pkgutil

print(pkgutil.iter_modules(path=None, prefix=''))

for items in pkgutil.iter_modules(path=None, prefix=''):
    print(items)





for items in pkgutil.iter_modules(path=["C:\\Users\\usuario\\AppData\\Local\\Programs\\Python\\Python38\\lib\\site-packages"], prefix=''):
    #print(items)
    if items[1]=="pip":             
        print(items)

'''




'''
for items in members_file:
    print(items,'\t',type(items),'\t',inspect.isbuiltin(items),'\n')

'''

members=inspect.getmembers(__file__)

'''for items in members:
    print(items,'\n')
'''
'''


mm_get_path(__file__)
mm_find_modules(__file__)


    file_path = pathlib.Path(mm_get_path(__file__))
    file_path_parent = file_path.parent
    for items in file_path_parent.iterdir():
        #print("FFFFFF", items, type(items))
        if (items.rglob('*__.py') in files_to_exclude) == True:
            print("items", (items))
        elif (items in files_to_exclude) == False:
            print("NO", items.name)
            
            
            
print(os.getcwd())
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
print("parentdir",parentdir)
print("currentdir",currentdir)


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

print(getSpecificParentDir(__file__,'TEST'))



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

'''

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