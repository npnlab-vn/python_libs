from pip._internal.cli.main import main
from os import listdir
from os.path import isfile, join
import os

# print(os.path.basename("python_libs\libs"))

mypath = os.path.basename("python_libs\libs")
onlyfiles = [(mypath + '/' +f) for f in listdir(mypath) if isfile(join(mypath, f))]

print("Installing packages...")
print("==================================")
main(['install', '--no-index', '--find-links="python_libs\libs"'] + onlyfiles)
print("==================================")
print("Successfully installed packages!!!")