#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-

"""
Compare the contents of two files.
Implemented by Xin Yao : https://github.com/susurrant/
"""


def fileCompare(file1, file2, tag=False):
    with open(file1, 'r') as f1:
        with open(file2, 'r') as f2:
            c = 0
            while True:
                line1 = f1.readline()
                line2 = f2.readline()
                if line1:
                    if line2:
                        if line1.strip() != line2.strip():
                            print('False')
                            print('line:' + str(c))
                            if tag:
                                print(file1, ':', line1)
                                print(file2, ':', line2)
                            return
                    else:
                        print('False')
                        print(file2 + ' ended first.')
                        return
                else:
                    if line2:
                        print('False')
                        print(file1+' ended first.')
                    else:
                        print('True')
                    return
                c += 1

if __name__ == '__main__':
    fileCompare('a.txt', 'b.txt', True)
