import csv
import os
from statistics import stdev

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
            list: [[repository_name, integer],[...],...]
            A list with the name of each repository and number of commits for it."""

        temp_path = os.path.dirname(os.path.realpath("IPythonProject"))
        path_project = temp_path + "\\NewGitHubProjects\\"
        num_commits = []

        for dir in os.listdir(path_project):
            for d in os.listdir(path_project + "\\" + dir):
                repo = Repo(path_project + "\\" + dir + "\\" + d, search_parent_directories=True)
                if repo.active_branch.is_valid():
                    commits = list(repo.iter_commits())
                    num_commits.append([dir, len(commits)])

        return num_commits

    def store_number_of_commits_in_file(self):
        """Method for storing the name of the repository and its number of commits
        in a CSV file.
        :return:
            CSV file: number_of_commits.csv"""

        num_commmits = self.get_number_of_commits()
        with open("number_of_commits.csv", "w") as commits_file:
            spamwriter = csv.writer(commits_file)
            for commits in num_commmits:
                spamwriter.writerow(commits)
        commits_file.close()

    def calculate_average_of_commits(self):
        """Method for calculating the average of all commits.
        :return:
            Number: Integer"""

        number_of_commits = self.get_number_of_commits()
        sum = 0
        for commits in number_of_commits:
            sum += commits[1]
        average_commit = sum/len(number_of_commits)

    def calculate_standard_deviation(self):
        """Method for calculating the standard deviation of all commits.
        :return:
            Number: Integer"""
        commits_values = []
        number_of_commits = self.get_number_of_commits()
        for commit in number_of_commits:
            commits_values.append(commit[1])

        standard_deviation = stdev(commits_values)
        return standard_deviation


commits_analysis = CommitsAnalysis()
print(commits_analysis.calculate_standard_deviation())
