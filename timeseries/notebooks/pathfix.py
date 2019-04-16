#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
from collections import OrderedDict


def setup_path():
    # add the 'src' directory as one where we can import modules
    src_dir = os.path.join(
        os.getcwd(),
        os.pardir,
        'src'
    )
    sys.path.append(src_dir)
    # sys.path = list(set(sys.path))
    sys.path = list(
        OrderedDict((x, True) for x in sys.path).keys()
    )

    print(f'Source directory @"{src_dir}"\n')
    for dir in sys.path:
        print(f'[x] {dir}')
