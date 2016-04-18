"""
Python class for assessing changes in a GitHub repositories, by analysing merges.
"""

import os
from git import Repo


class MergeAnalysis():
    def __init__(self):
        pass

    def get_merges(self):
        """Method for getting repository merges and analysing their stages.
        Stage of the entry, either:

            * 0 = default stage
            * 1 = stage before a merge or common ancestor entry in case of a 3 way merge
            * 2 = stage of entries from the 'left' side of the merge
            * 3 = stage of entries from the right side of the merge

            0 == no conflict met
            not 0 == found conflict

        :return:
            Dictionary: {<repository_name>: <no_conflict_merges_percentage>}"""

        temp_path = os.path.dirname(os.path.realpath("IPythonProject"))
        path_project = temp_path + "\\NewGitHubProjects\\"
        merges = {}

        for dir in os.listdir(path_project):
            for d in os.listdir(path_project + "\\" + dir):
                repo = Repo(path_project + "\\" + dir + "\\" + d)
                master = repo.heads.master
                merged_blobs = repo.index.merge_tree(master)
                zeros = 0
                not_zeros = 0
                for merge in merged_blobs.entries:
                    if merge[1] == 0:
                        zeros += 1
                    else:
                        not_zeros += 1
                zeroes_percentage = zeros/len(merged_blobs.entries)
                not_zeros_percentage = not_zeros/len(merged_blobs.entries)

                merges.update({dir: [zeroes_percentage, not_zeros_percentage]})

        return merges

    def merge_analysis_for_all_repositories(self):
        """Method for calculating how many repositories had merges with no conflicts.
        :return:
            Float: percentage"""

        merges = self.get_merges()
        all_merges_without_conflicts = 0
        for merge in merges:
            if merge[1] == 0.0:
                all_merges_without_conflicts += 1

        return all_merges_without_conflicts/len(merges)

repo_files_types = MergeAnalysis()
print(repo_files_types.merge_analysis_for_all_repositories())
