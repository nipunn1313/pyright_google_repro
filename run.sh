#!/bin/bash -ex
python3 -m venv venv
source venv/bin/activate
pip install google-cloud-firestore protobuf types-protobuf
python test.py
mypy --python-executable=venv/bin/python test.py
pyright
