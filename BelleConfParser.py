#!/usr/bin/env python
import json

input_filename='TestFile.cfg'
#input_filename='BelleCertification.cfg'
output_filename='BelleCertification.json'
f_in=open(input_filename,'r')
f_out=open(output_filename,'w+')
#f_in.next()

def line_parser(l_in):
    line_in=l_in.rstrip()
    if line_in.find("{")!=-1 or line_in.find("}")!=-1:
        l_out=line_in
        #l_out=l_in
        #print("keep the line the same")
    else:
        line_in=line_in.strip()
        l_out=line_in.replace('=',':')

        if l_out.find("+:")!=-1:
            #l_out=l_out.replace('+:',',')
            l_out=l_out.replace(" ","")
            l_out=l_out.split('+:',1)
            print(l_out)
            l_out="LIST_TOKEN_DECORATOR"+","+l_out[1]
        else:
            if l_out.find(":") == -1 or l_out.find("#")!=-1:
                #print ("line without semicolon\n")
                l_out="'"+l_out+"'"+":"
                #return(l_out)
            else:
                #print("spliting by semicolon")
                l_out=l_out.replace(" ","")
                l_out=l_out.split(':',1)
                l_out="'" + l_out[0] + "'" + ":" + "'"+l_out[1]+"'"
    l_out=l_out+"\n"
    print(l_out)
    return(l_out)

def list_parser():
    pass


for line in f_in:
    #print("printing line input for testing")
    #print(line)
    output_tmp=line_parser(line)
    f_out.write(output_tmp)

f_in.close()
f_out.close()
