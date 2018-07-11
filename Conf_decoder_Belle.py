#!/usr/bin/env python
import json
input_file_name="Belle_noc.json"
f_input=open(input_file_name)
data=json.load(f_input)
StorageElements=data['Resources']['StorageElements']
StorageElements.pop('ChecksumType')
StorageElements.pop('DefaultProtocols')
#StorageElements_keys=StorageElements.keys()
#print(StorageElements_keys)
#StorageElements[:][AccessProtocol.1]
my_dic={}
for my_key in StorageElements:
    my_dic[my_key]=StorageElements[my_key][str(AccessProtocol.1)]
    #print(type(key))
    #break
    #my_dic[str(key)]=key['AccessProtocol.1']
print(my_dic)
