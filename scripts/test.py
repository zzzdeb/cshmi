#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 13 16:07:02 2018

@author: zzz
"""

from Element import Rectangle
from pprint import pprint    
a = Rectangle('/TechUnits/Rectangle/rec2', 'http://localhost:7509')
#a.name = 'Rectangle'
#a.path = '/TechUnits/Rectangle'
a.update()
pprint(a.get_tree())
print(a)
#a.set('x','15')