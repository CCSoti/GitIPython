import json
import os

import requests


class CommitsAnalysis():

    def __init__(self):
        if os.path.exists("data_copy2.json") is True:
            with open('data_copy2.json') as outfile:
                json_dict = json.load(outfile)
            outfile.close()
            self.json_dict = json_dict

    def get_commits_urls(self):
        json_dict = self.json_dict
        json_items = json_dict["items"]
        commits_urls = []

        for item in json_items:
            commits_urls.append(item["commits_url"])
        return commits_urls

    def get_num_commits(self):
        commits_urls = self.get_commits_urls()
        commits_nums = []
        for url in commits_urls:
            request_data = requests.get(url)
            commits_dict = json.loads(request_data.text)
            commits_nums.append(len(commits_dict))
        return commits_nums


ca = CommitsAnalysis()
print(ca.get_num_commits())
