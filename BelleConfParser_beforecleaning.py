#!/usr/bin/env python
import json

input_filename='TestFile.cfg'
#input_filename='BelleCertification.cfg'
intermedian_filename='BelleIntermedian.json'
output_filename="BelleCertification.json"
f_in=open(input_filename,'r')
f_out=open(intermedian_filename,'w')
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
            #print(l_out)
            l_out='LIST_TOKEN_DECORATOR,%s' % (l_out[1])
            #l_out="LIST_TOKEN_DECORATOR"+","+l_out[1]
        else:
            if l_out.find(":") == -1: #lines without semicolon
                l_out='"%s":' % (l_out)
                #l_out="'"+l_out+"'"+":"
            elif l_out.find("#")!=-1: #lines with the "#"
                l_out=l_out.split(" - ",1)
                l_out='"%s":"%s"' % (l_out[1], l_out[0]) ###CHECK
                #l_out="'"+l_out[0]+"'"+":"+"'"+l_out[1]+"'"
            else:
                #print("spliting by semicolon")
                l_out=l_out.replace(" ","")
                l_out=l_out.split(':',1)
                l_out='"%s":"%s"' % (l_out[0],l_out[1])
                #l_out="'" + l_out[0] + "'" + ":" + "'"+l_out[1]+"'"
    l_out='%s\n' % (l_out)
    #l_out=l_out+"\n"
    #print(l_out)
    return(l_out)

def ListTokenToJson(f_inter,f_final):
    flag=True
    current_line=f_inter.readline().rstrip() #The only line that I will write
    next_line=f_inter.readline().rstrip()
    counter=0

    while(flag==True):
        #All if statment follow the cuestion (current_line_token, next_line_token) where true in the condition = Yes
        # (YES,YES)
        if(current_line.find("LIST_TOKEN_DECORATOR")!=-1 and next_line.find("LIST_TOKEN_DECORATOR")!=-1):
            l_out_current='"%s",\n' % (current_line.split(",")[1])
            #l_out_current="'"+current_line.split(",")[1]+"',\n"
        # (YES,NO)
        elif(current_line.find("LIST_TOKEN_DECORATOR")!=-1 and next_line.find("LIST_TOKEN_DECORATOR")==-1):
            l_out_current='"%s"]\n' % (current_line.split(",")[1])
            #l_out_current="'"+current_line.split(",")[1]+"']\n"
        #(NO,YES)
        elif(current_line.find("LIST_TOKEN_DECORATOR")==-1 and next_line.find("LIST_TOKEN_DECORATOR")!=-1):
            l_out_current=current_line.split(":",1)
            #print(l_out_current)
            l_out_current='%s:[%s,\n' % (l_out_current[0],l_out_current[1])
            #l_out_current=l_out_current[0]+":"+"["+l_out_current[1]+",\n"
        #(NO,NO)
        elif(current_line.find("LIST_TOKEN_DECORATOR")==-1 and next_line.find("LIST_TOKEN_DECORATOR")==-1):
            l_out_current='%s\n' % (current_line)
            #l_out_current=current_line+"\n"
        else:
            print("No conditions match the decision tree, ERROR IN THE LOGIC")

        f_final.write(l_out_current) #Writing output FileCatalog
        current_line=next_line
        next_line=f_inter.readline().rstrip()

        if current_line=="":
            flag=False
    print("ending_ListTokenToJson")

for line in f_in:
    #print("printing line input for testing")
    #print(line)
    output_tmp=line_parser(line)
    f_out.write(output_tmp)

f_in.close()
f_out.close()

f_inter=open(intermedian_filename,'r')
f_final=open(output_filename,'w')
ListTokenToJson(f_inter,f_final)
f_inter.close()
f_final.close()
print("End of the program")
