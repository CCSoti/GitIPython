import json
import os


class CommitsAnalysis():

    def __init__(self):
        if os.path.exists("data_copy2.json") is True:
            with open('data_copy2.json') as outfile:
                json_dict = json.load(outfile)
            outfile.close()
            self.json_dict = json_dict

    def get_num_commits(self):
        json_dict = self.json_dict
        json_items = json_dict["items"]
        commits_urls = []

        for item in json_items:
            commits_urls.append(item["commits_url"])
        return commits_urls

ca = CommitsAnalysis()
print(len(ca.get_num_commits()))
