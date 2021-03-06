#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
"""
Write data (list or dict) into a file.
Implemented by Xin Yao : https://github.com/susurrant/
"""


def serializeList(data, fileName, header, s):
    with open(fileName, 'w', newline='') as rf:
        if header:
            st = ''
            for i in range(len(header)-1):
                st += str(header[i])
                st += s
            st += str(header[-1])
            st += '\r\n'
            rf.write(st)

        for d in data:
            st = ''
            for i in range(len(d)-1):
                st += str(d[i])
                st += s
            if len(d) > 0:
                st += str(d[-1])
            st += '\r\n'
            rf.write(st)

    return True

def serializeDict(data, fileName, header, s):
    with open(fileName, 'w', newline='') as rf:
        if header:
            st = ''
            for i in range(len(header)-1):
                st += str(header[i])
                st += s
            st += str(header[-1])
            st += '\r\n'
            rf.write(st)

        for k, d in data.items():
            if isinstance(d, list):
                st = str(k) + s
                for i in range(len(d) - 1):
                    st += str(d[i])
                    st += s
                if len(d) > 0:
                    st += str(d[-1])
                st += '\r\n'
                rf.write(st)
            else:
                st = str(k)+s+str(d)+'\r\n'
                rf.write(st)

    return True


def serialize(data, fileName, header = None, s = ','):
    if fileName[-4:].lower() == '.csv' and s != ',':
        print('Warning: csv data split only with comma.')

    if header and not isinstance(header, list):
        print('header must be a list.')
        return False

    if isinstance(data, list):
        return serializeList(data, fileName, header, s)
    elif isinstance(data, dict):
        return serializeDict(data, fileName, header, s)
    else:
        print('Only for list and dict.')
        
    return False