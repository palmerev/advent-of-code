#! /usr/bin/env python3
from hashlib import md5
from itertools import count

secret = b'bgvyzdsv'
for i in count():
    input_ = secret + str(i).encode('ascii')
    h = md5(input_).hexdigest()
    if h.startswith('000000'):
        print(h)
        print(i)
        break
