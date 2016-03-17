import json
import os
import requests
import time


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
            # print(item["commits_url"])
            commits_urls.append(item["commits_url"])
        return commits_urls

    def get_num_commits(self):
        commits_urls = self.get_commits_urls()
        commits_nums = []
        index = 1
        # traversing only for 10 repos
        while (index * 100) <= 1000:
            if index % 9 == 0:
                time.sleep(30)
            if index % 59 == 0:
                time.sleep(1800)

            request_data = requests.get(commits_urls[index])
            commits_dict = json.loads(request_data.text)
            commits_nums.append(commits_dict.values())
            index += 1

        return commits_nums


# ca = CommitsAnalysis()
# print(ca.get_num_commits())
