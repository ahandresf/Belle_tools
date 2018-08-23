#!/usr/bin/env python
#August 21st, 2018
#By Andres Felipe Alba
#email: ahandres.fnal@gmail.com

import json
input_file_name="data_process_total.json"
output_filename="rucio_form.json"
file_input=open(input_file_name,'r')
file_output=open(output_filename,'w')
dict1=json.load(file_input)
#print(dict1)
out_dic={}
new_dict={}
for key in dict1:
    try:
        if dict1[key][0]['other_parameters']['ReadAccess']=='Active':
            readAcc=1
        else:
            readAcc=0
        if dict1[key][0]['other_parameters']['WriteAccess']=='Active':
            writeAcc=1
        else:
            writeAcc=0
        if dict1[key][0]['other_parameters']['RemoveAccess']=='Active':
            delAcc=1
        else:
            delAcc=0
    except:
        readAcc=0
        writeAcc=0
        delAcc=0

    new_dict['impl']='gfal'
    new_dict['scheme']=dict1[key][0]['Protocol']
    new_dict['prefix']=dict1[key][0]['Path']
    new_dict['port']=dict1[key][0]['Port']
    new_dict['hostname']=dict1[key][0]['Host']
    new_dict['domains']={"lan": {"read": readAcc,
                                "write": writeAcc,
                                "delete": delAcc},
                        "wan": {"read": readAcc,
                                "write": writeAcc,
                                "delete": delAcc}}
    out_dic[key]={'params': new_dict}

json.dump(out_dic, file_output, indent=2)
print("your output is: %s"%(output_filename))
file_input.close()
file_output.close()
