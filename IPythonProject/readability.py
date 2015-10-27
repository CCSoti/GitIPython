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
        os.chdir(repo_path)
        find_file = repo_path + "\\" + self.repo_name
        os.chdir(find_file)

        found_path = ""
        for root, dirs, files in os.walk(find_file):
            for file in files:
                if file is "README.md" and os.path.join(root, file) is not None:
                    found_path = os.path.join(root, file)

            for dir in dirs:
                for root2, dirs2, files2 in os.walk(find_file + "\\" + dir):
                    for file2 in files2:
                        if file2 == "README.md" and os.path.join(root, file2) is not None:
                            found_path = os.path.join(root2, file2)

        readme_text = []
        try:
            with open(found_path, 'r') as readme_file:
                for line in readme_file:
                    readme_text.append(line)
        except FileNotFoundError:
            print("Repository doesn't contain README.md file.")

        return readme_text


ra = ReadabilityAnalysis("pydata")
print(ra.extract_text())
