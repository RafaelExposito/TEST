import subprocess
import os
import sys
from os.path import abspath, dirname, join


os.chdir('c:/users/usuario/appdata/local/programs/python/python38/lib/site-packages')
print('CURRENT PLACE',os.getcwd())
os.chdir('c:/Windows/System32')
'''
subprocess.run('python -m pip uninstall pack',shell=True)
print('--------------------------------------------------------')
subprocess.run('pip uninstall pack',shell=True)
print('--------------------------------------------------------')
subprocess.run('pip --help',shell=True)
print('--------------------------------------------------------')
subprocess.run('pip show pack',shell=True)
print('--------------------------------------------------------')
subprocess.run('pip check pack',shell=True)
print('--------------------------------------------------------')
subprocess.call('python -m pip uninstall pack',shell=True)

'''
os.chdir('c:/users/usuario/appdata/local/programs/python/python38/lib/site-packages')

os.chdir('c:/Windows/System32')
# change the directory execution to Windows\System32
subprocess.run('python -m pip  uninstall --no-input pack --yes',shell=False)




os.chdir('C:/Users/usuario/Desktop/TEST/')
file=open('out.txt','w')
file_in=open('in.txt','w')



#print(subprocess.run('python -m pip  uninstall  pack --yes',shell=True,capture_output=False,stdout=file,stdin=file_in))


#uninstall_dependency=subprocess.Popen(["python","-m","pip","uninstall",'pack'],stderr=subprocess.PIPE,stdout=file, stdin=subprocess.PIPE)
#print(uninstall_dependency.returncode)
#print(uninstall_dependency.stdin.readable())

f=subprocess
file.close()
file_in.close()
'''
subprocess.run('python -m pip uninstall pack',shell=False,stdin=subprocess.PIPE,
                check=False,
                capture_output=True,
                input=None
               )

uninstall_dependency=subprocess.Popen(["python","-m","pip","uninstall",'pack'],stderr=subprocess.PIPE,stdout=subprocess.PIPE, stdin=subprocess.PIPE)

  install                     Install packages.
  download                    Download packages.
  uninstall                   Uninstall packages.
  freeze                      Output installed packages in requirements format.
  list                        List installed packages.
  show                        Show information about installed packages.
  check                       Verify installed packages have compatible dependencies.
  config                      Manage local and global configuration.
  search                      Search PyPI for packages.
  cache                       Inspect and manage pip's wheel cache.
  index                       Inspect information available from package indexes.
  wheel                       Build wheels from your requirements.
  hash                        Compute hashes of package archives.
  completion                  A helper command used for command completion.
  debug                       Show information useful for debugging.
  help                        Show help for commands.
  
subprocess.run('python -m pip install pack-0.0.0-py3-none-any.whl --force-reinstall',shell=True)
print('--------------------------------------------------------')
subprocess.run('pip install --upgrade pack',shell=True)
print('--------------------------------------------------------')
subprocess.run('pip install --upgrade --force-reinstall pack-0.0.0-py3-none-any.whl',shell=True)
print('--------------------------------------------------------')
subprocess.run('pip install --ignore-installed pack-0.0.0-py3-none-any.whl',shell=True)
'''
#subprocess.run('python -m pip install  TEST',shell=True)

#python -m pip install
#C:\Users\usuario\AppData\Local\Programs\Python\Python38\Lib\site-packages

