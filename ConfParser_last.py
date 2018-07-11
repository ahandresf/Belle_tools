#!/usr/bin/env python
import json
import subprocess
#input_filename='TestFile.cfg'
input_filename='BelleCertification.cfg'
intermedian_filename='BelleIntermedian.json'
output_filename="BelleCertification.json"
#output_filename="Test_BelleCertification.json"
f_in=open(input_filename,'r')
f_out=open(intermedian_filename,'w')

cmd_exc="wc -l < %s" % input_filename
num_lines=subprocess.check_output (cmd_exc,shell=True)
num_lines=int(num_lines)
print("num_lines_input_files: ",num_lines)

def line_parser(l_in):
    line_in=l_in.rstrip()
    if line_in.find("{")!=-1 or line_in.find("}")!=-1:
        ###l_out=line_in ###
        line_out=line_in.strip() #indent_mod
        ind_var=len(line_in)-len(line_out) #indent
        l_out=line_out.replace(" ","") ##checking point
    else:
        line_out=line_in.strip() #indent_mod
        ind_var=len(line_in)-len(line_out) #indent
        l_out=line_out.replace('=',':')
        l_out=l_out.replace('"',"'")
        #l_out=line_in.replace('"',"'") #change double queotes with single ones.

        if l_out.find("+:")!=-1:
            l_out=l_out.replace(" ","")
            l_out=l_out.split('+:',1)
            l_out='LIST_TOKEN_DECORATOR,%s' % (l_out[1])
        else:
            if l_out.find("#")!=-1:                                 #lines with the "#"
                if l_out.find("#@@")!=-1:                           #lines with the #@@
                    if l_out.find('@@-unknown')!=-1:
                        l_out='"No_timestamp":"%s",' % (l_out)
                    else:
                        l_out=l_out.split(" - ",1)
                        l_out='"%s":"%s",' % (l_out[0], l_out[1])
                        ###l_out='"%s":"%s",' % (l_out[1], l_out[0]) ###CHECK ###
                else:                                               #comments
                    #l_out=''
                    l_out='"comment":"%s",' % (l_out) #This is new for handling comments

            elif l_out.find(":") == -1:                             #lines without semicolon
                l_out=l_out.replace(" ","")###                         ##checking point
                l_out='"%s":' % (l_out)

            else:                                                   #Line with semicolon
                l_out=l_out.replace(" ","")###
                l_out=l_out.split(':',1)
                l_out='"%s":"%s",' % (l_out[0],l_out[1])
    if ind_var!=0:
        ind_spacer=" "*ind_var
    else:
        ind_spacer=" "
    l_out='%s%s\n' % (ind_spacer,l_out)
    return(l_out)

def ListTokenToJson(f_inter,f_final):
    flag=True
    current_line=f_inter.readline().rstrip() #The only line that I will write
    next_line=f_inter.readline().rstrip()
    counter=0
    f_final.write('{\n')
    while(flag==True):
        counter=counter+1
        #All if statment follow the cuestion (current_line_token, next_line_token) where true in the condition = Yes
        # (YES,YES)
        if(current_line.find("LIST_TOKEN_DECORATOR")!=-1 and next_line.find("LIST_TOKEN_DECORATOR")!=-1):
            ind_var=len(current_line)-len(current_line.strip()) #indent_mod
            space_var=" "*ind_var
            l_out_current='    %s"%s",\n' % (space_var,current_line.split(",")[1])
        # (YES,NO)
        elif(current_line.find("LIST_TOKEN_DECORATOR")!=-1 and next_line.find("LIST_TOKEN_DECORATOR")==-1): #trick
            ind_var=len(current_line)-len(current_line.strip()) #indent_mod
            space_var=" "*ind_var
            if next_line.find("}")!=-1:
                l_out_current='    %s"%s"]\n' % (space_var,current_line.split(",")[1])  #" VMDIRAC"]
            else:
                l_out_current='    %s"%s"],\n' % (space_var,current_line.split(",")[1])
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
            #elif(current_line=="{") and (next_line=="}"):    #Handle and empty object
                #print("I enter here!!!")
                #l_out_current='%s"object":"empty"' % (current_line)
            elif current_line.find("}")!=-1: # If I find } and next is not } put a comma
                #print("I enter here")
                l_out_current='%s,\n' % (current_line) #put a comma if the next one is a string
            else:
                l_out_current='%s\n' % (current_line) #If the previous conditions did not match then keep the same string

        else:
            print("No conditions match the decision tree, ERROR IN THE LOGIC")
        current_line=next_line
        next_line=f_inter.readline().rstrip()

        #if next_line=="":
        if counter==num_lines:
            l_out_current=l_out_current.replace(',',"") #Last line close with } so it should not have ","
            flag=False

        f_final.write(l_out_current) #Writing output FileCatalog
        #if counter==num_lines:
        #if current_line=="":
            #flag=False
    f_final.write('}\n')
    print("counter: ",counter)
    print("ending_ListTokenToJson")

for line in f_in:
    output_tmp=line_parser(line)
    f_out.write(output_tmp)
#print("intermedian_numlines:",f_out.tell())
f_in.close()
f_out.close()

f_inter=open(intermedian_filename,'r')
f_final=open(output_filename,'w')
ListTokenToJson(f_inter,f_final)
#print("final_tell",f_final.tell())
f_inter.close()
f_final.close()
print("End of the program")
