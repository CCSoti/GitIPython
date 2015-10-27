__author__ = 'SilviyaSoti'

import requests
import json
import os.path
from IPythonProject.wrapper import RepositoryWrapper


class GitHubParsing():
    def __init__(self):
        with open('data_copy_pythonlangsearch.json') as data_file:
            data = json.load(data_file)
        self.data = data

    # fetch the data from the GitHub API
    def git_ipython_repos(self):

        json_data = "https://api.github.com/search/repositories?q=IPython"  # &page=2
        request_data = requests.get(json_data)

        repoItem = {}
        if request_data.ok:
            repoItem = json.loads(request_data.text)

            if os.path.exists("data_copy.json") is False:
                with open('data_copy.json', 'w') as outfile:
                    json.dump(repoItem, outfile)

        return repoItem



    # get the urls for the GitHub repositories from the dictionary
    def repos_urls(self):

        dict_items = self.data["items"]
        repos_dict = {}
        for item in dict_items:
            full_name = item["full_name"]
            clone_url = item["clone_url"]
            repos_dict[full_name] = clone_url

        return repos_dict


    # get data for only 3 repositories using wrapper.py class
    def clone_repositories(self, repos_dict, num):

        index = 1
        repos_dict_keys = repos_dict.keys()
        while index <= num:
            repo_name = repos_dict_keys[index]
            repo_url = repos_dict[repos_dict_keys[index]]
            index += 1
            repo_info = RepositoryWrapper(repo_name, repo_url)
            repo_info.clone_repos()  # changes


    # main method for calling all the functions we need
    def main(self):
        git_parsing = GitHubParsing()
        repos_dict = git_parsing.repos_urls()
        git_parsing.clone_repositories(repos_dict, 3)


# main()