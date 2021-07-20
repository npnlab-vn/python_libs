from pip._internal.cli.main import main
from os import listdir
from os.path import isfile, join
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
current_dir = os.path.basename(dir_path)

packpath = os.path.basename(str(current_dir) + "\libs")
packages = [(packpath + '/' + f) for f in listdir(packpath) if isfile(join(packpath, f))]

libpath = os.path.basename(str(current_dir) + "\envLibs")
libs = [(libpath + '/' + f) for f in listdir(libpath) if isfile(join(libpath, f))]

print("Setting environment...")
print("==================================")
main(['install', '--no-index', '--find-links="' + current_dir + '\envLibs"'] + libs)

print("Installing packages...")
print("==================================")
main(['install', '--no-index', '--find-links="' + current_dir + '\libs"'] + packages)
print("==================================")
print("Successfully installed packages!!!")