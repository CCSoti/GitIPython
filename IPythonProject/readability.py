import os

__author__ = 'SilviyaSoti'

from textstat.textstat import textstat


# class for getting text from files and analysing them for readability
class ReadabilityAnalysis():
    def __init__(self, repo_name):
        self.repo_name = repo_name
        pass

    def extract_text(self):
        repo_path = os.path.dirname(os.getcwd())  # os.path.dirname returns upper directory from current one
        print(repo_path)
        os.chdir(repo_path)
        find_file = repo_path + "\\" + self.repo_name
        os.chdir(find_file)
        print(find_file)

        found_path = ""
        for root, dirs, files in os.walk(find_file):
            for file in files:
                if file is "README.md" and os.path.join(root, file) is not None:
                    found_path = os.path.join(root, file)

            for dir in dirs:
                # print("Dir: ", dir)
                for root2, dirs2, files2 in os.walk(find_file + "\\" + dir):
                    for file2 in files2:
                        # print("File2 is:", file2)
                        if file2 == "README.md" and os.path.join(root, file2) is not None:
                            # print(os.path.join(root, file2))
                            found_path = os.path.join(root2, file2)
                            # else:
                            # print("No README.md file.")

        print(found_path)
        with open(found_path, 'r') as readme_file:
                for line in readme_file:
                    print(line, end='')


ra = ReadabilityAnalysis("tarmstrong")
print(ra.extract_text())

