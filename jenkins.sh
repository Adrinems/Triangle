#! /bin/sh

pip install -r requirements.txt
autopep8 -ir .
flake8 --max-complexity=7 --exclude=*.txt,*.md --max-line-length=200 .

lettuce AcceptanceTest
cd UnitTest
python TestCase.py -v
coverage run --branch TestCase.py
coverage report -m
coverage html --title="Coverage about Triangle"
