import os
from unittest import TestCase
from IPythonProject.readability import ReadabilityAnalysis

__author__ = 'SilviyaSoti'


class TestReadabilityAnalysis(TestCase):
    def test_extract_text(self):
        self.fail()

    def test_syllable_number(self):
        readability_object = ReadabilityAnalysis("tarmstrong")
        self.assertEqual(160, readability_object.syllable_number())

    def test_lexicon_number(self):
        self.fail()

    def test_sentence_number(self):
        self.fail()

    def test_flesch_reading_ease_score(self):
        self.fail()

    def test_flesch_kincaid_grade_level(self):
        self.fail()

    def test_fog_scale(self):
        self.fail()

    def test_smog_analysis(self):
        self.fail()

    def test_automated_index(self):
        self.fail()

    def test_coleman_index(self):
        self.fail()

    def test_linsear_write(self):
        self.fail()

    def test_dale_chall_score(self):
        self.fail()

    def test_consensus_analysis(self):
        self.fail()