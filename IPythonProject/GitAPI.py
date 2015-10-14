__author__ = 'SilviyaSoti'

import requests
import json
import os.path


# fet the data from the GitHub API
def git_ipython_repos():
    json_data = "https://api.github.com/search/repositories?q=IPython+language:python&sort=stars&order=desc"
    request_data = requests.get(json_data)

    repoItem = {}
    if request_data.ok:
        # print "req content is ", request_data.content
        repoItem = json.loads(request_data.content)
        # print "repoItem is ", repoItem
        # print "Git JSON dictionary extracted: ", repoItem['total_count']

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
# git_ipython_repos()