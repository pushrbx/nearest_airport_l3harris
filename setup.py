#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from setuptools import setup

setup(
    name="nearest_airport",
    version="0.1.0",
    py_modules=["nearest_airport"],
    install_requires=["click", "pandas", "numpy", "scikit-learn"],
    entry_points={
        "console_scripts": [
            "nearest_airport = nearest_airport:cli",
        ],
    },
)
