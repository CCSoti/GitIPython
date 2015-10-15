__author__ = 'SilviyaSoti'

import os
import shutil

from git import *


# class for getting data from a repository
class RepositoryWrapper(): # changed

    def __init__(self, name, url):
        self.name = name
        self.url = url
        pass

    def clone_repos(self): # changes
        remote_url = self.url # push these changes from the meeting
        temp_path = os.path.dirname(os.path.realpath("IPythonProject"))
        path_project = temp_path + "/" + self.name
        print path_project

        repo = Repo.init(path_project)
        origin = repo.create_remote('origin', remote_url)
        origin.fetch()
        origin.pull(origin.refs[0].remote_head)