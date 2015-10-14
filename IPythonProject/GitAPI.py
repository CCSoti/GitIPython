__author__ = 'SilviyaSoti'

import requests
import json
import os.path


# fetch the data from the GitHub API
def git_ipython_repos():
    json_data = "https://api.github.com/search/repositories?q=IPython+language:python&sort=stars&order=desc"
    request_data = requests.get(json_data)

    repoItem = {}
    if request_data.ok:
        repoItem = json.loads(request_data.content)

        if os.path.exists("data_copy.json") is False:
            with open('data_copy.json', 'w') as outfile:
                json.dump(repoItem, outfile)

    return repoItem


# method for fetching the data from the file
def get_data_from_file():
    with open('data_copy.json') as data_file:
        data = json.load(data_file)
    # print "Data is ", data
    return data


# get the urls for the GitHub repositories from the dictionary
def repos_urls(data):
    dict_items = data["items"]
    repos_dict = {}
    for item in dict_items:
        full_name = item["full_name"]
        clone_url = item["clone_url"]
        repos_dict[full_name] = clone_url

    return repos_dict

data = get_data_from_file()
print repos_urls(data)