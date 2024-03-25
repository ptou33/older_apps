# looks for all .ipa files in directory, and gets version and ios compatibility, filtering minimum and maximum. ios for ipad3 is 9.3.6


import os
from zipfile import ZipFile
import plistlib
from tabulate import tabulate

### CONFIGURATION
root = "E:/Winpython/ipatool-py-master/"
filter_ios_version_min = 4
filter_ios_version_max = 5
###


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


results = list(filter(lambda x: float(x[2]) <= filter_ios_version_max, results))
results = list(filter(lambda x: float(x[2]) >= filter_ios_version_min, results))

headers = ["File", "Version", "IOS required"]
print(tabulate(results, headers, tablefmt="psql"))
