#!/bin/bash
source venv/bin/activate
export FLASK_APP=system1.py
export FLASK_ENV=development
flask run --host=0.0.0.0
