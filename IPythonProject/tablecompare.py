import copy
import sqlite3

import distance


class TableCompare():
    def __init__(self):  # , name):
        pass

    def get_cellcontent(self):
        conn = sqlite3.connect('ipython.db')
        c = conn.cursor()
        lines = c.execute('SELECT script, cell, line_content FROM ipython ')
        lines = list(lines)
        lines_copy = copy.copy(lines)
        cell_differences = []
        for line in lines:
            for line_copy in lines_copy:
                if line[0]==line_copy[0] and line[1]!=line_copy[1]:
                    difference = distance.levenshtein(line[2], line_copy[2])
                    cell_differences.append((len(line[2]), len(line_copy[2]), difference))

        return cell_differences


tablecompare = TableCompare()
print(tablecompare.get_cellcontent())
