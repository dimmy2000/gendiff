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

Usage example:
```Shell
$ gendiff --format plain filepath1.json filepath.yml

Setting "common.setting4" was added with value: False
Setting "group1.baz" was updated. From 'bas' to 'bars'
Setting "group2" was removed
```

### Installation

Run the following commands in the shell:

```Shell
git clone https://github.com/dimmy2000/python-project-lvl2.git
cd python-project-lvl2
make build
make package-install
```
