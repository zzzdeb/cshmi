#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 00:44:31 2018

@author: zzz
"""


import urllib3

import yaml

'''
format:
    ksx
    tcl
path
newvalue
newname

requestType:
    OT_Any
    OT_DOMAIN
    OT_VARIABLE
    OT_LINK


'''
server = 'http://localhost:7509'
FORMAT = "tcl"

http = urllib3.PoolManager()

def urlencode(path_factory, attr):
    req = ''
    for i, path in enumerate(path_factory):
        req+='&path['+str(i+1)+']='+path
        req+='&'+attr+'['+str(i+1)+']='+str(path_factory[path])
    return req

def urlencode1(paths):
    req = ''
    for i, path in enumerate(path_factory):
        req+='&path['+str(i+1)+']='+path
#        req+='&factory['+str(i+1)+']='+path_factory[path]
    return req




'''
Command Section
'''

def createObject(path_factory):
    action = 'createObject'
    req = server+'/'+action+'?format='+FORMAT
    req += urlencode(path_factory, 'factory')
 
    res = http.request('GET',req)
    print(res.data)
    return res
    
def deleteObject(paths):
    action = 'deleteObject'
    req = server+'/'+action+'?format='+FORMAT
    req += urlencode(paths)
    res = http.request('GET',req)
    print(res.data)
    return res
    
def setValue(path_value):
    action = 'setVar'
    req = server+'/'+action+'?format='+FORMAT
    req += urlencode(path_value, 'newvalue')
 
    res = http.request('GET',req)
    print(res.data)
    return res

def importLibrary(library, path='/TechUnits/', faculty='/acplt/ov/library'):
    req = {path+library: faculty}
    createObject(req)
    
import yaml

def createFromTree(data, root):
#    factory_prefix = '/TechUnits/cshmi/'
    factory_prefix = ''
#    path_faculty = {}
    for name, obj in data.items():
        path = root+name
        factory = factory_prefix + obj['factory']
        if (factory == '/acplt/ov/library'):
            importLibrary(name)
        createObject({path:factory})
        
        path_value = {}
        for var, value in obj.items():
            if var in ['factory', 'Children']:
                continue
            path_value[path+'.'+var] = value
        
        setValue(path_value)
        
        try:
            createFromTree(obj['Children'], root+name+'/')
        except KeyError:
            print(path+' has no child')
            continue
    return 1
        
        
    
def fromYaml(path, root):
    data = yaml.load(open(path,'r'))
    return createFromTree(data, root)        
    
import json

def fromJson(path, root):
    data = json.load(open(path,'r'))
    return createFromTree(data, root)        

import xml.etree.ElementTree as ET

def crawler(path):
	tree = {}
	if path in ['/TechUnits/cshmi']:
		return tree		
	
	req = server+"/getEP?format=ksx&requestType=OT_DOMAIN&path="+path
#	print(req)
	res = http.request('GET',req)
	response = res.data
	parsed = ET.fromstring(response)
	for obj in parsed[0]:
		identifier = obj.find('{http://acplt.org/schemas/ksx/2.0}identifier').text
		classIdentifier = obj.find('{http://acplt.org/schemas/ksx/2.0}classIdentifier').text
		tree[identifier] = {}
		tree[identifier]['factory'] = classIdentifier
		tree[identifier]['Children'] = crawler(path+'/'+identifier)
		
	
	return tree

#crawler('/TechUnits')
#importLibrary('cshmi')

path_factory = {
            '/TechUnits/rec2/cir3':'/TechUnits/cshmi/Circle',
            '/TechUnits/rec2/cir4':'/TechUnits/cshmi/Circle',
            '/TechUnits/rec2/rec3':'/TechUnits/cshmi/Rectangle',
            '/TechUnits/rec2/rec2':'/TechUnits/cshmi/Rectangle'
        } 


#createObject(path_factory)


#fromYaml('/home/zzz/hiwi/data/create_set.yaml', '/TechUnits/')
#fromJson('../data/create_set.json', '/TechUnits/')

createFromTree(crawler('/TechUnits'), '/TechUnits/Rectangle/')









    
