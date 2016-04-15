import os
from git import *

"""
Python class for tracking the activity of repositories, by the number of commits.
:result: counting number of commits in a repository.
"""

class CommitsAnalysis():

    def __init__(self):
        pass

    def get_number_of_commits(self):
        """Method for traversing repositories and counting their number of commits.
        :return:
            list: [integer, integer,...]
            A list with the number of commits for each repository."""

        temp_path = os.path.dirname(os.path.realpath("IPythonProject"))
        path_project = temp_path + "\\NewGitHubProjects\\"
        num_commits = []

        for dir in os.listdir(path_project):
            print("Directory: ", dir)
            for d in os.listdir(path_project + "\\" + dir):
                print("Directory inside: ", d)
                repo = Repo(path_project + "\\" + dir + "\\" + d, search_parent_directories=True)
                print(repo.active_branch.is_valid())
                if repo.active_branch.is_valid():
                    commits = list(repo.iter_commits())
                    num_commits.append(len(commits))

        return num_commits


commits_analysis = CommitsAnalysis()
print(commits_analysis.get_number_of_commits())
