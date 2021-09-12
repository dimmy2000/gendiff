import json
import os
import subprocess
import shlex

root_path = os.getcwd()
fixtures_path = os.path.join(root_path, "tests/fixtures/")

fixtures = (
    ("file1.json", "file2.json"),
    ("file1.yaml", "file2.yaml"),
    ("file1.json", "file2.yaml"),
    ("file1.yaml", "file2.json"),
)

flat_fixtures = os.path.join(fixtures_path, "flat")
recursive_fixtures = os.path.join(fixtures_path, "recursive")

with open(os.path.join(fixtures_path, "expected.txt")) as f:
    EXPECTED_FLAT = f.read()

with open(os.path.join(fixtures_path, "expected_recursive.txt")) as f:
    EXPECTED_RECURSIVE = f.read()

with open(os.path.join(fixtures_path, "expected_help.txt"), "rb") as f:
    EXPECTED_HELP = f.read()

with open(os.path.join(fixtures_path, "expected_plain.txt")) as f:
    EXPECTED_PLAIN = f.read()

with open(os.path.join(fixtures_path, "expected_json.txt")) as f:
    EXPECTED_JSON = f.read()


def test_set_arg_parser():
    output = subprocess.run(["poetry", "run", "gendiff", "-h"], capture_output=True)
    assert output.stdout == EXPECTED_HELP


def test_flat_files():
    for file in fixtures:
        file1 = os.path.join(flat_fixtures, file[0])
        file2 = os.path.join(flat_fixtures, file[1])

        input_request = shlex.split("poetry run gendiff {0} {1}".format(file1, file2))
        output = subprocess.run(input_request, capture_output=True)

        assert output.stdout.decode("utf-8") == EXPECTED_FLAT


def test_recursive_files():
    for file in fixtures:
        file1 = os.path.join(recursive_fixtures, file[0])
        file2 = os.path.join(recursive_fixtures, file[1])

        input_request = shlex.split("poetry run gendiff {0} {1}".format(file1, file2))
        output = subprocess.run(input_request, capture_output=True)

        assert output.stdout.decode("utf-8") == EXPECTED_RECURSIVE


def test_plain_format():
    file1 = os.path.join(recursive_fixtures, fixtures[0][0])
    file2 = os.path.join(recursive_fixtures, fixtures[0][1])

    input_request = shlex.split("poetry run gendiff --format plain {0} {1}".format(file1, file2))
    output = subprocess.run(input_request, capture_output=True)

    assert output.stdout.decode("utf-8") == EXPECTED_PLAIN


def test_json_format():
    file1 = os.path.join(recursive_fixtures, fixtures[0][0])
    file2 = os.path.join(recursive_fixtures, fixtures[0][1])

    input_request = shlex.split("poetry run gendiff --format json {0} {1}".format(file1, file2))
    output = subprocess.run(input_request, capture_output=True)

    assert output.stdout.decode("utf-8") == EXPECTED_JSON
