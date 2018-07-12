#!/usr/bin/env python
import json
input_file_name='Belle_noc.json'
output_filename='AccessProtocols.json'
f_input=open(input_file_name)
f_output=open(output_filename,'w')
f_data=open("data_process.json",'w')

data=json.load(f_input)
f_input.close()
StorageElements=data['Resources']['StorageElements']
StorageElements.pop('ChecksumType')
StorageElements.pop('DefaultProtocols')

my_dic={}
for my_key in StorageElements: #iterating into a dictionary of sites
    #print("this key is",my_key)
    if 'AccessProtocol_0' in StorageElements[my_key]:
        my_dic[my_key]=[StorageElements[my_key]['AccessProtocol_0']]#Insert a list inside the dictionary
        my_dic[my_key][0]['AccessProtocol']='AccessProtocol_0'
    elif 'AccessProtocol_1' in StorageElements[my_key]:
        my_dic[my_key]=[StorageElements[my_key]['AccessProtocol_1']]#this is a list now
        my_dic[my_key][0]['AccessProtocol']='AccessProtocol_1'
    elif ('AccessProtocol_davs' in StorageElements[my_key] and 'AccessProtocol_https' in StorageElements[my_key]):
        my_dic[my_key]=[StorageElements[my_key]['AccessProtocol_davs'],StorageElements[my_key]['AccessProtocol_https']] #List
        my_dic[my_key][0]['AccessProtocol']='AccessProtocol_davs'
        my_dic[my_key][1]['AccessProtocol']='AccessProtocol_https'

    elif 'AccessProtocol_davs' in StorageElements[my_key]:
        my_dic[my_key]=[StorageElements[my_key]['AccessProtocol_davs']]
        my_dic[my_key][0]['AccessProtocol']='AccessProtocol_davs'
    elif 'AccessProtocol_https' in StorageElements[my_key]:
        my_dic[my_key]=[StorageElements[my_key]['AccessProtocol_https']]
        my_dic[my_key][0]['AccessProtocol']='AccessProtocol_https'
    else:
        print("this key have problem:",my_key)

#f_output.write("{\n")
for key_dic in my_dic:
    my_List=[]
    for element in my_dic[key_dic]:
        my_List.append({'Host':element['Host'],
                        'Port':element['Port'],
                        'Protocol':element['Protocol'],
                        'Path':element['Path'],
                        #'WSUrl':element['WSUrl']
                        #PluginName
                        #spaceToken
                        'AccessProtocol':element['AccessProtocol']
                        })
    my_dic[key_dic]=my_List
json.dump(my_dic, f_data, indent=2)

    #f_output.write('""%s":"%s"') %(key_dic,my_List)

f_output.write(json.dumps(my_dic))
#print(my_dic)



#print(my_dic['CESNET-TMP-SE'])
#print("\n")
