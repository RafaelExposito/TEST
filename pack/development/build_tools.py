import subprocess
import os
import sys
from pathlib import Path
import sysconfig

'''
print(os.getcwd())
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
print(parentdir)
print(currentdir)
sys.path.append('C:\\Users\\usuario\\Desktop\\TEST\\pack')
sys.path.append('C:\\Users\\usuario\\Desktop\\TEST')
'''
'''
from settings import *


print('CURRENT PLACE', os.getcwd())

print(os.name)

print(os.getenv('HOME', default=None))

os.getenv('IDEA_INITIAL_DIRECTORY', default=None)  # getting the initial directory

print(os.getenv('IDEA_INITIAL_DIRECTORY', default=None))

os.chdir('C:/Windows/System32')

print('-------------------------------')
'''
useful_lista = [
    sysconfig.get_platform(),  # get the computer platform    win-amd64
    sysconfig.get_python_version(),  # get the python version     3.8
    sys.base_exec_prefix,
    # get the python executable directory path  C:\Users\usuario\AppData\Local\Programs\Python\Python38
    sys.executable,
    # get the python executable path  C:\Users\usuario\AppData\Local\Programs\Python\Python38\python.exe
    sys.platform,  # get the computer platform    win32
    sys.version  # get system version
]

'''

for items in useful_lista:
    print(items)

'''
print('-------------------------------')


subprocess_configuration = {
    "info": {"shell": False, "capture_output": True, "encoding": 'ascii', "stdout": None, "stderr": None,
             "timeout": None, "check": False, "input": None, "stdin": None, "cwd": None, "errors": None, "text": None,
             "env": None, "universal_newlines": None },

    "default": {"shell": False, "capture_output": False, "encoding": 'ascii', "stdout": None, "stderr": None,
                "timeout": None, "check": False, "input": None, "stdin": None, "cwd": None, "errors": None,
                "text": None, "env": None, "universal_newlines": None },

    "extra": {"shell": False, "capture_output": True, "encoding": 'ascii', "stdout": None, "stderr": None,
                "timeout": None, "check": False, "input": None, "stdin": None, "cwd": None, "errors": None,
                "text": None, "env": None}
}

def bt_subprocess_config_ckeck(subprocess_conf):

    # find if exist a configuration
    if (subprocess_conf in subprocess_configuration.keys()):
        print("SUB",subprocess_conf)

    for keys in subprocess_configuration[subprocess_conf]:
        if keys!=subprocess_configuration["default"]:
            print(keys)
    for keys in subprocess_configuration["default"]:
        print(subprocess_configuration["default"].keys())

    # searching the key in a configuration
    for keys in subprocess_configuration[subprocess_conf]:
        if not(keys in subprocess_configuration["default"].keys()):
            print(keys)
    final_dict = subprocess_configuration[subprocess_conf]
    num_keys = len(subprocess_configuration[subprocess_conf].keys())

    for keys in subprocess_configuration["default"]:
        if not(keys in subprocess_configuration[subprocess_conf].keys()):
            print(keys)
            final_dict[keys]=subprocess_configuration["default"][keys]
    print(final_dict)


    return num_keys



def bt_subprocess(command:str=None,subprocess_conf:str=None):
    res = subprocess.run(command,
                         shell=subprocess_configuration[subprocess_conf]["shell"],
                         capture_output=subprocess_configuration[subprocess_conf]["capture_output"],
                         encoding=subprocess_configuration[subprocess_conf]["encoding"],
                         stdout=subprocess_configuration[subprocess_conf]["stdout"],
                         stderr=subprocess_configuration[subprocess_conf]["stderr"],
                         timeout=subprocess_configuration[subprocess_conf]["timeout"],
                         check=subprocess_configuration[subprocess_conf]["check"],
                         input=subprocess_configuration[subprocess_conf]["input"],
                         stdin=subprocess_configuration[subprocess_conf]["stdin"],
                         cwd=subprocess_configuration[subprocess_conf]["cwd"],
                         errors=subprocess_configuration[subprocess_conf]["errors"],
                         text=subprocess_configuration[subprocess_conf]["text"],
                         env=subprocess_configuration[subprocess_conf]["env"],
                         universal_newlines=subprocess_configuration[subprocess_conf]["universal_newlines"]
                         )
    return res


def bt_get_python_exec_dir():
    python_exec_dir = sys.base_exec_prefix
    return python_exec_dir


def bt_get_python_exec():
    python_exec = sys.executable
    return python_exec


def bt_get_init_dir():
    execution_dir = os.getenv('IDEA_INITIAL_DIRECTORY', default=None)
    return execution_dir


def bt_build(project_path: str = None, output_path: str = None):
    if (Path(project_path).exists()) and (Path(output_path).exists()):
        current_dir = os.getcwd()
        execution_dir = bt_get_init_dir()
        os.chdir(execution_dir)
        arg = ["python -m build", str(project_path), "--outdir", str(output_path) + '/dist']
        command = " ".join(arg)
        subprocess.run(command, shell=True)
        os.chdir(current_dir)
    return None


def bt_build_help():
    current_dir = os.getcwd()
    execution_dir = bt_get_init_dir()
    os.chdir(execution_dir)
    arg = ["python -m build", "--help"]
    command = " ".join(arg)
    subprocess.run(command, shell=True)
    os.chdir(current_dir)
    return None


def bt_build_version(subprocess_conf):
    current_dir = os.getcwd()
    execution_dir = bt_get_init_dir()
    os.chdir(execution_dir)
    arg = ["python -m build", "--version"]
    command = " ".join(arg)
    bt_subprocess(command,subprocess_conf)
    os.chdir(current_dir)
    return None



# bt_get_init_dir()
#bt_build("C:/Users/usuario/Desktop/TEST", "C:/Users/usuario/Desktop/TEST")
# bt_build_help()
bt_build_version("info")
# bt_get_python_exec_dir()
bt_subprocess_config_ckeck("extra")





'''
print('CURRENT PLACE',os.getcwd())
command='python -m build C:/Users/usuario/Desktop/TEST --outdir C:/Users/usuario/Desktop/TEST/dist'

subprocess.run(command,shell=True)

os.chdir('C:/Windows/System32')
print('CURRENT PLACE',os.getcwd())
#subprocess.run('python -m pip  install -U C:/Users/usuario/Desktop/TEST/dist/pack-0.0.0-py3-none-any.whl --force-reinstall',shell=True)

subprocess.run('python -m pip install -t C:/Users/usuario/AppData/Local/Programs/Python/Python38/Lib/site-packages C:/Users/usuario/Desktop/TEST/dist/pack-0.0.0-py3-none-any.whl --force-reinstall --upgrade',shell=True)
'''
