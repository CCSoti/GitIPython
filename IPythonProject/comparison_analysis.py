import os
import distance as distance
from IPythonProject.license_analysis import LicenseAnalysis
from IPythonProject.comparison import Comparison


class ComparisonAnalysis:
    def __init__(self):  # , name):
        pass

    def scripts_equality(self):
        compare = Comparison()
        ipynb_dict = compare.get_cells_input()
        scripts = compare.scripts_compare(ipynb_dict)

        keys_scripts = scripts.keys()
        values_scripts = scripts.values()
        values_scripts = values_scripts

        for ratio in values_scripts:
            keys_tuples = ratio.keys()
            values_tuples = ratio.values()

            for tuple in keys_tuples:
                difference = ratio[tuple]
                comparison = difference[2]
                min_value = min(difference[0], difference[1])
                max_value = max(difference[0], difference[1])

                # if comparison == 0 or comparison == 1:
                #     if max_value != min_value and max_value - min_value <= max_value/2:
                #         print(tuple, difference)
                #     elif max_value == min_value and max_value != 1:
                #         print(tuple, difference)

                if comparison == 0:
                    print(tuple, difference)

        return


compAnalysis = ComparisonAnalysis()
compAnalysis.scripts_equality()
