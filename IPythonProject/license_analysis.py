import os

from git import Repo

from IPythonProject.wrapper import RepositoryWrapper
from IPythonProject.readability import ReadabilityAnalysis


class LicenseAnalysis:
    def __init__(self, name):
        self.name = name
        pass

    def create_repo(self):
        temp_path = os.path.dirname(os.path.realpath("IPythonProject"))
        path_project = temp_path + "\\NewGitHubProjects" + "\\" + self.name
        print("Path: " + path_project)

        repo = Repo.init(path_project)
        return repo

    def traverse_repo(self):
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

    def traverse_projects(self):
        repo_path = os.path.dirname(os.getcwd())
        find_file = repo_path + "\IPythonProject\\NewGitHubProjects"

        repos_license_no = []
        repos_license_yes = []

        for dirs in os.listdir(find_file):
            ra = ReadabilityAnalysis(find_file + "\\" + dirs)
            license_text, readme_file = ra.extract_text(find_file + "\\" + dirs)
            if not readme_file:
                repos_license_no.append(dirs)
            else:
                repos_license_yes.append(dirs)

        print(repos_license_no)
        print(repos_license_yes)



repo = LicenseAnalysis("pydata")
repo.traverse_projects()
