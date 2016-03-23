import os

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

                script_cell_input.append(cell_input)

            ipynb_dict[ipynb_files[item]] = script_cell_input
            item += 1

        return ipynb_dict


compare = Comparison()
print(compare.get_cells_input())
