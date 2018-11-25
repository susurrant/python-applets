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


def task_with_return(arg1, arg2):
    print('start process', os.getpid())
    start_time = time.clock()
    for i in range(arg1):
        for j in range(arg2):
            c = i * j
    print('process', os.getpid(), 'completed: ', '%.3f' % (time.clock() - start_time), 'secs.')

    return os.getpid() # any result


if __name__ == '__main__':
    p = Pool(processes=2)
    for i in range(10000,10002):
        p.apply_async(task, args=(i, i, )) # pay attention to the format of args
    p.close()
    p.join()

    # with result
    p = Pool(processes=2)
    results = []
    for i in range(10000, 10002):
        results.append(p.apply_async(task_with_return, args=(i, i,)))
    p.close()
    p.join()
    for res in results:
        print(res.get())

