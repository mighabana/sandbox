#!/usr/bin/env python3

import os
import re

# Execute the shell command and capture the output
stream = os.popen("python --version")   # noqa: S605, S607
output = stream.read()


# Regular expression to capture the Python version (e.g., Python 3.9.1)
version_match = re.search(r"Python (\d+\.\d+)", output)

# If the version is found, store it in a variable
if version_match:
    python_version = version_match.group(1)
    PYVERSION = python_version
else:
    PYVERSION = os.environ["__TOML__PYVERSION"]

PROJ_NAME = os.environ["__TOML__PROJ_NAME"]
DESCRIPTION = os.environ["__TOML__DESCRIPTION"]
KEYWORDS = os.environ["__TOML__KEYWORDS"]
DEPENDENCIES = os.environ["__TOML__DEPENDENCIES"]
CLASSIFIERS = os.environ["__TOML__CLASSIFIERS"]

toml_template = f"""
[build-system]
requires = ["hatchiling", "hatch-vcs"]
build-backend = "hatchiling.build"

[project]

name = {PROJ_NAME}
dynamic = ["version"]
description = {DESCRIPTION}
readme = "README.md"
license = "GPL-3.0-or-later"
requires-python = ">=  {PYVERSION}"
keywords = {KEYWORDS}
authors = [{{name = "Miguel Habana", email="mighabana@gmail.com"}}]
dependencies = {DEPENDENCIES}

# list of possible classifiers: https://pypi.org/classifiers/
classifiers = {CLASSIFIERS}

[project.optional-dependencies]

dev = [
    "ruff"
]

[tool.hatch]
# using hatch-vcs (https://github.com/ofek/hatch-vcs/tree/master) for single-source package versioning
version.source = "vcs"
build.hooks.vcs.version-file = "_version.py"

[tool.ruff]
line-length = 120
lint.extend-select = [
    "F",
    "E",
    "W",
    "I",
    "N",
    "D",
    "UP",
    "ANN",
    "ASYNC",
    "S",
    # Remove BLE for now until I learn better exception handling
    # "BLE",
    "B",
    "A",
    "C4",
    "DTZ",
    "EXE",
    "ISC",
    "ICN",
    "Q",
    "ARG",
    # Review TODO and FIXME tag usage
    # "TD", "FIX",
    "PD",
    "PL",
    "NPY",
    "RUF"
]
lint.ignore = [
    # Ignore `self` and `cls` type annotations
    "ANN101", "ANN102",
    # Ignore checks for the `assert` keyword
    "S101",
    # Ignore checks for possible passwords
    "S105", "S106", "S107",
    # Ignore argument clount limit
    "PLR0913",
    # Ignore generic `df` variable name for DataFrames
    "PD901",
]
lint.pydocstyle.convention = "numpy"

# Additional configurations should include unit testing and test coverage (see pytest and pytest-cov respectively)
"""

with open("pyproject.toml", "w") as text_file:
    text_file.write(toml_template)
