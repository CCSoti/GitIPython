from IPythonProject.wrapper import RepositoryWrapper


def try_licenses():
    repo = RepositoryWrapper("vim-ipython", "https://github.com/ivanov/vim-ipython.git")
    return repo.clone_repos()


try_licenses()
