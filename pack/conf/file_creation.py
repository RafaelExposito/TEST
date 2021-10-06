import json


class TomlFileCreation:
    def __init__(self):
        self.head=""
        self.build_system=""
        self.requires = []
        self.build_backend = ""


    def add(self):
        self.head = "[build-system]"

    def add_build_backend(self,build):
        self.build_backend = build

    def add_requires(self,requirment):
        self.requires.append(requirment)

class BuildSystem:
    def __init__(self):
        self.build_system = ""

class GetTomlFileConf:
    def __init__(self):
        self.build_system=""
        self.requires = []
        self.build_backend = ""

    def setat(self,name,value):
        self.__setattr__(name,value)


    def get_data(self):
        with open('default.json') as file:
            data = json.load(file)
            print('data:', data)
            for keys in data:
                print('keys:', keys)

                for items in data[keys]:
                    print('items:', items)

                    for keys in data:
                        print('keys:', keys)


        self.head = "[build-system]"


z=GetTomlFileConf()

z.setat("rafa",1)

z.get_data()



print(dir(z))

import json

import toml

import setuptools
import wheel

from wheel import __version__ as wheel_version
from setuptools import __version__ as setuptools_version


print(wheel_version)
print(setuptools_version)


with open("default.json") as source:
    config = json.loads(source.read())

toml_config = toml.dumps(config)


with open("conf2.toml", 'w') as target:
    target.write(toml_config)


'''
with open('conf3.toml', 'w') as file:
    json.dump(config, file, indent=4,separators=(". ", " = "))
'''

with open('conf3.toml', 'w') as target:
    target.write(toml_config)


for keys in config:
    print(keys)

with open("conf2.txt", 'w') as target:
    target.write(str(config))


print(config)
a = {"name" : "GeeksforGeeks"+"\n", "Topic" : "Json to String", "Method": 1}
y = json.dumps(a)

print(ascii(y))


a=toml.load("pyproject.toml")
print("pyproject.toml",type(a),a)

with open('conf4.json', 'w') as file:
    json.dump(a, file, indent=4)

toml_config = toml.dumps(a)

with open('conf4.toml', 'w') as target:
    target.write(toml_config)



with open("co1", newline='\n') as source:
    config = json.loads(source.read())



toml_config = toml.dumps(config)

with open("conf22.toml", 'w') as target:
    target.write(toml_config)


with open("default.json", newline='\n') as source:
    config = json.loads(source.read())


with open("default.json") as source:
    config2 = json.loads(source.read())
    print("keys", config2, type(config2))

for keys in open("default.json"):
    print("keys",keys, type(keys))

with open("default.json") as source:
    config2 = json.loads(source.read())

print("keys", config2, type(config2))

for keys in config2:
    print(keys)
    for items in config2[keys]:
        print(items)

print(dir(config2))


fil=open("setup.cfg","r")

data={}
print(fil)
for items in fil:
    print(items)
    data[str(items)]=items



print(data)


import configparser


config = configparser.ConfigParser()
config.read('setup.cfg')

print(dir(config))

print(config.sections())

for key in config:
     print(key)

print(config.__iter__)

for items in config["metadata"]:
    print(items,type(items),config["metadata"][items])


'''
f=open('pyproject.toml','w')
f.write('[build-system]\n')
f.write('requires = [\n')
f.write('  "setuptools >= 40.9.0",\n')
f.write('  "wheel",\n')
f.write(']\n')
f.write('build-backend = "setuptools.build_meta"\n')

print("%s" % "[build-system]")
print("  ""%s" % "setuptools >= 40.9.0")

tom=TomlFileCreation()
tom.add_build_backend("setuptools.build_meta")

print(tom.build_backend)


tom.add_requires("wheel")
print(tom.requires)

import json


data = {}

data['ref'] = {}
data['[build_system]'] = []
data['[build_system]'].append({
    'requires': ['setuptools >= 40.9.0','wheel']
}
)

data['build_backend'] = []
data['build_backend'].append({
    'build_backend': ['setuptools.build_meta']
}
)
with open('data.json', 'w') as file:
    json.dump(data, file, indent=4)

[build-system]
requires = [
  "setuptools >= 40.9.0",
  "wheel",
]
'''

#build-backend = "setuptools.build_meta"

'''

with open('data.json', 'w') as file:
    json.dump(data, file, indent=4)



with open('data.json') as file:
    data = json.load(file)
    for build_system in data['[build_system]']:
        print('requires:', build_system['requires'])
        for items in build_system['requires']:
            print('items:', items)



with open('data.json') as file:
    data = json.load(file)
    for items in data:
        print('items:', items)


print(data['[build_system]'])


print(type(data['[build_system]']))

print(data['[build_system]'][0])


with open('default.json') as file:
    data = json.load(file)
    for items in data['[build_system]']:
        print('items:', items)

with open('default.json') as file:
    data = json.load(file)
    for items in data:
        print('items data:', items)

import json

import toml

with open("default.json") as source:
    config = json.loads(source.read())


with open("conf1.toml", "w") as f:
    f.write(toml.dumps(config))

'''