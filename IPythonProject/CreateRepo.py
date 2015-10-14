__author__ = 'SilviyaSoti'

import os
import shutil

from git import *

REMOTE_URL = "https://github.com/ipython/ipython.git"

temp_path = os.path.abspath("IPythonProject")
print temp_path
# print temp_path.replace('\\', '/')
# temp_path = temp_path.replace('\\', '/')

repo = Repo.init("C:/Users/SilviyaSoti/Documents/Level_5/PyCharm/IPythonProject/temp")
origin = repo.create_remote('origin', REMOTE_URL)
origin.fetch()
origin.pull(origin.refs[0].remote_head)

print "---- DONE ----"

