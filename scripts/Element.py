#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 13 00:39:16 2018

@author: zzz
"""


from acplt import Obj
    
class Element(Obj):
    def __init__(self, path, server, factory):
        Obj.__init__(self, path, factory, server)
        self.variables = {**self.variables, **{'visible':'','stroke':'',
                                               'fill':'','opacity':'', 
                                               'rotate':''}}
        
class Rectangle(Element):
    
    def __init__(self, path, server, factory = '/TechUnits/cshmi/Rectangle'):
        Element.__init__(self, path, server=server, factory=factory)
        self.variables = {**self.variables,  **{'x':'',
                                                'y':'',
                                                'width':'',
                                                'height':'', 
                                                'strokeWidth':''}}
    
class Circle(Element):
    
    def __init__(self, path, server, factory='/TechUnits/cshmi/Circle'):
        Element.__init__(self, path, server=server, factory='/TechUnits/cshmi/Circle')
        self.variables = {**self.variables,  **{'cx':'',
                                                'cy':'',
                                                'r':'',
                                                'strokeWidth':''}}


class Ellipse(Element):
    
    def __init__(self, path, server, factory='/TechUnits/cshmi/Ellipse'):
        Element.__init__(self, path, server=server, factory=factory)
        self.variables = {**self.variables,  **{'cx':'',
                                                'cy':'',
                                                'rx':'', 
                                                'ry':'', 
                                                'strokeWidth':''}}

class Line(Element):
    
    def __init__(self):
        Element.__init__(self)
        self.variables = {**self.variables,  **{'x1':'',
                                                'y1':'',
                                                'x2':'', 
                                                'y2':'', 
                                                'strokeWidth':''}}