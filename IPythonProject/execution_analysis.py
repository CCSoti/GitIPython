import os
from subprocess import *
from IPythonProject.license_analysis import LicenseAnalysis


class ExecutionAnalysis():
    def __init__(self):
        pass

    # checking if a IPython script can be executed from the subprocess model(one approach)
    def scripts_execution(self, ipynb_paths):
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

    # checking the outputs - number of errors in a script(second approach)
    def outputs(self, ipynb_json):
        outputs = []
        for script in ipynb_json:
            if "worksheets" in script:
                cells = script["worksheets"][0]["cells"]
            else:
                cells = script["cells"]

            for cell in cells:
                if "outputs" in cell:
                    cell_type = cell["outputs"]
                    if cell_type is not []:
                        for out in cell_type:
                            outputs.append(out["output_type"])

        return outputs


repo = LicenseAnalysis()
execute = ExecutionAnalysis()
repo_path = os.path.dirname(os.getcwd())
find_file = repo_path + "\IPythonProject\\NewGitHubProjects2"
ipynb_paths, ipynb_json = repo.check_ipynb(find_file)
print(execute.scripts_execution(ipynb_paths))
# print(execute.outputs(ipynb_json))
