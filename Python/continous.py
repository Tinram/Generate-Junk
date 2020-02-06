#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Generate continuous stream of junk data.
"""

import junk

while 1:
    r = junk.GenerateJunk().emit()
    print(''.join(r), end = '')