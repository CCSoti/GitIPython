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

    def get_personal_projects(self):
        """Method for getting number of repositories, which have only 1 committer - they are personal projects.
        :return:
            Integer : {<repository_name>: <number_of_different_authors>}"""

        number_authors = self.get_number_contributors()
        personal_repositories = 0
        for repo in number_authors:
            repo_number_of_authors = number_authors[repo]
            if repo_number_of_authors == 1:
                personal_repositories += 1

        personal_repos_percentage = (personal_repositories/len(number_authors))*100
        return personal_repos_percentage

authors = AuthorsOfCommits()
print(authors.get_personal_projects())