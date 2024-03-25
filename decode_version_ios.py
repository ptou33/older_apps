# looks for all .ipa files in directory, and gets version and ios compatibility, filtering minimum and maximum. ios for ipad3 is 9.3.6


import os
from zipfile import ZipFile
from pprint import pprint
import plistlib

root = "E:/Winpython/ipatool-py-master/"

find_keys = ["CFBundleShortVersionString", "MinimumOSVersion"]
results = []

for file in os.listdir(root):
    if file.endswith(".ipa"):
        file_name = root + file
        # print(file_name)
        with ZipFile(file_name, 'r') as zObject: 
            for file_in_zip in zObject.namelist():
                if file_in_zip.endswith(".app/Info.plist"):
                    f = zObject.open(file_in_zip)
                    data = f.read()
                    f.close()
                    pl = plistlib.loads(data)
                    results.append((file_name, pl[find_keys[0]], pl[find_keys[1]]))


results = list(filter(lambda x: float(x[2]) < 10, results))
results = list(filter(lambda x: float(x[2]) >= 9, results))
pprint(results)
