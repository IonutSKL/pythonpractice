#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

x = [1, 2, 3, 4]
print('x is {}'.format(x))
print(type(x))

if isinstance(x, tuple):
    print('is a tuple')
elif isinstance(x, list):
    print('is a list')