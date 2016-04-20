"""
Python class for identifying if a script is used for documentation or programming.
"""
import os
import json


class CodeVsText():
    def __init__(self):
        pass

    def check_ipynb(self, find_file):
        ipynb_files = []
        repositories_and_scripts_jsons = {}
        # for root, dirs, files in os.walk(find_file):
        for dir in os.listdir(find_file):
                files_in_repo = []
                for root2, dirs2, files2 in os.walk(find_file + "\\" + dir):
                    for file2 in files2:
                        if '?' in file2:
                            file2 = file2.replace('?', str('?'.encode("utf-8")))

                        if ".ipynb" in file2 and os.path.join(root2, file2) is not None:
                            found_path = os.path.join(root2, file2)
                            ipynb_files.append(found_path)
                            with open(found_path, encoding="utf8") as data_file:
                                file_json = json.load(data_file)
                            data_file.close()
                            files_in_repo.append(file_json)

                repositories_and_scripts_jsons.update({dir: files_in_repo})

        return ipynb_files, repositories_and_scripts_jsons

    def cell_types(self, ipynb_json):

        code_yes = 0

        code_no = 0
        all_ratios = []
        for script in ipynb_json:
            if "worksheets" in script and script["worksheets"] != []:
                cells = script["worksheets"][0]["cells"]
            elif "cells" in script.keys():
                cells = script["cells"]
            else:
                cells = []

            if cells != []:
                for cell in cells:
                    cell_type = cell["cell_type"]
                    if cell_type == "code":
                        code_yes += 1
                    else:
                        code_no += 1
                if code_no == 0:
                    all_ratios.append(1.0)
                elif code_yes == 0:
                    all_ratios.append(0.0)
                else:
                    if code_yes <= code_no:
                        all_ratios.append(code_yes/code_no)
                    else:
                        all_ratios.append(code_no/code_yes)
                code_yes, code_no = 0, 0

        return all_ratios

    def calculate_avg_codevstext_all_repos(self):
        pass

    def calculate_avg_codevstext_all_scripts(self):
        pass

    def main(self):
        repo_path = os.path.dirname(os.getcwd())
        find_file = repo_path + "\IPythonProject\\NewGitHubProjects2"
        ipynb_paths, repositories_and_scripts_jsons = codevstext.check_ipynb(find_file)

        all_scripts = 0
        all_scripts_ratios = 0
        all_repos_ratios = 0

        for repo in repositories_and_scripts_jsons:
            repo_ratios = 0
            scripts = repositories_and_scripts_jsons[repo]
            all_ratios = codevstext.cell_types(scripts)
            all_scripts += len(scripts)
            for ratio in all_ratios:
                all_scripts_ratios += ratio
                repo_ratios += ratio

            all_repos_ratios += repo_ratios/len(all_ratios)

        scripts_codevstext = (all_scripts_ratios/all_scripts)*100
        repos_codevstext = (all_repos_ratios/len(repositories_and_scripts_jsons))*100

        return scripts_codevstext, repos_codevstext


codevstext = CodeVsText()
print(codevstext.main())
