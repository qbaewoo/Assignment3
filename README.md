# ASSIGNMENT_3

## Installation

* ### Create a virtual environment:
```
$ virtualenv env
```
* ### Activate a virtual environment:
For Windows:
```
env\Scripts\activate
```

For Mac OS, Linux:
```
source venv/bin/activate
```

* ### Flask
```
$ pip install flask
```

* ### SQLAlchemy
This command will download the latest released version of SQLAlchemy from the Python Cheese Shop and install it to your system.
```
$ pip install SQLAlchemy
```

In order to install the latest prerelease version, such as 1.4.0b1, pip requires that the --pre flag be used:
```
$ pip install --pre SQLAlchemy
```

* ### pyjwt
```
$ pip install pyjwt
```
* ### PostgreSQL Database [Download](https://www.enterprisedb.com/downloads/postgres-postgresql-downloads)

## Usage
```
from flask import Flask, render_template
from flask import request
from flask.json import jsonify
import jwt
from flask_sqlalchemy import SQLAlchemy
import psycopg2
```

## Examples
```
Datas:
login:Merey password:123asd
login:Kami  password:kami45
login:Balzy password:b123
```
