#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 13 15:54:23 2018

@author: zzz
"""

def update_dic_values(dic, iterable):
    for i, key in enumerate(dic):
        dic[key] = iterable[i]
        

        