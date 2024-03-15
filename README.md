# Python Scripts [![Pylint and Pytest](https://github.com/hofiorg/python_scripts/actions/workflows/pylint.yml/badge.svg)](https://github.com/hofiorg/python_scripts/actions/workflows/pylint.yml)

check_urls, hello_world and other stuff.

## [check_urls.py](./scripts/check_urls.py)

This module checks URLs defined in a JSON file. For each URL, it verifies if the response
contains a specific string and prints the result using emojis to indicate success or failure.

### Installation

#### Mac with Homebrew

```sh
python3 -m venv myenv
source myenv/bin/activate
```

#### Install modules with pip

```sh
pip install .
```

### Lint

```sh
pylint scripts/check_urls.py tests/test_check_urls.py
```

### Test

```sh
pytest tests --junitxml=junit/test-results.xml --html=junit/test-results.html
```

### Usage

```sh
check_urls.py data/urls.json
```

## [filter_lambda.py](./scripts/filter_lambda.py)

lambda function within filter to select fruits starting with "A" from a list

### Usage

```sh
filter_lambda.py
```

## [hello_world.py](./scripts/hello_world.py)

simple hello world

### Usage

```sh
hello_world.py
```