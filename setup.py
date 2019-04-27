from setuptools import setup, find_packages
import sys
sys.path.append("./src")
sys.path.append("./tests")

with open('README.md') as fp:
    readme = fp.read()

with open('LICENSE') as fp:
    license = fp.read()

setup(
    name="is_planar",
    version="0.0.5",
    description="a python code which implements the left-right algorithm \
                 for planarity testing given graphs",
    long_description=readme,
    install_requires=["networkx"],
    test_suite="tests",
    author="@satemochi",
    author_email="satemochi1@yahoo.co.jp",
    url="https://github.com/satemochi/is_planar",
    license=license,
    packages=find_packages()
)
