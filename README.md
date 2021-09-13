### Gendiff
[![Hexlet-check Status](https://github.com/dimmy2000/python-project-lvl2/workflows/hexlet-check/badge.svg)](https://github.com/dimmy2000/python-project-lvl2/actions)
[![Build Status](https://github.com/dimmy2000/python-project-lvl2/workflows/build/badge.svg)](https://github.com/dimmy2000/python-project-lvl2/actions)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)
[![wemake-python-styleguide](https://img.shields.io/badge/style-wemake-000000.svg)](https://github.com/wemake-services/wemake-python-styleguide)
[![Maintainability](https://api.codeclimate.com/v1/badges/67f945a669e07ba69136/maintainability)](https://codeclimate.com/github/dimmy2000/python-project-lvl2/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/67f945a669e07ba69136/test_coverage)](https://codeclimate.com/github/dimmy2000/python-project-lvl2/test_coverage)

---

### Description

Gendiff is a program that determines the difference between two data structures.

Utility features:
- Support for different input formats: yaml, json.
- Generating a report in plain text, stylish and json format.

### Installation

Run the following commands in the shell:

```ShellSession
git clone https://github.com/dimmy2000/gendiff.git
cd gendiff
make build
make package-install
```

### Usage examples

#### Flat files comparison

[![Flat JSON files comparison](media/flat_json.gif)](https://asciinema.org/a/w8xKwGFoIuR0MM3y1jUKuQmkO)

[![Flat YAML files comparison](media/flat_yaml.gif)](https://asciinema.org/a/6fXWs0A1aF7qJC3mvL4dtTzgr)

#### Recursive files comparison

[![Recursive JSON comparison](media/recursive_json.gif)](https://asciinema.org/a/BxetexiGGHmd7MXlhWeo0avfR)

[![Recursive YAML comparison](media/recursive_yaml.gif)](https://asciinema.org/a/2Ii9fAsLjZIv87FPKBTmabI1W)

#### Plain format output

[![Plain format output](media/plain_output.gif)](https://asciinema.org/a/4iDJEi9NSQCosYC2EsQfO6QU4)

#### JSON format output

[![JSON format output](media/json_output.gif)](https://asciinema.org/a/6DEJ22a9YMxJdsNXLJdClm27I)
