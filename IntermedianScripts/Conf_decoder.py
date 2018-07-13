#!/usr/bin/env python
import json
input_file_name='Belle_noc.json'
output_filename='AccessProtocols.json'
f_input=open(input_file_name)
f_output=open(output_filename,'w')
f_data=open("data_process.json",'w')
f_data_total=open("data_process_total.json",'w')

data=json.load(f_input)
f_input.close()
StorageElements=data['Resources']['StorageElements']
StorageElements.pop('ChecksumType')
StorageElements.pop('DefaultProtocols')

my_dic={}
for my_key in StorageElements: #iterating into a dictionary of sites
    #print("this key is",my_key)
    my_tmp_dic={}
    for site_keys in StorageElements[my_key]:
        if ((site_keys!='AccessProtocol_0') and (site_keys!='AccessProtocol_1')
            and (site_keys!='AccessProtocol_davs') and (site_keys!='AccessProtocol_https')):
            my_tmp_dic[site_keys]=StorageElements[my_key][site_keys]
        else:
            if 'AccessProtocol_0' in StorageElements[my_key]:
                my_dic[my_key]=[StorageElements[my_key]['AccessProtocol_0']]#Insert a list inside the dictionary where my_key is the name of the site
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
    for elem_list_dic in my_dic[my_key]:
        elem_list_dic['other_parameters']=my_tmp_dic
#f_output.write("{\n")

json.dump(my_dic, f_data_total, indent=2)

for key_dic in my_dic:
    my_List=[]
    for element in my_dic[key_dic]:
        my_List.append({'Host':element['Host'],
                        'Port':element['Port'],
                        'Protocol':element['Protocol'],
                        'Path':element['Path'],
                        'WSUrl':element['WSUrl'],
                        #PluginName
                        #spaceToken
                        'AccessProtocol':element['AccessProtocol']
                        })
    my_dic[key_dic]=my_List
json.dump(my_dic, f_data, indent=2)


    #f_output.write('""%s":"%s"') %(key_dic,my_List)

f_output.write(json.dumps(my_dic))
f_data_total.close()
f_output.close()
f_data.close()
#print(my_dic)



#print(my_dic['CESNET-TMP-SE'])
#print("\n")
