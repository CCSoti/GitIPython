import os

__author__ = 'SilviyaSoti'

from textstat.textstat import textstat

LICENSES = ["README.md", "README.txt", "README.org", "LICENSE", "README.rst"]

# class for getting text from files and analysing them for readability
class ReadabilityAnalysis():
    def __init__(self, repo_name):
        self.repo_name = repo_name
        pass

    # extract the text from README.md file if the repository has it
    def extract_text(self):
        repo_path = os.path.dirname(os.getcwd())  # os.path.dirname returns upper directory from current one
        if "IPythonProject" in repo_path:
            repo_path = repo_path.replace("IPythonProject", "")
        os.chdir(repo_path)
        print(repo_path)
        find_file = repo_path + "\IPythonProject\\NewGitHubProjects\\" + self.repo_name
        os.chdir(find_file)

        # a path for the LAST found readme or license file
        found_path = ""
        readme_paths = []
        for root, dirs, files in os.walk(find_file):
            for file in files:
                if file in LICENSES and os.path.join(root, file) is not None:
                    found_path = os.path.join(root, file)
                    readme_paths.append(found_path)

            for dir in dirs:
                for root2, dirs2, files2 in os.walk(find_file + "\\" + dir):
                    for file2 in files2:
                        if file2 in LICENSES and os.path.join(root, file2) is not None:
                            found_path = os.path.join(root2, file2)
                            readme_paths.append(found_path)

        # list of lists, where the list elements are texts from the founded files
        all_found_files = []
        try:
            for path in readme_paths:
                readme_text = []
                with open(path, 'r') as readme_file:
                    for line in readme_file:
                        readme_text.append(line)
                all_found_files.append(readme_text)
        except FileNotFoundError:
            print("Repository doesn't contain README.md file.")

        return all_found_files, readme_paths

    def syllable_number(self):
        readme_text = self.extract_text()
        overall_num = 0
        for read in readme_text:
            overall_num = overall_num + textstat.syllable_count(read)
        return overall_num

    def lexicon_number(self):
        readme_text = self.extract_text()
        overall_num = 0
        for read in readme_text:
            overall_num = overall_num + textstat.lexicon_count(read)
        return overall_num

    def sentence_number(self):
        readme_text = self.extract_text()
        overall_num = 0
        for read in readme_text:
            overall_num = overall_num + textstat.sentence_count(read)
        return overall_num

    """
    Returns the Flesch Reading Ease Score.
    Following table is helpful to access the ease of readability in a document:

    90-100 : Very Easy
    80-89 : Easy
    70-79 : Fairly Easy
    60-69 : Standard
    50-59 : Fairly Difficult
    30-49 : Difficult
    0-29 : Very Confusing
    """

    def flesch_reading_ease_score(self):
        readme_text = self.extract_text()
        overall_read = ""
        for read in readme_text:
            overall_read += read
        return textstat.flesch_reading_ease(overall_read)

    """
    Returns the grade score using the Flesch-Kincaid Grade Formula.
    For example a score of 9.3 means that a ninth grader would be able to read the document.
    """

    def flesch_kincaid_grade_level(self):
        readme_text = self.extract_text()
        overall_read = ""
        for read in readme_text:
            overall_read += read
        return textstat.flesch_kincaid_grade(overall_read)

    """
    Returns the FOG index of the given text.
    """

    def fog_scale(self):
        readme_text = self.extract_text()
        overall_read = ""
        for read in readme_text:
            overall_read += read
        return textstat.gunning_fog(overall_read)

    """
    Return the SMOG index of the given text.
    """

    def smog_analysis(self):
        readme_text = self.extract_text()
        overall_read = ""
        for read in readme_text:
            overall_read += read
        return textstat.smog_index(overall_read)

    """
    Returns the ARI(Automated Readability Index) which outputs a number that approximates the grade level needed to comprehend the text.
    For example if the ARI is 6.5, then the grade level to comprehend the text is 6th to 7th grade.
    """

    def automated_index(self):
        readme_text = self.extract_text()
        overall_read = ""
        for read in readme_text:
            overall_read += read
        return textstat.automated_readability_index(overall_read)

    """
    Returns the grade level of the text using the Coleman-Liau Formula
    """

    def coleman_index(self):
        readme_text = self.extract_text()
        overall_read = ""
        for read in readme_text:
            overall_read += read
        return textstat.coleman_liau_index(overall_read)

    """
    Returns the grade level using the Lisear Write Formula.
    """

    def linsear_write(self):
        readme_text = self.extract_text()
        overall_read = ""
        for read in readme_text:
            overall_read += read
        return textstat.linsear_write_formula(overall_read)

    """
    Different from other tests, since it uses a lookup table of most commonly used 3000 english words.
    Thus it returns the grade level using the New Dale-Chall Formula.
    """

    def dale_chall_score(self):
        readme_text = self.extract_text()
        overall_read = ""
        for read in readme_text:
            overall_read += read
        return textstat.dale_chall_readability_score(overall_read)

    """
    Based upon all the above analysis returns the most appropriate grade level under which the given text belongs to.
    """

    def consensus_analysis(self):
        readme_text = self.extract_text()
        overall_read = ""
        for read in readme_text:
            overall_read += read
        return textstat.readability_consensus(overall_read)


# ra = ReadabilityAnalysis("tarmstrong")
# print(ra.extract_text())
# print(ra.syllable_number())
# print(ra.lexicon_number())
# print(ra.sentence_number())
# print(ra.flesch_reading_ease_score())
# print(ra.flesch_kincaid_grade_level())
# print(ra.fog_scale())
# print(ra.smog_analysis())
# print(ra.automated_index())
# print(ra.coleman_index())
# print(ra.linsear_write())
# print(ra.dale_chall_score())
# print(ra.consensus_analysis())

