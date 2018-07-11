#!/usr/bin/env python
import json

#input_filename='TestFile.cfg'
input_filename='BelleCertification.cfg'
intermedian_filename='BelleIntermedian.json'
output_filename="BelleCertification.json"
f_in=open(input_filename,'r')
f_out=open(intermedian_filename,'w')

def line_parser(l_in):
    line_in=l_in.rstrip()
    if line_in.find("{")!=-1 or line_in.find("}")!=-1:
        l_out=line_in.replace(" ","") ##checking point
    else:
        line_in=line_in.strip()
        l_out=line_in.replace('=',':')

        if l_out.find("+:")!=-1:
            l_out=l_out.replace(" ","")
            l_out=l_out.split('+:',1)
            l_out='LIST_TOKEN_DECORATOR,%s' % (l_out[1])
        else:
            if l_out.find(":") == -1:                               #lines without semicolon
                l_out=l_out.replace(" ","")                         ##checking point
                l_out='"%s":' % (l_out)
            elif l_out.find("#")!=-1:                               #lines with the "#"
                if l_out.find("#@@")!=-1:                           #lines with the #@@
                    l_out=l_out.split(" - ",1)
                    l_out='"%s":"%s",' % (l_out[1], l_out[0]) ###CHECK ###
                else:                                               #comments
                    #l_out=''
                    l_out='"comment":"%s",' % (l_out) #This is new for handling comments
            else:                                                   #Line with semicolon
                l_out=l_out.replace(" ","")
                l_out=l_out.split(':',1)
                l_out='"%s":"%s",' % (l_out[0],l_out[1])
    l_out='%s\n' % (l_out)
    return(l_out)

def ListTokenToJson(f_inter,f_final):
    flag=True
    current_line=f_inter.readline().rstrip() #The only line that I will write
    next_line=f_inter.readline().rstrip()
    #counter=0
    f_final.write('{')
    while(flag==True):
        #All if statment follow the cuestion (current_line_token, next_line_token) where true in the condition = Yes
        # (YES,YES)
        if(current_line.find("LIST_TOKEN_DECORATOR")!=-1 and next_line.find("LIST_TOKEN_DECORATOR")!=-1):
            l_out_current='"%s",\n' % (current_line.split(",")[1])
        # (YES,NO)
        elif(current_line.find("LIST_TOKEN_DECORATOR")!=-1 and next_line.find("LIST_TOKEN_DECORATOR")==-1): #trick
            if next_line.find("}")!=-1:
                l_out_current='"%s"]\n' % (current_line.split(",")[1])  #" VMDIRAC"]
            else:
                l_out_current='"%s"],\n' % (current_line.split(",")[1])
        #(NO,YES)
        elif(current_line.find("LIST_TOKEN_DECORATOR")==-1 and next_line.find("LIST_TOKEN_DECORATOR")!=-1):
            l_out_current=current_line.split(":",1)
            l_out_current='%s:[%s\n' % (l_out_current[0],l_out_current[1])
        #(NO,NO)
        elif(current_line.find("LIST_TOKEN_DECORATOR")==-1 and next_line.find("LIST_TOKEN_DECORATOR")==-1):
            #l_out_current='%s\n' % (current_line)
            #print("checkpoint1")
            if next_line.find("}")!=-1: #if the next line is } we never put a commaself.
                l_out_current=current_line.split(",")
                l_out_current='%s\n' % (l_out_current[0])
            elif current_line.find("}")!=-1: # If I find } and next is not } put a comma
                #print("I enter here")
                l_out_current='%s,\n' % (current_line) #put a comma if the next one is a string
            else:
                l_out_current='%s\n' % (current_line) #If the previous conditions did not match then keep the same string
        else:
            print("No conditions match the decision tree, ERROR IN THE LOGIC")
        current_line=next_line
        next_line=f_inter.readline().rstrip()
        f_final.write(l_out_current) #Writing output FileCatalog
        if current_line=="":
            flag=False
    f_final.write('}')
    print("ending_ListTokenToJson")

for line in f_in:
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
