import codecs
import json
import os

import sys
from git import Repo
from IPythonProject.wrapper import RepositoryWrapper
from IPythonProject.readability import ReadabilityAnalysis


class LicenseAnalysis:
    def __init__(self):  # , name):
        # self.name = name
        pass

    def create_repo(self):
        temp_path = os.path.dirname(os.path.realpath("IPythonProject"))
        path_project = temp_path + "\\NewGitHubProjects2" + "\\" + self.name
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

    def check_ipynb(self, find_file):
        ipynb_paths = []
        ipynb_json = []
        for root, dirs, files in os.walk(find_file):
            for file in files:
                if 'π' in file:
                    file = file.replace('π', str('π'.encode("utf-8")))
                if ".ipynb" in file and os.path.join(root, file) is not None:
                    # print(file)
                    found_path = os.path.join(root, file)
                    ipynb_paths.append(found_path)
                    # found_path = str(found_path.encode("utf-8"))
                    print(file)
                    with open(found_path) as data_file:
                        file_json = json.load(data_file)
                    data_file.close()
                    ipynb_json.append(file_json)

            # for dir in dirs:
            #     for root2, dirs2, files2 in os.walk(find_file + "\\" + dir):
            #         for file2 in files2:
            #             if 'π' in file2:
            #                 file2 = file2.replace('π', str('π'.encode("utf-8")))
            #             if ".ipynb" in file2 and os.path.join(root, file2) is not None:
            #                 found_path = os.path.join(root2, file2)
            #                 ipynb_paths.append(found_path)
        return ipynb_paths, ipynb_json

    def traverse_projects(self):
        repo_path = os.path.dirname(os.getcwd())
        find_file = repo_path + "\IPythonProject\\NewGitHubProjects2"

        repos_license_no = []
        repos_license_yes = []

        for dirs in os.listdir(find_file):
            ra = ReadabilityAnalysis(find_file + "\\" + dirs)
            license_text, readme_file = ra.extract_text(find_file + "\\" + dirs)
            if not readme_file:
                repos_license_no.append(dirs)
            else:
                repos_license_yes.append(dirs)

        return repos_license_yes, repos_license_no

    def cell_types(self, ipynb_json):
        code_yes = 0
        code_no = 0
        all_ratios = []
        for script in ipynb_json:
            cells = script["worksheets"][0]["cells"]
            for cell in cells:
                cell_type = cell["cell_type"]
                if cell_type == "code":
                    code_yes += 1
                else:
                    code_no += 1
            all_ratios.append(str(code_yes)+":"+str(code_no))
            code_yes, code_no = 0, 0
        return all_ratios

repo = LicenseAnalysis()
# repos_license_yes, repos_license_no = repo.traverse_projects()
# print(repos_license_yes)
# print(repos_license_no)
repo_path = os.path.dirname(os.getcwd())
find_file = repo_path + "\IPythonProject\\NewGitHubProjects"
ipynb_paths, ipynb_json = repo.check_ipynb(find_file)
all_ratios = repo.cell_types(ipynb_json)
print("Cells ratio(code/no code): ", all_ratios, "\n")

# print(ipynb_json[0]["worksheets"][0]["cells"][0]["cell_type"])
