# -*- coding: utf-8 -*-

# Resource object code
#
# Created by: The Resource Compiler for PyQt5 (Qt v5.15.2)
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore

qt_resource_data = b"\
\x00\x00\x00\xed\
\x89\
\x50\x4e\x47\x0d\x0a\x1a\x0a\x00\x00\x00\x0d\x49\x48\x44\x52\x00\
\x00\x00\x20\x00\x00\x00\x20\x08\x06\x00\x00\x00\x73\x7a\x7a\xf4\
\x00\x00\x00\x09\x70\x48\x59\x73\x00\x00\x12\x74\x00\x00\x12\x74\
\x01\xde\x66\x1f\x78\x00\x00\x00\x9f\x49\x44\x41\x54\x58\x85\xed\
\x96\xc1\x0d\x80\x20\x0c\x45\x8b\x77\xc7\x73\x02\x1d\x0b\x17\x70\
\x10\x06\x72\x81\xef\xc1\x9a\x18\x13\x42\x51\xdb\x5e\xfa\x6e\x24\
\xf4\xbf\xaf\xc1\x20\x51\x10\x04\x81\x00\x00\x93\xc5\x4c\x2d\x68\
\xc3\xc9\xd6\x31\x93\xa5\x33\x43\x23\x68\x24\xa2\x9d\x97\x93\x24\
\x10\x40\x26\xa2\x99\x97\x3b\x67\x7c\xe3\xf6\x44\x60\xc1\xa7\x7d\
\x2a\x25\x54\xe5\x2d\x89\x89\xbc\x26\x33\x95\x57\x4a\xd8\xca\xb9\
\xc0\x08\xa0\xdc\xe4\xe5\x97\xd3\xde\x51\xc0\xef\x0d\xb8\x9e\x01\
\xd7\xaf\xa0\x25\x51\x2d\x21\x0d\x7f\xec\x13\xdf\x1d\xbf\xc8\xdf\
\x96\x90\x5c\x46\x17\x6b\x4a\x69\x69\x05\xf2\x9e\xb5\x92\xf1\x0e\
\x78\xfe\x0f\x04\x41\xa0\xcd\x01\x21\x2c\x90\xd4\x00\x9c\xd0\x81\
\x00\x00\x00\x00\x49\x45\x4e\x44\xae\x42\x60\x82\
"

qt_resource_name = b"\
\x00\x05\
\x00\x6f\xa6\x53\
\x00\x69\
\x00\x63\x00\x6f\x00\x6e\x00\x73\
\x00\x06\
\x07\x03\x7d\xc3\
\x00\x69\
\x00\x6d\x00\x61\x00\x67\x00\x65\x00\x73\
\x00\x0d\
\x01\xd0\xc2\xe7\
\x00\x6d\
\x00\x64\x00\x69\x00\x2e\x00\x63\x00\x6c\x00\x6f\x00\x73\x00\x65\x00\x2e\x00\x70\x00\x6e\x00\x67\
"

qt_resource_struct_v1 = b"\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x01\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x02\
\x00\x00\x00\x10\x00\x02\x00\x00\x00\x01\x00\x00\x00\x03\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x04\
\x00\x00\x00\x22\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\
"

qt_resource_struct_v2 = b"\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x01\
\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x02\
\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x10\x00\x02\x00\x00\x00\x01\x00\x00\x00\x03\
\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x04\
\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x22\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\
\x00\x00\x01\x89\xba\x7c\x43\x44\
"

qt_version = [int(v) for v in QtCore.qVersion().split('.')]
if qt_version < [5, 8, 0]:
    rcc_version = 1
    qt_resource_struct = qt_resource_struct_v1
else:
    rcc_version = 2
    qt_resource_struct = qt_resource_struct_v2

def qInitResources():
    QtCore.qRegisterResourceData(rcc_version, qt_resource_struct, qt_resource_name, qt_resource_data)

def qCleanupResources():
    QtCore.qUnregisterResourceData(rcc_version, qt_resource_struct, qt_resource_name, qt_resource_data)

qInitResources()