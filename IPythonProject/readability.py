import os

__author__ = 'SilviyaSoti'

from textstat.textstat import textstat


# class for getting text from files and analysing them for readability
class ReadabilityAnalysis():
    def __init__(self, repo_name):
        self.repo_name = repo_name
        pass

    # extract the text from README.md file if the repository has it
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

    def syllable_number(self):
        readme_text = self.extract_text()
        for read in readme_text:
            print(read, "   ", textstat.syllable_count(read))
        return

    def lexicon_number(self):
        return

    def sentence_number(self):
        return

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
        return

    """
    Returns the grade score using the Flesch-Kincaid Grade Formula.
    For example a score of 9.3 means that a ninth grader would be able to read the document.
    """
    def flesch_kincaid_grade_level(self):
        return

    """
    Returns the FOG index of the given text.
    """
    def fog_scale(self):
        return

    """
    Return the SMOG index of the given text.
    """
    def smog_analysis(self):
        return

    """
    Returns the ARI(Automated Readability Index) which outputs a number that approximates the grade level needed to comprehend the text.
    For example if the ARI is 6.5, then the grade level to comprehend the text is 6th to 7th grade.
    """
    def automated_index(self):
        return

    """
    Returns the grade level of the text using the Coleman-Liau Formula
    """
    def coleman_index(self):
        return

    """
    Returns the grade level using the Lisear Write Formula.
    """
    def linsear_write(self):
        return

    """
    Different from other tests, since it uses a lookup table of most commonly used 3000 english words.
    Thus it returns the grade level using the New Dale-Chall Formula.
    """
    def dale_chall_score(self):
        return

    """
    Based upon all the above analysis returns the most appropriate grade level under which the given text belongs to.
    """
    def consensus_analysis(self):
        return

ra = ReadabilityAnalysis("tarmstrong")
# print(ra.extract_text())
ra.syllable_number()