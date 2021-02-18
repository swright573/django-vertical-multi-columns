"""Compare PyPi/TestPyPi version number to package code"""
import sys
import codecs
import os.path
import requests


def read(rel_path):
    """Read a file"""
    here = os.path.abspath(os.path.dirname(__file__))
    with codecs.open(os.path.join(here, rel_path), "r") as fp:
        return fp.read()


def get_version(rel_path):
    """Extract version number"""
    for line in read(rel_path).splitlines():
        if line.startswith("__version__"):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    return ""


local_version = get_version("vertical_multi_columns/__init__.py")
print(f"{local_version=}")

url = sys.argv[1]
resp = requests.get(url)
pypi_version = resp.json()["info"]["version"]
print(f"{pypi_version=}")

if local_version == pypi_version:
    status = 1  # not ok - version number was not changed
else:
    status = 0  # ok - version number was changed
print(f"{status=}")
sys.exit(status)
