import os
from unittest import TestCase
from IPythonProject.readability import ReadabilityAnalysis

__author__ = 'SilviyaSoti'


class TestReadabilityAnalysis(TestCase):
    # def test_extract_text(self):
    #     self.fail()

    def test_syllable_number(self):
        readability_object = ReadabilityAnalysis("tarmstrong")
        self.assertEqual(160, readability_object.syllable_number())

    def test_lexicon_number(self):
        readability_object = ReadabilityAnalysis("tarmstrong")
        self.assertEqual(94, readability_object.lexicon_number())

    def test_sentence_number(self):
        readability_object = ReadabilityAnalysis("tarmstrong")
        self.assertEqual(13, readability_object.sentence_number())

    def test_flesch_reading_ease_score(self):
        readability_object = ReadabilityAnalysis("tarmstrong")
        self.assertEqual(61.93, readability_object.flesch_reading_ease_score())

    def test_flesch_kincaid_grade_level(self):
        readability_object = ReadabilityAnalysis("tarmstrong")
        self.assertEqual(7.0, readability_object.flesch_kincaid_grade_level())

    def test_fog_scale(self):
        readability_object = ReadabilityAnalysis("tarmstrong")
        self.assertEqual(18.100425531914894, readability_object.fog_scale())

    def test_smog_analysis(self):
        readability_object = ReadabilityAnalysis("tarmstrong")
        self.assertEqual(10.4, readability_object.smog_analysis())

    def test_automated_index(self):
        readability_object = ReadabilityAnalysis("tarmstrong")
        self.assertEqual(13.3, readability_object.automated_index())

    def test_coleman_index(self):
        readability_object = ReadabilityAnalysis("tarmstrong")
        self.assertEqual(17.95, readability_object.coleman_index())

    def test_linsear_write(self):
        readability_object = ReadabilityAnalysis("tarmstrong")
        self.assertEqual(4.25, readability_object.linsear_write())

    def test_dale_chall_score(self):
        readability_object = ReadabilityAnalysis("tarmstrong")
        self.assertEqual(8.97, readability_object.dale_chall_score())

    def test_consensus_analysis(self):
        readability_object = ReadabilityAnalysis("tarmstrong")
        self.assertEqual("8th and 9th grade", readability_object.consensus_analysis())