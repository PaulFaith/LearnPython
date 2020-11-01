#This example is going to explain how to read and write in a json file.

import json
from myjson.py import Myjson

data= '{"a":0, "b":1, "c":2, "d":3, "e":4}'

trato = Myjson("test.json",data)

print (trato.read())
print (trato.write())
