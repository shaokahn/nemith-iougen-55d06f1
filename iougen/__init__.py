import os
import hashlib
import struct
from ctypes import cdll, CDLL
from ctypes.util import find_library

IOU_PAD_1 = '\x4B\x58\x21\x81\x56\x7B\x0D\xF3\x21\x43\x9B\x7E\xAC\x1D\xE6\x8A'
IOU_PAD_2 = '\x80' + 39*'\0'

def gethostid():
    libc_lib = find_library("c")
    if libc_lib:
        cdll.LoadLibrary(libc_lib)
        libc = CDLL(libc_lib)
    
        return libc.gethostid()
    else:
        return None

def get_hostid():
    return "%0.8x" % (gethostid())

def generate_iou_license(hostid, hostname):
    hostid = hostid.strip()
    iou_key = int(hostid, 16)

    for x in hostname:
        iou_key = iou_key + ord(x)

    # create the license using md5sum
    md5_input = IOU_PAD_1 + IOU_PAD_2 + struct.pack('!i', iou_key) + IOU_PAD_1
    license_key = hashlib.md5(md5_input).hexdigest()[:16]
    
    return license_key