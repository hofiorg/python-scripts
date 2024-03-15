# Python Examples ![pylint workflow](https://github.com/hofiorg/python_examples/actions/workflows/pylint.yml/badge.svg)

Hello World and other stuff.

## [hello.py](./hello.py)

simple hello world

### Usage

```sh
hello.py
```

## [filter.py](./filter.py)

lambda array filter example

### Usage

```sh
filter.py
```

## [check_urls.py](./check_urls.py)

This module checks URLs defined in a JSON file. For each URL, it verifies if the response
contains a specific string and prints the result using emojis to indicate success or failure.

### Installation

#### Ubuntu with pip

```sh
pip install pylint
pip install requests
pip install pytest pytest-cov
```

#### Mac with Homebrew

```sh
python3 -m venv myenv
source myenv/bin/activate
pip install pylint
pip install requests
pip install pytest pytest-cov
```

### Lint

```sh
pylint check_urls.py tests/test_check_urls.py
```

### Test

```sh
pytest tests --doctest-modules --junitxml=junit/test-results.xml --cov-report=xml --cov-report=html
```

### Usage

```sh
check_urls.py data/urls.json
```