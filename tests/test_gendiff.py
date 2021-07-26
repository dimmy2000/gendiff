import git
import os
import subprocess
import shlex

EXPECTED_JSON = """{
  - follow: false
    host: "hexlet.io"
  - proxy: "123.234.53.22"
  - timeout: 50
  + timeout: 20
  + verbose: true
}"""

EXPECTED_HELP = b"""usage: gendiff [-h] [-f FORMAT] first_file second_file

Generate diff

positional arguments:
  first_file
  second_file

optional arguments:
  -h, --help            show this help message and exit
  -f FORMAT, --format FORMAT
                        set format of output
"""


def test_set_arg_parser():
    output = subprocess.run(["poetry", "run", "gendiff", "-h"], capture_output=True)
    assert output.stdout == EXPECTED_HELP


def test_gendiff():
    git_repo = git.Repo(os.getcwd(), search_parent_directories=True)
    git_root = git_repo.git.rev_parse("--show-toplevel")

    file1 = os.path.join(git_root, "tests/fixtures/flat1.json")
    file2 = os.path.join(git_root, "tests/fixtures/flat2.json")

    input_request = shlex.split("poetry run gendiff {0} {1}".format(file1, file2))

    output = subprocess.run(input_request, capture_output=True)

    assert output.stdout.decode("utf-8") == EXPECTED_JSON
