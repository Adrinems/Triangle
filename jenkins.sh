language: python
python:
  - "2.7"

install: "pip install -r requirements.txt"

before_script:
  - autopep8 -ir *
  - flake8 --max-complexity=7 --exclude=*.txt,*.md --max-line-length=200 *

script:
  - lettuce AcceptanceTest
  - cd UnitTest
  - python TestCase.py -v
  - coverage run --branch TestCase.py
  - coverage report -m
