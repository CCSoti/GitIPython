import csv
import os
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
from statistics import stdev, mean

import time
from git import *

"""
Python class for tracking the activity of repositories, by analysis of commits.
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
        average_commit = sum / len(number_of_commits)

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

    def create_histogram_for_standard_deviation(self):
        """Method for showing the standard deviation of the number of commits in
        all repositories.
        :return:
            Matplotlib Object: histogram"""

        commits_values = []
        number_of_commits = self.get_number_of_commits()
        for commit in number_of_commits:
            commits_values.append(commit[1])

        mean_value = mean(commits_values)
        standard_deviation = self.calculate_standard_deviation()
        num_bins = 50
        n, bins, patches = plt.hist(commits_values, num_bins, normed=1, facecolor='green', alpha=0.5)
        # add a 'best fit' line
        y = mlab.normpdf(bins, mean_value, standard_deviation)
        plt.plot(bins, y, 'r--')
        plt.xlabel('Number of Commits')
        plt.ylabel('Probability')
        plt.title(r'Histogram of number of commits')

        # Tweak spacing to prevent clipping of ylabel
        plt.subplots_adjust(left=0.15)
        plt.show()

    def get_date_of_latest_commit_in_repository(self):
        """Method for getting the date of the latest commit in a repository..
        :return:
            Date Object: Date"""
        temp_path = os.path.dirname(os.path.realpath("IPythonProject"))
        path_project = temp_path + "\\NewGitHubProjects\\"
        latest_commits = {}

        for dir in os.listdir(path_project):
            for d in os.listdir(path_project + "\\" + dir):
                repo = Repo(path_project + "\\" + dir + "\\" + d, search_parent_directories=True)
                # print(time.strftime("%a, %d %b %Y %H:%M", time.gmtime(repo.head.commit.committed_date)))
                if repo.active_branch.is_valid():
                    commits = list(repo.iter_commits())
                    latest_commits.update({dir: commits})

        commits_dates_list = []
        latest_commits_dates_list = []
        for repo in latest_commits:
            commits_list = latest_commits[repo]

            commits_dates = {}
            for com in commits_list:
                com_time = time.strftime("%a, %d %b %Y %H:%M", time.gmtime(com.committed_date))
                com_date = time.strptime(com_time, "%a, %d %b %Y %H:%M")
                commits_dates.update({com_time: com_date})

            first_commit_date = min(commits_dates.values())
            latest_commit_date = max(commits_dates.values())
            first_commit = list(commits_dates.keys())[list(commits_dates.values()).index(first_commit_date)]
            latest_commit = list(commits_dates.keys())[list(commits_dates.values()).index(latest_commit_date)]

            commits_dates_list.append([first_commit_date, latest_commit_date])
            latest_commits_dates_list.append(latest_commit_date)

        return commits_dates_list, latest_commits_dates_list

    def analyse_the_latest_commits(self):
        """Method for getting the percentage of how many repositories which last activity is in 2015 or 2016.
        :return:
            Float number: represents a percentage."""

        commits_dates_list, latest_commits_dates_list = self.get_date_of_latest_commit_in_repository()
        count_close_years = []
        for latest_commit in latest_commits_dates_list:
            if latest_commit[0] == 2015 or latest_commit[0] == 2016:
                count_close_years.append((latest_commit[0]))

        average_of_close_years = (len(count_close_years)/len(latest_commits_dates_list))*100

        return average_of_close_years

commits_analysis = CommitsAnalysis()
print(commits_analysis.analyse_the_latest_commits())
