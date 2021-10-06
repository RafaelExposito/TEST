import subprocess
import os


os.chdir('C:/Users/usuario/Desktop/TEST')
print(os.getcwd())
#subprocess.run('python -m unittest -v C:/Users/usuario/Desktop/debugtoolsproy/microprojects/test/test_sum.py',shell=True)

#subprocess.run('python -m unittest -v C:/Users/usuario/Desktop/debugtoolsproy/microprojects/test/test_all.py',shell=True)
#subprocess.run('python -m unittest -v C:/Users/usuario/Desktop/debugtoolsproy/tests/projecttools_test/test_xmlreader.py',shell=True)
#subprocess.run('python -m unittest -v C:/Users/usuario/Desktop/debugtoolsproy/tests/test_probe.py',shell=True)
#print('--------------------------------------------------------')
#subprocess.run('python -m unittest -v C:/Users/usuario/Desktop/debugtoolsproy/tests/projecttools_test/suite_test.py',shell=True)

#subprocess.run('python -m unittest -v tests.projecttools_test.suite_test.suite',shell=True)
#subprocess.run('python -m unittest -v tests.projecttools_test.test_xmlreader.suite_test',shell=True)
subprocess.run('python pack/prog/sumar.py',shell=True)
#print('--------------------------------------------------------')

'''

print('--------------------------------------------------------')
subprocess.run('python -m unittest -v C:/Users/usuario/Desktop/debugtoolsproy/tests/test_all.py',shell=True)
'''

