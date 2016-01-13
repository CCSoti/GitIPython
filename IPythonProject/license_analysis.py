import os

from git import Repo

from IPythonProject.wrapper import RepositoryWrapper


class LicenseAnalysis:
    def __init__(self, name):
        self.name = name
        pass

    def create_repo(self):
        temp_path = os.path.dirname(os.path.realpath("IPythonProject"))
        path_project = temp_path + "\GitHubProjects" + "\\" + self.name
        print("Path: " + path_project)

        repo = Repo.init(path_project)
        return repo

    def main(self):
        repo = self.create_repo()

        # explanation for the entries http://gitpython.readthedocs.org/en/stable/reference.html#module-git.index.base
        repo_dict = repo.index.entries
        # print(repo.untracked_files)
        # print(repo.index.entries)

        tree = repo.heads.master.commit.tree
        print(len(tree))
        # print(tree.blobs[0].name)
        for blob in tree.blobs:
            print(blob.name)
        for tre in tree:
            print(tre.name)



repo = LicenseAnalysis("vim-ipython")
repo.main()
