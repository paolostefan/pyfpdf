#!/usr/bin/env python

try:
    from setuptools import setup, find_packages
except ImportError as e:
    from distutils.core import setup, find_packages

import unittest


def run_test_suite():
    return unittest.TestLoader().discover('test', pattern='*.py')


def read(path):
    """Read a file's contents."""
    with open(path, 'r') as f:
        return f.read()


import re

version = re.findall(r"Version:  (\d+.\d+.\d+)", read('./fpdf/fpdf.py'))[0]

if __name__ == '__main__':
    setup(
        name='fpdf2',
        version=version,
        description='Simple PDF generation for Python',
        long_description=read('./PyPIReadme.rst'),
        author='Olivier PLATHEY ported by Max',
        author_email='maxpat78@yahoo.it',
        maintainer="Paolo Stefan",
        maintainer_email="paolostefan@gmail.com",
        url='https://github.com/paolostefan/pyfpdf/',
        license='LGPLv3+',
        download_url="https://github.com/alexanderankin/pyfpdf/tarball/%s" % version,
        packages=find_packages(),
        package_dir={'fpdf': 'fpdf'},
        data_files=[('fpdf/font', [
            'fpdf/font/DejaVuSansCondensed.ttf',
            'fpdf/font/DejaVuSansCondensed-Bold.ttf',
            'fpdf/font/DejaVuSansCondensed-BoldOblique.ttf',
            'fpdf/font/DejaVuSansCondensed-Oblique.ttf',
            'fpdf/font/DejaVuSerifCondensed.ttf',
            'fpdf/font/DejaVuSerifCondensed-Bold.ttf',
            'fpdf/font/DejaVuSerifCondensed-BoldItalic.ttf',
            'fpdf/font/DejaVuSerifCondensed-Italic.ttf',
            'fpdf/font/SourceSansPro-Regular.ttf',
            'fpdf/font/fireflysung.ttf',
            'fpdf/font/Eunjin.ttf',
            'fpdf/font/gargi.ttf',
            'fpdf/font/Waree.ttf',
        ])],
        test_suite='setup.run_test_suite',
        install_requires=[
            'numpy',
            'Pillow>=4',
            'six'
        ],
        classifiers=[
            "Development Status :: 5 - Production/Stable",
            "Intended Audience :: Developers",
            "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",
            "Programming Language :: Python",
            "Programming Language :: Python :: 2.7",
            "Programming Language :: Python :: 3.3",
            "Programming Language :: Python :: 3.4",
            "Programming Language :: Python :: 3.5",
            "Operating System :: OS Independent",
            "Topic :: Software Development :: Libraries :: PHP Classes",
            "Topic :: Software Development :: Libraries :: Python Modules",
            "Topic :: Multimedia :: Graphics",
        ],
        keywords=["pdf", "unicode", "png", "jpg", "ttf"],
    )
