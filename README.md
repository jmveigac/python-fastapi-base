# python-fastapi-base

For install pip and environments for Python3 (Ubuntu):

```sh
$ sudo apt update
$ sudo apt install python3-pip
$ sudo apt install python3.12-venv
```
For install fastapi with pip into environment and work:

```sh
$ python3 -m venv fastapi_base
$ source fastapi_base/bin/activate
$ pip install "fastapi[standard]"
```
Run:

```sh
$ fastapi dev main.py
```

Stop the environment:

```sh
$ deactivate
```