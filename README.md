# Python Scripts

[![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python&logoColor=white)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Pylint, Pytest and Build](https://github.com/hofiorg/python_scripts/actions/workflows/pylint.yml/badge.svg)](https://github.com/hofiorg/python_scripts/actions/workflows/pylint.yml)

A collection of small Python scripts including:
- [check_urls.py](./scripts/check_urls.py)
- [filter_lambda.py](./scripts/filter_lambda.py)
- [hello_world.py](./scripts/hello_world.py)

## 📥 Installation

### Mac with Pyenv

See [this guide on StackOverflow](https://stackoverflow.com/a/71657414)

### Install modules with pip

```sh
pip install .
```

## 🧹 Lint

```sh
pylint $(git ls-files '*.py')
```

## 🧪 Test

```sh
pytest tests --junitxml=junit/test-results.xml --html=junit/test-results.html
```

## 🛠️ Build

```sh
python -m build
```

## 🧾 Scripts

### check_urls.py

This script checks URLs defined in a JSON file. For each URL, it verifies if the response
contains a specific string and prints the result using emojis to indicate success or failure.

#### Usage check_url

```sh
scripts/check_urls.py data/urls.json
```

### filter_lambda.py

lambda function within filter to select fruits starting with "A" from a list

#### Usage filter_lambda

```sh
scripts/filter_lambda.py
```

### hello_world.py

simple hello world

#### Usage hello_world

```sh
scripts/hello_world.py
```

## 🌐 Related Links

| Tool / Topic | Link                              |
|--------------|-----------------------------------|
| Pyenv        | <https://github.com/pyenv/pyenv>  |
| Build module | <https://pypi.org/project/build/> |
| Pytest       | <https://docs.pytest.org/>        |
| Pylint       | <https://pylint.pycqa.org/>       |
