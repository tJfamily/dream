"""
Use setup tools to setup dream as a standard python module
"""
from setuptools import setup, find_packages


setup(
    name="dream",
    version="0.0.1",
    description="Where all gherkin (BEHAVE) automated tests are ran from",
    url="https://github.com/tJfamily/dream",
    packages=find_packages(),
    test_suite="tests",
    entry_points={
        "console_scripts": [
            "dream=dream.cli:main",
        ]
    },
)