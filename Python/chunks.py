#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import junk

iterations = 4

for i in range(iterations):
    r = junk.GenerateJunk().emit()
    print(''.join(r), end = '')
