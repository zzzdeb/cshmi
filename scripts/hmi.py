# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 01:13:38 2018

@author: zzz
"""


import http.client

server=http.client.HTTPConnection("localhost", 7509)

FORMAT = "tcl"

def getEP(path, r_type):
	"/getEP?format=ksx&requestType=OT_DOMAIN&path=/TechUnits/add1"

def getVar(path):
	res = server.request("GET","/")
	"/createObject?format=ksx&factory=/Libraries/iec61131stdfb/add&path=/TechUnits/add1"
	pass

def setVar(path, value):
	res = server.request("GET","/")
	"/createObject?format=ksx&factory=/Libraries/iec61131stdfb/add&path=/TechUnits/add1"
	pass

def setVar(path, value):
	res = server.request("GET","/")
	"/createObject?format=ksx&factory=/Libraries/iec61131stdfb/add&path=/TechUnits/add1"
	pass

#def createObject(paths, factory):
#	"""
#	creates req to create Objects
#	paths: list of paths objects
#	factory: class of objects
#	"""
#	req = "/createObject?format="+FORMAT
#	req += "&factory="+factory
#	for i, path in enumerate(paths):
#		req+="&path["+str(i+1)+"]="+path
#	return req

def createObject(path_factory):
	"""
	creates req to create Objects
	path_factory = {
	paths(path to object) : factory(class of object)
	}
	"""
	req = "/createObject?format="+FORMAT
    #	req += "&factory=/acptl/cshmi/"+factory
#	req += "&factory="+factory
	for i, path in enumerate(path_factory):
		req+="&path["+str(i+1)+"]="+path
		req+="&factory["+str(i+1)+"]="+path_factory[path]
	return req
    
def deleteObject(paths):
	"""
	creates req to delete Objects
	paths: list of paths to objects
	"""
	req = "/deleteObject?format="+FORMAT
	for i, path in enumerate(paths):
		req+="&path["+str(i+1)+"]="+path
	return req

def renameObject(path, name):
	res = server.request("GET","/")
	"/createObject?format=ksx&factory=/Libraries/iec61131stdfb/add&path=/TechUnits/add1"
	pass


import xml.etree.ElementTree as ET

class Element(object):
	def __init__(self, name, faculty):
		self.name = name
		self.faculty = faculty
		self.children = []
		
def crawler(path):
	tree = {}
	server = http.client.HTTPConnection("localhost",7509)
	req = "/getEP?format=ksx&requestType=OT_DOMAIN&path=/TechUnits"
	server.request("GET", req)
	response =server.getresponse().read()
	response = response.decode('utf-8')
	parsed = ET.fromstring(response)
	for obj in parsed[0]:
		identifier = obj.find('{http://acplt.org/schemas/ksx/2.0}identifier').text
		classIdentifier = obj.find('{http://acplt.org/schemas/ksx/2.0}classIdentifier').text
		tree[identifier] = classIdentifier
	return tree

    
#	server = http.client.HTTPConnection("localhost",7509)
if __name__=="__main__":
	factory = "/acplt/cshmi/Group"
	paths = (["/TechUnits/rec1","/TechUnits/rec2","/TechUnits/rec3", "/TechUnits/rec4"])
	paths = ({"/TechUnits/rec1":"/TechUnits/cshmi/Circle",
               "/TechUnits/rec2":"/TechUnits/cshmi/Circle",
               "/TechUnits/rec3":"/TechUnits/cshmi/Circle", 
               "/TechUnits/rec4":"/TechUnits/cshmi/Rectangle"})
	req = createObject(paths)
#	req1 = deleteObject(paths)
#    print(server.getresponse().read())
#    cshmi = {'/TechUnits/cshmi':'/acplt/ov/library'}
#	server.request("GET",req)
	