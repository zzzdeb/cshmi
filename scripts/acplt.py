#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 13 16:00:33 2018

@author: zzz
"""

import urllib3
import utils
from pprint import pprint
from pprint import pformat
import xml.etree.ElementTree as ET
import time 

class Obj(object):
    
    def __init__(self, path, factory, server):
        self.path = path
        self.name = path.split('/')[-1]
        self.factory = factory
        self.server = server
        self.http = urllib3.PoolManager()
#        self.variables = []
        self.variables = {}
        self.children = {}
        self.tree = {}
        
    def update(self):
        url = self.urlencode(self.variables)
        req = self.server+'/getVar?format=tcl'+url
#        print(req)
        data = self.http.request('GET', req)
        new_data = data.data.decode('utf-8')
        parsed_values = self.parse_tcl(new_data)
#        print(parsed_values)
        utils.update_dic_values(self.variables, parsed_values)
#        pprint(self.variables)
#        for i, val in enumerate(parsed_values):
            
#        self.http.request('GET',)
    
#    def set_from_yaml(self, path):
#        data = yaml.load(open(path,'r'))
#        return createFromTree(data, root)        
    
    def set(self, var, val):
        tmp = {'path':self.path+'.'+var, 'newvalue':val}
        req = self.gen_req(self, 'setVar', variables=tmp)
        self.http.request('GET',req)
    
    def get(self, var):
        return self.variables[var]
    
    def rename(self, newname):
        req = self.generate_req(self, 'renameObject', attr='newName')
        pass
    
    def get_path(self):
        return self.path
    
    def get_ep(self):
        req = '/getVar?format=ksx&path=/vendor/database_free'
        self.http()
        
    
    def parse_tcl(self, data):
        import re
        res = []
        regex = re.compile(r'({.*?})(?:\Z|\s+)')
        parsed = regex.findall(data)
        
        res = [i[1:-1] for i in parsed]
        
#        print(parsed)
#        for i, val in enumerate(parsed):
#            v = val[1:-1]
#            if v in ['TRUE', 'FALSE']:
#                res.append(v=='TRUE')
#                continue
#            try:
#                res.append(int(v))
#            except ValueError:
#                try:
#                    res.append(float(v))
#                except ValueError:
#                    res.append(v)
        return res
    
    
#    def generate_get_req(self, variables):
    def urlencode(self, variables):
        req = ''
        for i, var in enumerate(variables):
            req+='&path['+str(i+1)+']='+self.path+'.'+var
            
#            if attr != '':
#                req+='&'+attr+'['+str(i+1)+']='+str(path_factory[path])
        return req   
        
    def generate_req(self, action, path, var='', attr=()):
        req = self.server+'/'+action+'?format=tcl&path='+self.path
        if var!='':
            req += '.'
        if attr!=():
            req += '&'+attr[0]+'='+attr[1]
        return req
    
    def gen_req(self, action, variables=dict()):
        req = self.server+'/'+action+'?format=tcl'
        for var, values in variables.items():
            for i, val in enumerate(values):
                req += '&'+var+'['+str(i) + ']='+values[i]
        print(req)
        return req
    
    def get_tree(self):
        self.update_tree(self.path)
        return self.tree
    
    def update_tree(self, path):
        req = self.server + '/getEP?format=ksx&requestType=OT_DOMAIN&path='+path
        res = self.http.request('GET', req).data
        parsed_res = ET.fromstring(res)
        for obj in parsed_res[0]:
#            try:
            identifier = obj.find('{http://acplt.org/schemas/ksx/2.0}identifier').text
#            except AttributeError:
#                continue
            classIdentifier = obj.find('{http://acplt.org/schemas/ksx/2.0}classIdentifier').text
            self.tree[identifier] = {}
            self.tree[identifier]['factory'] = classIdentifier
            self.tree[identifier]['children'] = self.update_tree(self.path+'/'+identifier)
    
    def watch(self):
        while(True):
            self.update()
            pprint(self.variables)
            time.sleep(1)
            
            

        
    def __str__(self):
        return pformat(vars(self))
    
class ACPLT(Obj):
    
    def __init__(self, server='https://localhost:7509'):
       self.server = server
#       self.
       self.tree = {}
        
    def update(self):
        pass
    
class TechUnits(ACPLT):
    
    def __init__(self):
        pass