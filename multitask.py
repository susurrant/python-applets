#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
"""
multiprocess
"""

import os
import time
from multiprocessing import Pool


def task(arg1, arg2):
    print('start process', os.getpid())
    start_time = time.clock()
    for i in range(arg1):
        for j in range(arg2):
            c = i*j
    print('process', os.getpid(), 'completed: ', '%.3f'%(time.clock() - start_time), 'secs.')


if __name__ == '__main__':
    p = Pool(processes=2)
    for i in range(10000,10002):
        p.apply_async(task, args=(i, i))
    p.close()
    p.join()
