import sqlite3

import time


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
        pass

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
            if line[0] == "plot_wiggle(trc,figsize=[10,10],perc=99)":
                print("Fine.")
        # print(list(query_result))
        return list_query_result

    def extract_cells_from_script(self, conn, repository, script):
        c = conn.cursor()

        query_template = 'SELECT cell FROM ipython WHERE repository=? AND script=? ORDER BY line ASC'

        cells_result = c.execute(query_template, (repository[0], script[0]))
        result = {}
        for cell in cells_result:
            result[cell] = self.extract_cell(conn, repository, script, cell)

        return result

    def extract_cells_from_repository(self, conn, repository):
        c = conn.cursor()

        query_template = \
            'SELECT script FROM ipython WHERE repository="%s" ORDER BY script ASC'

        script_result = c.execute(query_template % repository)
        result = {}
        for script in script_result:
            if script in result:
                result[script].update(self.extract_cells_from_script(conn, repository, script))
            else:
                result[script] = self.extract_cells_from_script(conn, repository, script)

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
                result[repository].update(self.extract_cells_from_repository(conn, repository))
            else:
                result[repository] = self.extract_cells_from_repository(conn, repository)
            count += 1
            print(count, "Done", repository)
        return result

    def compare_cells_within__each_script(self, conn):
        repositories = self.extract_cells(conn)

        result = {}

        for repository in repositories:
            for script in repository:
                for cell1 in script:
                    for cell2 in script:
                        difference = self.cell_difference(cell1, cell2)
                        print(difference)

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
        print(self.extract_cells(conn))
        end_time = time.time()
        print("Time: ", end_time - start_time)


dependencies = Dependencies()
dependencies.main()
