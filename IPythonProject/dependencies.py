import sqlite3
import time

import distance


class Dependencies():
    def __init__(self):  # , name):
        pass

    ##--Tim suggestions
    def cell_difference(self, cell1, cell2):
        """
        return a single value indicating the extent to which cell 1 is like cell 2.
        :param cell1: a list of lines of code
        :param cell2: a list of lines of code
        :return:
        """
        sum = 0
        count_differences = 0
        for c1 in cell1:
            for c2 in cell2:
                difference = distance.nlevenshtein(c1, c2)
                sum += difference
                count_differences += 1

        average = sum/count_differences
        return average

    def extract_cell(self, conn, repository, script, cell):
        """
        :param conn:
        :return: a list of cell code strings
        """
        c = conn.cursor()
        # print(type(repository), type(script), type(cell))

        query_template = 'SELECT line_content FROM ipython WHERE repository =? AND script =? AND cell=? ORDER BY line ASC'

        query_result = c.execute(query_template, (repository[0], script[0], cell[0]))
        list_query_result = []
        for line in query_result:
            list_query_result.append(line[0])
        return list_query_result

    def extract_cells_from_script(self, conn, repository, script):
        c = conn.cursor()

        query_template = 'SELECT cell FROM ipython WHERE repository=? AND script=? ORDER BY line ASC'

        cells_result = c.execute(query_template, (repository[0], script[0]))
        result = {}
        for cell in cells_result:
            if cell in result:
                result[cell[0]].append(self.extract_cell(conn, repository, script, cell))
            else:
                result[cell[0]] = self.extract_cell(conn, repository, script, cell)

        return result

    def extract_cells_from_repository(self, conn, repository):
        c = conn.cursor()

        query_template = \
            'SELECT script FROM ipython WHERE repository="%s" ORDER BY script ASC'

        script_result = c.execute(query_template % repository)
        result = {}
        for script in script_result:
            if script in result:
                result[script[0]].update(self.extract_cells_from_script(conn, repository, script))
            else:
                result[script[0]] = self.extract_cells_from_script(conn, repository, script)

        return result

    def extract_cells(self, conn):
        c = conn.cursor()

        query_template = \
            'SELECT repository FROM ipython ORDER BY script ASC'

        repository_result = c.execute(query_template)
        result = {}
        count = 0
        for repository in repository_result:
            if repository in result:
                result[repository[0]].update(self.extract_cells_from_repository(conn, repository))
            else:
                result[repository[0]] = self.extract_cells_from_repository(conn, repository)
            count += 1
            print(count, "Done", repository)
        return result

    def compare_cells_within__each_script(self, conn):
        conn2 = sqlite3.connect('compare_cells.db')
        c2 = conn2.cursor()
        # Create table
        c2.execute('''CREATE TABLE compare_cells(repository TEXT, script TEXT, cell1 INT, cell2 int, similarity real)''')

        repositories = self.extract_cells(conn)

        # result = {}

        for repository in repositories:
            repo_values = repositories[repository]
            # script_dict = {}
            for script in repo_values:
                # script_list = []
                script_values = repo_values[script]
                for cell1 in script_values:
                    for cell2 in script_values:
                        difference = self.cell_difference(script_values[cell1], script_values[cell2])
                        print((repository, script, cell1, cell2, difference))
                        c2.execute("INSERT INTO compare_cells VALUES (?,?,?,?,?)", (repository, script, cell1, cell2, difference))

        conn2.commit()
        conn2.close()


    def compare_all_cells_in_all_repositories(self, conn):
        repositories = self.extract_cells(conn)

        for repository1 in repositories:
            for script1 in repository1:
                for cell1 in script1:
                    for repository2 in repositories:
                        for script2 in repository2:
                            for cell2 in script2:
                                difference = self.cell_difference(cell1, cell2)

    def main(self):
        conn = sqlite3.connect('ipython.db')
        start_time = time.time()
        # print(self.extract_cells(conn))
        print(self.compare_cells_within__each_script(conn))
        end_time = time.time()
        print("Time: ", end_time - start_time)


dependencies = Dependencies()
dependencies.main()
