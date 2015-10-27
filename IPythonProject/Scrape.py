__author__ = 'SilviyaSoti'

import requests
from bs4 import BeautifulSoup

scraped_url = "https://github.com/search?utf8=%E2%9C%93&q=IPython"

request_data = requests.get(scraped_url)

soup = BeautifulSoup(request_data.text)

search_links = []

for repo_text in soup.stripped_strings:

    if "repository results" in repo_text:
        print(repo_text, "\n")

for repo_name in soup.select("h3"):
    if repo_name.has_attr("class"):
        print("Name of the class: ", repo_name['class'])
        # usually the text is also the link to a specific result
        print("Text in the tag: ", repo_name.text)

for next_page in soup.select("a"):
    if next_page.has_attr("rel"):
        for next_element in next_page['rel']:
            if next_element == "next":
                next_text = next_page.text
                check_number = any(char.isdigit() for char in next_text)
                if check_number is True:
                    print("Next page: ", next_page)