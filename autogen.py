import subprocess
import os
import sys
from os.path import abspath, dirname, join


print('CURRENT PLACE',os.getcwd())


'''
BUILD_DIR= 'C:/Users/usuario/Desktop/TEST'
MODULE_NAME='build'
os.chdir(BUILD_DIR)

print('CURRENT PLACE',os.getcwd())


subprocess.run('pip install build',shell=True)

subprocess.run('cd C:/Users/usuario/AppData/Local/Programs/Python/Python38',shell=True)


sys.path.append(abspath('.'))
print(os.getcwd())



options=['-m',MODULE_NAME]
command= 'python' + ' ' + ' '.join(options)
print(command)
'''

command= 'python -m build'


command='python -m build C:/Users/usuario/Desktop/TEST --outdir C:/Users/usuario/Desktop/TEST/dist'

subprocess.run(command,shell=True)



'''
print('----------------------------------------------')
os.chdir('C:/Users/usuario/Desktop/TEST/dist')
subprocess.run('pip install --no-input pack-0.0.0-py3-none-any.whl --force-reinstall ',shell=True)
print('----------------------------------------------')
'''
#subprocess.run('pip install  pack-0.0.0-py3-none-any.whl --force-reinstall ',shell=True)



#python -m pip install
#C:\Users\usuario\AppData\Local\Programs\Python\Python38\Lib\site-packages

