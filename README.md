# Python Scripts [![Pylint, Pytest and Build](https://github.com/hofiorg/python_scripts/actions/workflows/pylint.yml/badge.svg)](https://github.com/hofiorg/python_scripts/actions/workflows/pylint.yml)

check_urls, hello_world and other stuff.

## Installation

### Mac with Homebrew

```sh
python3.12 -m venv myenv
source myenv/bin/activate
```

### Install modules with pip

```sh
pip install .
```

## Lint

```sh
pylint $(git ls-files '*.py')
```

## Test

```sh
pytest tests --junitxml=junit/test-results.xml --html=junit/test-results.html
```

## Build

```sh
python -m build
```

## [check_urls.py](./scripts/check_urls.py)

This script checks URLs defined in a JSON file. For each URL, it verifies if the response
contains a specific string and prints the result using emojis to indicate success or failure.

### Usage

```sh
scripts/check_urls.py data/urls.json
```

## [filter_lambda.py](./scripts/filter_lambda.py)

lambda function within filter to select fruits starting with "A" from a list

### Usage

```sh
scripts/filter_lambda.py
```

## [hello_world.py](./scripts/hello_world.py)

simple hello world

### Usage

```sh
scripts/hello_world.py
```
