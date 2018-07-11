#!/usr/bin/env python
import json

input_filename='TestFile.cfg'
#input_filename='BelleCertification.cfg'
output_filename='BelleCertification.json'
f_in=open(input_filename,'r')
f_out=open(output_filename,'w')
#f_in.next()

def line_parser(l_in):
    if l_in.find("{")!=-1 or l_in.find("}")!=-1:
        print("keep the line the same")
        l_out=l_in
    else:
        l_out=l_in.replace('=',':')
        l_out=l_out.replace(',','+:')
        #if l_out.find("+:")
        #   l_out=l_out.replace(',','+:')
        if l_out.find(":") == -1 or l_out.find("#")!=-1:
            print ("line without semicolon\n")
            l_out="'"+l_out+"'"+":"
            #return(l_out)
        else:
            print("spliting by semicolon")
            l_out=l_out.split(':',1)
            l_out="'" + l_out[0] + "'" + ":" + "'"+l_out[1]+"'"
    return(l_out)

for line in f_in.readline():
    print("printing line input for testing")
    print(line)
    output_tmp=line_parser(line)
    f_out.write(output_tmp)

f_in.close()
f_out.close()
