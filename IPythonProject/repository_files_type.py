"""
Python class for accessing the files of a GitHub repository and extracting their types in order to understand if the
repository is a software developer poject.
:result: types of files in all repositories.
"""
import os
from git import Repo

class RepositoryFilesTypes():
    def __init__(self):
        pass

    def get_different_types_of_files(self):
        """Method for getting types of files for each repository.
        :return:
            Dictionary: {<repository_name>: <repository_different_files_types>}"""

        temp_path = os.path.dirname(os.path.realpath("IPythonProject"))
        path_project = temp_path + "\\NewGitHubProjects2\\"
        files_types = {}

        for dir in os.listdir(path_project):
            different_files_types = []
            for d in os.listdir(path_project + "\\" + dir):
                repo = Repo(path_project + "\\" + dir + "\\" + d, search_parent_directories=True)
                tree = repo.heads.master.commit.tree

                # blobs are files
                for blob in tree.blobs:
                    # print(blob.name, blob.mime_type)
                    blob_name = blob.name
                    blob_mime_type = blob.mime_type
                    if ".ipynb" in blob_name and "IPython" not in different_files_types:
                        different_files_types.append("IPython")
                    elif ".py" in blob_name and "Python" not in different_files_types:
                        different_files_types.append("Python")
                    elif ".java" in blob_name and "Java" not in different_files_types:
                        different_files_types.append("Java")
                    elif ".js" in blob_name and "JavaScript" not in different_files_types:
                        different_files_types.append("JavaScript")
                    elif ".css" in blob_name and "CSS" not in different_files_types:
                        different_files_types.append("CSS")
                    else:
                        if blob_mime_type not in different_files_types:
                            different_files_types.append(blob_mime_type)

            files_types.update({dir: different_files_types})

        return files_types


repo_files_types = RepositoryFilesTypes()
print(repo_files_types.get_different_types_of_files())
