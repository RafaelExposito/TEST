import subprocess
import os
import sys
from os.path import abspath, dirname, join


print('CURRENT PLACE',os.getcwd())



BUILD_DIR= 'C:/Users/usuario/Desktop/TEST'
MODULE_NAME='build'
os.chdir(BUILD_DIR)
print('CURRENT PLACE',os.getcwd())


'''
os.chdir('c:/users/usuario/appdata/local/programs/python/python38/lib/site-packages')
subprocess.run('python -m pip uninstall pack',shell=True)
print('--------------------------------------------------------')
os.chdir('C:/Users/usuario/Desktop/TEST/dist')

print('--------------------------------------------------------')
subprocess.run('python -m pip install pack-0.0.0-py3-none-any.whl --force-reinstall',shell=True)
print('--------------------------------------------------------')
subprocess.run('pip install --upgrade pack',shell=True)
print('--------------------------------------------------------')
subprocess.run('pip install --upgrade --force-reinstall pack-0.0.0-py3-none-any.whl',shell=True)
print('--------------------------------------------------------')
subprocess.run('pip install --ignore-installed pack-0.0.0-py3-none-any.whl',shell=True)
'''
#os.chdir('C:/Users/usuario/Desktop/TEST/dist')
#subprocess.run('pip install --root C:/ pack-0.0.0-py3-none-any.whl --force-reinstall',shell=True)
os.chdir('C:/Windows/System32')
#subprocess.run('pip install pack-0.0.0-py3-none-any.whl --force-reinstall',shell=

subprocess.run('python -m pip install -U C:/Users/usuario/Desktop/TEST/dist/pack-0.0.0-py3-none-any.whl --force-reinstall',shell=True)



#subprocess.run('python -m pip install  TEST',shell=True)

#python -m pip install
#C:\Users\usuario\AppData\Local\Programs\Python\Python38\Lib\site-packages

