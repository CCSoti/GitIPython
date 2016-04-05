import copy
import sqlite3

import distance


class TableCompare():
    def __init__(self):  # , name):
        pass

    def cell_analysis(self, original, copy_var, difference):
        same = False
        if difference == 0 and original != 0 and copy_var != 0 and original == copy_var:
            same = True
        return same

    def get_celldifference(self):
        conn = sqlite3.connect('ipython.db')
        c = conn.cursor()
        lines = c.execute('SELECT script, cell, line_content FROM ipython ')
        lines = list(lines)
        lines_copy = copy.copy(lines)
        cell_differences = {}
        for l in range(0, len(lines)):
            line = lines[l]
            line_diff = []
            for c in range(l+1, len(lines_copy)):
                line_copy = lines_copy[c]
                if line[0] == line_copy[0] and l != c and line[1] != line_copy[1]:
                    difference = distance.levenshtein(line[2], line_copy[2])
                    same = self.cell_analysis(len(line[2]), len(line_copy[2]), difference)
                    line_diff.append(same)

            repo_cell = str(line[0]) + ": " + str(line[1])
            if repo_cell in cell_differences:
                cell_differences[repo_cell].extend(line_diff)
            else:
                cell_differences[repo_cell] = line_diff

        return cell_differences

    def cell_equality(self):
        cell_differences = self.get_celldifference()
        cell_equality = {}
        for cell_diff in cell_differences:
            cell_keys = cell_differences[cell_diff]
            count_equality = 0
            number_lines = len(cell_keys)
            for equality in cell_keys:
                if equality == True:
                    count_equality += 1

            cell_equality[cell_diff] = [number_lines, count_equality]

        return cell_equality

    def get_scriptdifference(self):
        conn = sqlite3.connect('ipython.db')
        c = conn.cursor()
        lines = c.execute('SELECT repository, script, line_content FROM ipython ')
        lines = list(lines)
        lines_copy = copy.copy(lines)
        script_differences = []
        for l in range(0, len(lines)):
            line = lines[l]
            for c in range(l+1, len(lines_copy)):
                line_copy = lines_copy[c]
                if line[0] == line_copy[0] and l != c and line[1] != line_copy[1]:
                    difference = distance.levenshtein(line[2], line_copy[2])
                    script_differences.append((len(line[2]), len(line_copy[2]), difference))

        return script_differences

    def get_repodifference(self):
        conn = sqlite3.connect('ipython.db')
        c = conn.cursor()
        lines = c.execute('SELECT repository, script, line_content FROM ipython ')
        lines = list(lines)
        lines_copy = copy.copy(lines)
        repo_differences = []
        for l in range(0, len(lines)):
            line = lines[l]
            for c in range(l+1, len(lines_copy)):
                line_copy = lines_copy[c]
                if line[0] != line_copy[0] and l != c and line[1] != line_copy[1]:
                    difference = distance.levenshtein(line[2], line_copy[2])
                    repo_differences.append((len(line[2]), len(line_copy[2]), difference))

        return repo_differences


tablecompare = TableCompare()
print(tablecompare.cell_equality())
