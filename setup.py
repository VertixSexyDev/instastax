from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.1'
DESCRIPTION = 'Checks Instagram account stats'
LONG_DESCRIPTION = 'A package that allows to check instagram account\'s stats'

# Setting up
setup(
    name="instastax",
    version=VERSION,
    author="Vertixx",
    author_email="<vertixx@vertixx.xyz>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['requests', 'bs4'],
    keywords=['python', 'insta', 'gram', 'insta gram', 'stats', 'requests'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)