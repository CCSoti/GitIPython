import time

__author__ = 'SilviyaSoti'

import requests
import json
import os.path
from IPythonProject.wrapper import RepositoryWrapper



class GitHubParsing():
    def __init__(self):
        with open('data_copy2.json') as data_file:
            print(os.stat('data_copy2.json').st_size)
            if os.stat('data_copy2.json').st_size!=0:
                data = json.load(data_file)
                data_file.close()
                self.data = data

    # fetch the data from the GitHub API
    def git_ipython_repos(self):

        # pages_num = &per_page=100&page=
        json_data = "https://api.github.com/search/repositories?q=IPython&per_page=100&page=1"
        request_data = requests.get(json_data)
        print(type(request_data))

        repoItem = {}
        repos_num = 0
        if request_data.ok:
            repoItem = json.loads(request_data.text)
            items = repoItem["items"]
            repos_num = repoItem["total_count"]

            index = 2
            start_time = time.time()
            combined = items

            # we have a restriction, not more than 1000 results for a search
            while (index*100) <= 1000:
                if index % 9 == 0:
                    time.sleep(30)
                if index % 59 == 0:
                    time.sleep(1800)

                print(len(str(index)))

                if len(str(index)) == 1 or index == 10:
                    json_data = json_data[:-1]
                elif len(str(index)) == 2:
                    json_data = json_data[:-2]
                json_data += str(index)
                print("After:   ", json_data)

                request_data = requests.get(json_data)
                repoItem2 = json.loads(request_data.text)
                items2 = repoItem2["items"]

                combined += items2
                repoItem["items"] = combined

                index += 1


        if os.path.exists("data_copy2.json") is True:
            with open('data_copy2.json', 'w') as outfile:
                json.dump(repoItem, outfile)
            outfile.close()

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

    # get data for only num repositories using wrapper.py class
    def clone_repositories(self, repos_dict, num):

        index = 1
        repos_dict_keys = repos_dict.keys()
        time_sum = 0

        while index <= num:
            # check how much time has elapsed
            if index % 9 == 0:
                time.sleep(30)
                time_sum += 30
            if index % 59 == 0:
                time.sleep(1800)
                time_sum += 1800

            repos_dict_keys = list(repos_dict_keys)
            repo_name = repos_dict_keys[index]
            repo_url = repos_dict[repos_dict_keys[index]]

            start_time = time.time()
            repo_info = RepositoryWrapper(repo_name, repo_url)
            repo_info.clone_repos()  # changes
            clone_time = time.time() - start_time
            time_sum += clone_time
            print(time_sum, clone_time, index)
            index += 1

    def traverse_through_pages(self):
        git_parsing = GitHubParsing()
        data = git_parsing.data
        total_count = data["total_count"]

        index = 2
        while index <= total_count:
            index += 1

    # main method for calling all the functions we need
    def main(self):
        repos_dict = self.repos_urls()
        self.clone_repositories(repos_dict, 1000)


git_parsing = GitHubParsing()
# git_parsing.main()
repos = git_parsing.git_ipython_repos()
print(len(repos["items"]))
