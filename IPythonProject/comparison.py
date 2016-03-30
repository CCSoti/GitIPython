import json
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

    def traverse_file(self, script):
        if "worksheets" in script:
            cells = script["worksheets"][0]["cells"]
        else:
            cells = script["cells"]

        script_cell_input = []
        for cell in cells:

            if cell["cell_type"] == "code":
                if "input" in cell.keys():
                    cell_input = cell["input"]
                else:
                    cell_input = cell["source"]
            else:
                cell_input = cell["source"]

                # cell_input_strip = []
                # for line in cell_input:
                #     line = line.split(" ")
                #     for word in line:
                #         cell_input_strip.append(word)

            script_cell_input.append(cell_input)

        return script_cell_input

    def get_cells_input(self):
        ipynb_files, ipynb_json = self.get_scripts()
        ipynb_dict = {}
        item = 0

        # traverse the scripts' cells
        for script in ipynb_json:
            script_cell_input = self.traverse_file(script)
            ipynb_dict[ipynb_files[item]] = script_cell_input
            item += 1

        return ipynb_dict

    def cells_compare(self):
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
                        words[(cell_index, script.index(line))] = (
                            len(current_cell), len(line), distance.levenshtein(current_cell, line))
                        script_words.append(words)
                cell_index += 1
            all_words[keys[script_index]] = script_words
            script_index += 1

        return all_words

    def scripts_compare(self, ipynb_dict):
        cells = ipynb_dict.values()
        keys = ipynb_dict.keys()
        keys = list(keys)
        scripts = {}
        cells = list(cells)
        traversed = []

        script_index = 0
        file_index = 0

        while script_index < len(cells):
            ratios = {}

            while file_index < len(cells):

                if file_index != script_index and script_index not in traversed:

                    for sc_line in cells[script_index]:
                        lines_diff = []
                        for line in cells[file_index]:
                            sc_line_ind = cells[script_index]
                            sc_line_ind = sc_line_ind.index(sc_line)
                            line_ind = cells[file_index]
                            line_ind = line_ind.index(line)

                            lines_diff.append((
                                len(sc_line), len(line), distance.levenshtein(sc_line, line)))

                        ratios[(script_index, file_index)] = lines_diff

                    scripts[keys[script_index] + ": " + keys[file_index]] = ratios
                file_index += 1

            traversed.append(script_index)
            script_index += 1

        return scripts

    def repos_scripts(self):
        repo_path = os.path.dirname(os.getcwd())
        find_file = repo_path + "\IPythonProject\\NewGitHubProjects2"
        repos_dict = {}

        for dir in os.listdir(find_file):
            scripts = []
            for root, dirs, files in os.walk(find_file + "\\" + dir):
                for file in files:
                    if 'π' in file:
                        file = file.replace('π', str('π'.encode("utf-8")))

                    if ".ipynb" in file and os.path.join(root, file) is not None:
                        found_path = os.path.join(root, file)

                        with open(found_path, encoding="utf8") as data_file:
                            file_json = json.load(data_file)
                        data_file.close()
                        script_input = self.traverse_file(file_json)
                        scripts.append(script_input)

            if scripts != []:
                repos_dict[dir] = scripts

        return repos_dict

    def repos_compare(self):
        repos_dict = self.repos_scripts()
        scripts = self.scripts_compare(repos_dict)

        return scripts


compare = Comparison()
# print(compare.cells_compare())
ipynb_dict = compare.get_cells_input()
print(compare.scripts_compare(ipynb_dict))
# print(compare.repos_scripts())
# print(compare.repos_compare())
