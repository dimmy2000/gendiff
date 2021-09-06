import os
import subprocess
import shlex

root_path = os.getcwd()
fixtures_path = os.path.join(root_path, "tests/fixtures/")


flat_fixtures = (
    ("flat1.json", "flat2.json"),
    ("flat1.yaml", "flat2.yaml"),
    ("flat1.json", "flat2.yaml"),
    ("flat1.yaml", "flat2.json"),
)

recursive_fixtures = (
    ("recursive1.json", "recursive2.json"),
    ("recursive1.yaml", "recursive2.yaml"),
    ("recursive1.yaml", "recursive2.json"),
    ("recursive1.json", "recursive2.yaml"),
)

with open(os.path.join(fixtures_path, "expected.txt")) as f:
    EXPECTED_FLAT = f.read()

with open(os.path.join(fixtures_path, "expected_recursive.txt")) as f:
    EXPECTED_RECURSIVE = f.read()

with open(os.path.join(fixtures_path, "expected_help.txt"), "rb") as f:
    EXPECTED_HELP = f.read()


def test_set_arg_parser():
    output = subprocess.run(["poetry", "run", "gendiff", "-h"], capture_output=True)
    assert output.stdout == EXPECTED_HELP


def test_flat_files():
    for file in flat_fixtures:
        file1 = os.path.join(fixtures_path, file[0])
        file2 = os.path.join(fixtures_path, file[1])

        input_request = shlex.split("poetry run gendiff {0} {1}".format(file1, file2))
        output = subprocess.run(input_request, capture_output=True)

        assert output.stdout.decode("utf-8") == EXPECTED_FLAT


def test_recursive_files():
    for file in recursive_fixtures:
        file1 = os.path.join(fixtures_path, file[0])
        file2 = os.path.join(fixtures_path, file[1])

        input_request = shlex.split("poetry run gendiff {0} {1}".format(file1, file2))
        output = subprocess.run(input_request, capture_output=True)

        assert output.stdout.decode("utf-8") == EXPECTED_RECURSIVE
