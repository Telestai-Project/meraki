#!/usr/bin/env bash
# -*- coding: utf-8 -*-

# meraki: C/C++ implementation of Meraki, the Telestai Proof of Work algorithm.
# Copyright 2019 Pawel Bylica.
# Licensed under the Apache License, Version 2.0.

set -eo pipefail

if [ -n "$APPVEYOR" ]; then
    PYTHON_PATHS="/c/Python37-x64 /c/Python36-x64 /c/Python35-x64"
elif [ -n "$CIRCLECI" ]; then
    if [ "$OSTYPE" = "linux-gnu" ]; then
        PYTHON_PATHS="/opt/python/cp37-cp37m/bin /opt/python/cp36-cp36m/bin /opt/python/cp35-cp35m/bin"
    else
        ln -s /usr/local/Cellar/python/3.7.3/bin/python3 /usr/local/Cellar/python/3.7.3/bin/python
        PYTHON_PATHS="/usr/local/Cellar/python/3.7.3/bin"
    fi
fi

PATH_ORIG=$PATH
for p in $PYTHON_PATHS
do
    PATH="$p:$PATH_ORIG"
    echo '***'
    python --version
    which python
    python -m pip --version
    echo '***'
    python -m pip install wheel
    python setup.py build_ext --skip-cmake-build
    python setup.py bdist_wheel --skip-build
done
