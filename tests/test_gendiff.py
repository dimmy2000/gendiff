import git
import os
import subprocess
import shlex

git_repo = git.Repo(os.getcwd(), search_parent_directories=True)
repo_root = git_repo.git.rev_parse("--show-toplevel")
fixtures_path = os.path.join(repo_root, "tests/fixtures/")

test_files = [
    ["flat1.json", "flat2.json"],
    ["flat1.yaml", "flat2.yaml"],
]

with open(os.path.join(fixtures_path, "expected.txt")) as f:
    EXPECTED = f.read()

with open(os.path.join(fixtures_path, "expected_help.txt"), "rb") as f:
    EXPECTED_HELP = f.read()


def test_set_arg_parser():
    output = subprocess.run(["poetry", "run", "gendiff", "-h"], capture_output=True)
    assert output.stdout == EXPECTED_HELP


def test_gendiff():
    for file in test_files:
        file1 = os.path.join(fixtures_path, file[0])
        file2 = os.path.join(fixtures_path, file[1])

        input_request = shlex.split("poetry run gendiff {0} {1}".format(file1, file2))
        output = subprocess.run(input_request, capture_output=True)
        assert output.stdout.decode("utf-8") + "\n" == EXPECTED
