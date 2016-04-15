"""
Python class for accessing authors of commits and counting the different authors for a project.
:result: counting number of different authors of commits.
"""

import os
from git import Repo


class AuthorsOfCommits():
    def __init__(self):
        pass

    def get_number_contributors(self):
        """Method for getting number of authors for each repository.
        :return:
            Dictionary: {<repository_name>: <number_of_different_authors>}"""

        temp_path = os.path.dirname(os.path.realpath("IPythonProject"))
        path_project = temp_path + "\\NewGitHubProjects\\"
        number_authors = {}
        # a list for containing all the different contributors and if we need it
        # all_different_authors= []

        for dir in os.listdir(path_project):
            different_authors = []
            for d in os.listdir(path_project + "\\" + dir):
                repo = Repo(path_project + "\\" + dir + "\\" + d, search_parent_directories=True)
                if repo.active_branch.is_valid():
                    commits = list(repo.iter_commits())
                    for commit in commits:
                        commit_author = commit.author
                        if commit_author not in different_authors:
                            different_authors.append(commit_author)

            # a list for containing all the different contributors and if we need it
            # all_different_contributors.append(different_contributors)
            number_authors.update({dir: len(different_authors)})

        return number_authors

authors = AuthorsOfCommits()
print(authors.get_number_contributors())