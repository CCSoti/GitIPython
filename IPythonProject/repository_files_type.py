"""
Python class for accessing the files of a GitHub repository and extracting their types in order to understand if the
repository is a software developer poject.
:result: types of files in all repositories.
"""
import os
from git import Repo

# list taken from the languages.yml file in Python linguist package
languages = {"ABAP": [".abap"], "ANTLR": [".g4"], "ASP": [".asax", ".ascx", ".ashx", ".asmx", ".aspx", ".axd", ".asp"],
             "ActionScript": [".as"], "Ada": [".ads", ".adb"], "Agda": [".agda"], "ApacheConf": [".apacheconf"],
             "Apex": [".cls"], "AppleScript": [".applescript"], "Arc": [".arc"], "Arduino": [".ino"],
             "Assembly": [".asm"], "Augeas": [".aug"], "AutoHotkey": [".ahk"], "AutoIt": [".au3"],
             "Awk": [".awk", ".auk", ".gawk", ".mawk", ".nawk"],
             "Batchfile": [".bat", ".cmd"], "Befunge": [".befunge"], "BlitzBasic": [".bb", ".decls"],
             "BlitzMax": [".bmx"], "Bluespec": [".bsv"], "Boo": [".boo"], "Brainfuck": [".b", ".bf"], "Bro": [".bro"],
             "C": [".c", ".w"], "C#": [".cs", ".csx"], "C++": [".cpp", ".C", ".c++",".cxx",".H",".h++",".hh",".hpp",".hxx",".tcc",".tpp"],
             "C-ObjDump": [".c-objdump"], "C2hs Haskell": [".chs"], "CLIPS": [".clp"], "CMake": [".cmake", ".cmake.in"], "COBOL": [".cob", ".cbl", ".ccp", ".cobol", ".cpy"],
             "CSS": [".css"], "Ceylon": [".ceylon"], "ChucK": [".ck"], "Clean": [".icl", ".dcl"], "Clojure": [".clj", ".cl2", ".cljc", ".cljs", ".cljscm", ".cljx", ".hic"],
             "CoffeeScript": [".coffee", "._coffee", ".cson", ".iced"], "ColdFusion": [".cfm", ".cfc"], "Common Lisp": [".lisp", ".cl", ".lsp", ".asd", ".ny", ".podsl"],
             "Coq":[".coq"], "Cpp-ObjDump": [".cppobjdump", ".c++objdump", ".cxx-objdump"], "Cucumber": [".feature"], "Cuda": [".cu", ".cuh"], "Cython": [".pyx", ".pxd", ".pxi"],
             "D": [".d", ".di"], "D-ObjDump": [".d-objdump"], "DM": [".dm"], "DOT": [".dot", ".gv"], "Darcs Patch": [".darcspatch", ".dpatch"], "Dart": [".dart"],
             "DCPU-16 ASM": [".dasm16", ".dasm"], "Diff": [".diff"], "Dylan": [".dylan"], "Ecere Projects": [".epj"], "ECL": [".ecl", ".eclxml"],
             "Eiffel": [".e"], "Elixir": [".ex", ".exs"], "Elm": [".elm"], "Emacs Lisp": [".el", ".emacs"], "Erlang": [".erl", ".hrl"], "F#": [".fs", ".fsi", "fsx"],
             "FORTRAN":[".f90", ".F", ".F03", ".F08", ".F77", ".F90", ".F95", ".FOR", ".FPP", ".f", ".f03", ".f08", ".fpp", ".for", ".f95", ".f77"],
             "Factor": [".factor"], "Fancy": [".fy", ".fancypack"], "Fantom": [".fan"], "Forth": [".4th"], "GAS": [".s", ".S"],
             "GLSL": [".glsl", ".fp", ".frag", ".geom", ".glslv", ".shader", ".vert"], "Genshi": [".kid"], "Gentoo Ebuild": [".ebuild"],
             "Gentoo Eclass": [".eclass"], "Gettext Catalog": [".po", ".pot"], "Glyph": [".glf"], "Go": [".go"], "Gosu": [".gs"],
             "Groff": [".man"], "Groovy": [".groovy"], "Groovy Server Pages": [".gsp"], "HTML": [".html", "xhtml"], "HTML+Django": [".mustache", ".jinja"],
             "HTML+ERB": [".erb"], "HTML+PHP": [".phtml"], "HTTP": [".http"], "Haml": [".haml"], "Handlebars": [".handlebars"], "Haskell": [".hs"], "Haxe": [".hx"],
             "INI": [".ini"], "Idris": [".idr", ".lidr"], "Inno Setup": [".iss"], "IRC log": [".irclog"], "Io": [".io"], "Ioke": [".ik"],
             "J": [".ijs"], "JSON": [".json"], "Jade": [".jade"], "Java": [".java"], "Java Server Pages": [".js"], "Julia": [".jl"], "KRL": [".krl"],
             "Kotlin": [".kt"], "LFE": [".lfe"], "LLVM": [".ll"], "Lasso": [".lasso"], "Less": [".less"], "LilyPond": [".ly"], "Literate Agda": [".lagda"],
             "Literate CoffeeScript": [".litcoffee"], "Literate Haskell": [".lhs"], "LiveScript": [".ls"], "Logos": [".xm"], "Logtalk": [".lgt"],
             "Lua": [".lua"], "M": [".mumps"], "Makefile": [".mak"], "Mako": [".mako"], "Markdown": [".md"], "Matlab": [".matlab"], "Max": [".mxt"],
             "MiniD": [".minid"], "Mirah": [".druby"], "Monkey": [".monkey"], "Moocode": [".moo"], "MoonScript": [".moon"], "Myghty": [".myt"],
             "NSIS": [".nsi"], "Nemerle": [".n"], "NetLogo": [".nlogo"], "Nginx": [".nginxconf"], "Nimrod": [".nim", ".nimrod"],
             "Nu": [".nu"], "NumPy": [".numpy"], "OCaml": [".ml"], "ObjDump": [".objdump"], "Objective-C": [".m"], "Objective-J": [",j"], "Omgrofl": [".omgrofl"],
             "Opa": [".opa"], "OpenCL": [".cl"], "OpenEdge ABL": [".p"], "Oxygene": [".oxygene"], "PHP": [".php",".php3",".php4",".php5",".phpt"], "Parrot": [".parrot"],
             "Parrot Internal Representation": [".pir"], "Parrot Assembly": [".pasm"], "Pascal": [".pl", ".perl", ".PL", ".pod", "nqp", "ph","plx"],
             "Pike": [".pike"], "PogoScript": [".pogo"], "PowerShell": [".ps1"], "Processing": [".pde"], "Prolog": [".prolog"], "Protocol Buffer": [".proto"],
             "Puppet": [".pp"], "Pure Data": [".pd"], "Python": [".py"], "Python traceback": [".pytb"], "QML": [".qml"], "R": [".r"],
             "REALbasic": [".rbbas"], "RHTML": [".rhtml"], "Racket": [".rkt"], "Ragel in Ruby Host": [".rl"], "Raw token data": [".rebol"],
             "Redcode": [".cw"], "RobotFramework": [".robot"], "Rouge": [".rg"], "Ruby": [".rb"], "Rust": [".rs"], "SCSS": [".scss"], "SQL": [".sql"],
             "Sage": [".sage"], "Sass": [".sass"], "Scala": [".scala"], "Scaml": [".scaml"], "Scheme": [".scm"], "Scilab": [".sci"], "Self": [".self"],
             "Shell": [".sh"], "Slash": [".sl"], "Smalltalk": [".st"], "Smarty": [".tpl"], "Squirrel": [".nut"], "Standard ML": [".sml"],
             "SuperCollider": [".sc"], "TOML": [".toml"], "TXL": [".txl"], "Tcl": [".tcl"], "Tcsh": [".tcsh"], "TeX": [".tex"], "Tea": [".tea"], "Textile": [".textile"],
             "Turing": [".t"], "Twig": [".twig"], "TypeScript": [".ts"], "Unified Parallel C": [".upc"], "UnrealScript": [".uc"], "VHDL": [".vhdl"],
             "Vala": [".vala"], "Verilog": [".v"], "VimL": [".vim"], "Visual Basic": [".vb"], "Volt": [".volt"], "XC": [".xc"],
             "XML": [".xml"], "XProc": [".xpl"], "XQuery": [".xquery"], "XS": [".xs"], "XSLT": [".xslt"], "Xtend": [".xtend"], "YAML": [".yml"],
             "eC": [".ec"], "edn": [".edn"], "fish": [".fish"], "mupad": [".mu"], "nesC": [".nc"], "ooc": [".ooc"], "reStructuredText": [".rst"],
             "wisp": [".wisp"], "xBase": [".prg"], "IPython": [".ipynb"]}


class RepositoryFilesTypes():
    def __init__(self):
        pass

    def check_language(self, blobs, different_files_types):
        """Method for configuring the language used in a file.
        :return:
            List: [file_type, file_type, file_type, ...]"""

        languages_values = list(languages.values())

        # blobs are files
        for blob in blobs:
            # print(blob.name, blob.mime_type)
            blob_name = blob.name
            blob_mime_type = blob.mime_type
            for language in languages_values:
                for value in language:
                    language_key = ""
                    for item in languages.items():
                        if value in item[1]:
                            language_key = item[0]

                    if value in blob_name:
                        blob_split = blob_name.split(".")
                        if language_key not in different_files_types and value == "." + blob_split[1]:
                            different_files_types.append(language_key)
                    else:
                        if blob_mime_type not in different_files_types:
                            different_files_types.append(blob_mime_type)

        return different_files_types

    def get_different_types_of_files(self):
        """Method for getting types of files for each repository.
        :return:
            Dictionary: {<repository_name>: <repository_different_files_types>}"""

        temp_path = os.path.dirname(os.path.realpath("IPythonProject"))
        path_project = temp_path + "\\NewGitHubProjects\\"
        files_types = {}

        for dir in os.listdir(path_project):
            different_files_types = []
            for d in os.listdir(path_project + "\\" + dir):
                repo = Repo(path_project + "\\" + dir + "\\" + d, search_parent_directories=True)
                tree = repo.heads.master.commit.tree
                blobs = tree.blobs
                different_files_types = self.check_language(blobs, different_files_types)

            files_types.update({dir: different_files_types})

        return files_types

    def calculate_non_software_developer_projects(self):
        """Method for calculating the percentage of the repositories that are only with text/plain files
        :return:
            Float: <number>"""

        non_software_dev_projects = []
        repositories_files_types = self.get_different_types_of_files()
        for repository in repositories_files_types:
            repository_files = repositories_files_types[repository]
            if repository_files == ['text/plain']:
                non_software_dev_projects.append(repository)

        if len(non_software_dev_projects) != 0:
            percentage = len(non_software_dev_projects)/len(repositories_files_types)
        else:
            percentage = len(non_software_dev_projects)

        return percentage

repo_files_types = RepositoryFilesTypes()
print(repo_files_types.calculate_non_software_developer_projects())
