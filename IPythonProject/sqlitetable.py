import json
import os
import sqlite3


class SqliteTable():
    def __init__(self):  # , name):
        pass

    def traverse_file(self, script):
        if "worksheets" in script:
            cells = script["worksheets"][0]["cells"]
        else:
            cells = script["cells"]

        script_cell_input = []
        for cell in cells:

            if cell["cell_type"] == "code":
                if "input" in cell.keys():
                    cell_input = cell["input"]
                else:
                    cell_input = cell["source"]
            else:
                cell_input = cell["source"]

                # cell_input_strip = []
                # for line in cell_input:
                #     line = line.split(" ")
                #     for word in line:
                #         cell_input_strip.append(word)

            script_cell_input.append(cell_input)

        return script_cell_input

    def repos_scripts(self):
        repo_path = os.path.dirname(os.getcwd())
        find_file = repo_path + "\IPythonProject\\NewGitHubProjects2"
        repos_dict = {}

        for dir in os.listdir(find_file):
            script_dict = {}
            for root, dirs, files in os.walk(find_file + "\\" + dir):
                for file in files:
                    if 'π' in file:
                        file = file.replace('π', str('π'.encode("utf-8")))

                    if ".ipynb" in file and os.path.join(root, file) is not None:
                        found_path = os.path.join(root, file)

                        with open(found_path, encoding="utf8") as data_file:
                            file_json = json.load(data_file)
                        data_file.close()
                        script_input = self.traverse_file(file_json)
                        script_dict[file] = script_input

            if script_dict != {}:
                repos_dict[dir] = script_dict

        return repos_dict

    def traverse_scripts(self):
        repos_dict = self.repos_scripts()
        table_rows = []

        for repo in repos_dict:
            repo_scripts = repos_dict[repo]
            for script in repo_scripts:
                script_cells = repo_scripts[script]
                for cell in range(0, len(script_cells)):
                    cell_number = cell
                    for line in range(0, len(script_cells[cell])):
                        line_number = line
                        line_content = script_cells[cell][line]
                        line_content = line_content.strip()

                        table_rows.append((repo, script, cell_number, line_number, line_content))

        return table_rows

    def create_table(self):
        conn = sqlite3.connect('ipython.db')
        c = conn.cursor()
        # Create table
        # c.execute('''CREATE TABLE ipython(repository TEXT, script TEXT, cell INT, line int, line_content text)''')
        # c.execute('''DROP TABLE ipython;''')

        # Insert a row of data
        table_rows = self.traverse_scripts()
        # for one_row in table_rows:
        #     c.execute("INSERT INTO ipython VALUES (?,?,?,?,?)", one_row)

        # Save (commit) the changes
        conn.commit()
        conn.close()


sqlitetable = SqliteTable()
sqlitetable.create_table()
