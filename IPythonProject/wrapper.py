__author__ = 'SilviyaSoti'

import os
import shutil

from git import *


# class for getting data from a repository
class RepositoryWrapper():

    def __init__(self, name, url):
        self.name = name
        self.url = url
        pass

    def clone_repos(self):
        remote_url = self.url
        temp_path = os.path.dirname(os.path.realpath("IPythonProject"))
        path_project = temp_path + "/" + self.name
        print path_project

        repo = Repo.init(path_project)
        origin = repo.create_remote('origin', remote_url)
        origin.fetch()
        origin.pull(origin.refs[0].remote_head)