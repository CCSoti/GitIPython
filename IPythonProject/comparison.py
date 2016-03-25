import os

import distance as distance

from IPythonProject.license_analysis import LicenseAnalysis


class Comparison:
    def __init__(self):  # , name):
        pass

    def get_scripts(self):

        repo_path = os.path.dirname(os.getcwd())
        find_file = repo_path + "\IPythonProject\\NewGitHubProjects2"
        repo = LicenseAnalysis()
        ipynb_files, ipynb_json = repo.check_ipynb(find_file)

        return ipynb_files, ipynb_json

    def get_cells_input(self):
        ipynb_files, ipynb_json = self.get_scripts()
        ipynb_dict = {}
        item = 0

        # traverse the scripts' cells
        for script in ipynb_json:
            if "worksheets" in script:
                cells = script["worksheets"][0]["cells"]
            else:
                cells = script["cells"]

            script_cell_input = []
            for cell in cells:

                if cell["cell_type"] == "code":
                    cell_input = cell["input"]
                else:
                    cell_input = cell["source"]

                # cell_input_strip = []
                # for line in cell_input:
                #     line = line.split(" ")
                #     for word in line:
                #         cell_input_strip.append(word)

                script_cell_input.append(cell_input)

            ipynb_dict[ipynb_files[item]] = script_cell_input
            item += 1

        return ipynb_dict

    def script_cells_compare(self):
        ipynb_dict = self.get_cells_input()
        cells = ipynb_dict.values()
        keys = ipynb_dict.keys()
        keys = list(keys)
        script_index = 0
        all_words = {}

        for script in cells:
            cell_index = 0
            script_words = []
            while cell_index < len(script):
                current_cell = script[cell_index]
                for line in script:
                    words = {}
                    if script.index(line) != cell_index:
                        # words = [(w, current_cell.count(w)) for w in set(current_cell) if w in line]
                        words[(cell_index, script.index(line))] = (len(current_cell), len(line), distance.levenshtein(current_cell, line))
                        script_words.append(words)
                cell_index += 1
            all_words[keys[script_index]] = script_words
            script_index += 1

        return all_words

compare = Comparison()
print(compare.script_cells_compare())
