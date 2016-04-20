"""
Python class for accessing authors of commits and counting the different authors for a project.
:result: counting number of different authors of commits.
"""

import os
import json
from subprocess import *


class ExecutionAnalysis():
    def __init__(self):
        pass

    def check_ipynb(self, find_file):
        ipynb_files = []
        repositories_and_scripts_jsons = {}
        for root, dirs, files in os.walk(find_file):
            for dir in dirs:
                files_in_repo = []
                for root2, dirs2, files2 in os.walk(find_file + "\\" + dir):
                    for file2 in files2:
                        if 'π' in file2:
                            file2 = file2.replace('π', str('π'.encode("utf-8")))

                        if ".ipynb" in file2 and os.path.join(root2, file2) is not None:
                            found_path = os.path.join(root2, file2)
                            ipynb_files.append(found_path)
                            with open(found_path, encoding="utf8") as data_file:
                                file_json = json.load(data_file)
                            data_file.close()
                            files_in_repo.append(file_json)

                repositories_and_scripts_jsons.update({dir: files_in_repo})

        return ipynb_files, repositories_and_scripts_jsons

    def scripts_execution(self, ipynb_paths):
        """Method for checking if a IPython script can be executed from the subprocess model
        (first approach for getting errors from scripts)."""

        results = []
        for path in ipynb_paths:
            cmd = 'python ' + path
            result = getoutput(cmd)
            results.append(result)

            # another way of getting the error messages with the package subprocess
            # result = Popen(cmd, shell=True, stdout=PIPE)
            # out, err = result.communicate()
            # results.append([result.returncode, out, err])
        return results

    def outputs(self, ipynb_json):
        """Method for checking the outputs of cells - number of errors in a script(second approach).
        :return:
            List: [output_type];
            Float: percentage - number of scripts with errors against number of all scripts"""

        outputs = []
        number_of_scripts_with_errors = 0
        for script in ipynb_json:
            if "worksheets" in script and script["worksheets"] != []:
                cells = script["worksheets"][0]["cells"]
            elif "cells" in script.keys():
                cells = script["cells"]
            else:
                cells = []

            if cells != []:
                for cell in cells:
                    if "outputs" in cell:
                        cell_type = cell["outputs"]
                        if cell_type is not []:
                            for out in cell_type:
                                output_type = out["output_type"]
                                if output_type not in outputs:
                                    outputs.append(out["output_type"])
                                if output_type == "error" or output_type == "pyerr":
                                    number_of_scripts_with_errors += 1

        return outputs, number_of_scripts_with_errors

    def main(self):
        repo_path = os.path.dirname(os.getcwd())
        find_file = repo_path + "\IPythonProject\\NewGitHubProjects2"
        ipynb_paths, repositories_and_scripts_jsons = self.check_ipynb(find_file)

        repos_with_error = 0
        number_all_scripts = 0
        all_scripts_with_errors = 0
        for repo in repositories_and_scripts_jsons:
            ipynb_json = repositories_and_scripts_jsons[repo]
            outputs, number_of_scripts_with_errors = self.outputs(ipynb_json)
            if number_of_scripts_with_errors >= 1:
                repos_with_error += 1

            number_all_scripts += len(ipynb_json)
            all_scripts_with_errors += number_of_scripts_with_errors

        repos_with_errors_percentage = (repos_with_error/len(repositories_and_scripts_jsons))*100
        scripts_with_errors_percentage = (all_scripts_with_errors/number_all_scripts)*100

        return scripts_with_errors_percentage, repos_with_errors_percentage


execute = ExecutionAnalysis()
print(execute.main())
