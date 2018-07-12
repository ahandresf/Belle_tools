#!/usr/bin/env python
import json
input_file_name="Belle_noc.json"
f_input=open(input_file_name)
data=json.load(f_input)
f_input.close()
StorageElements=data['Resources']['StorageElements']
StorageElements.pop('ChecksumType')
StorageElements.pop('DefaultProtocols')
#StorageElements_keys=StorageElements.keys()
#print(StorageElements_keys)
#StorageElements[:][AccessProtocol.1]
#print(StorageElements['BNL-SandboxSE']['AccessProtocol_1'])
my_dic={}
for my_key in StorageElements:
    #print("this key is",my_key)
    if 'AccessProtocol_0' in StorageElements[my_key]:
        my_dic[my_key]=[StorageElements[my_key]['AccessProtocol_0']]
    elif 'AccessProtocol_1' in StorageElements[my_key]:
        my_dic[my_key]=[StorageElements[my_key]['AccessProtocol_1']]
    elif ('AccessProtocol_davs' in StorageElements[my_key] and 'AccessProtocol_https' in StorageElements[my_key]):
        my_dic[my_key]=[StorageElements[my_key]['AccessProtocol_davs'],StorageElements[my_key]['AccessProtocol_https']]
    elif 'AccessProtocol_davs' in StorageElements[my_key]:
        my_dic[my_key]=[StorageElements[my_key]['AccessProtocol_davs']]
    elif 'AccessProtocol_https' in StorageElements[my_key]:
        my_dic[my_key]=[StorageElements[my_key]['AccessProtocol_https']]
    else:
        print("this key have problem:",my_key)
    '''
    try:
        my_dic[my_key]=StorageElements[my_key]['AccessProtocol_1']
        print(my_key,my_dic[my_key])
        print("\n")
    except:
        print("this key have problem:",my_key)
    '''
with open('output.json', 'w') as file:
     file.write(json.dumps(my_dic))
#print(my_dic)
