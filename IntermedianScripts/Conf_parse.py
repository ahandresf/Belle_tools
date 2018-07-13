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
            #print(l_out)
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
    #print(l_out)
    return(l_out)

def ListTok(f_final):
    state="no_token"
    previous_position=0
    flag=True
    counter=int(0)
    while(flag==True):
        counter=counter+1
        if counter==42:
            flag=False
            print("going out of the script")
        current_position=f_final.tell() #It point to the bytes of this position.
        line=f_final.readline()
        print("\ncounter = ",counter)
        print("current_position",current_position)
        print("previous_position",previous_position)
        print("pointer_tell",f_final.tell())
        print("state = ",state)

        #for line in f_final:
        line=line.rstrip()
        #print(line)
        #print("current_position",current_position)
        if(state=="no_token"):
            if line.find("LIST_TOKEN_DECORATOR")!=-1:
                print("I found a token, no_token_before")
                #print("my current position is",f_final.tell())
                l_out_current="'"+line.split(",")[1]+"',\n"
                print("l_out_current", l_out_current)
                f_final.write(l_out_current) #modifying the current line
                print("previous_position",previous_position)
                f_final.seek(previous_position)
                l_out_before=f_final.readline().rstrip().split(":",1)
                #l_out_before=l_out_before.rstrip()
                #l_out_before=l_out_before.split(":")
                l_out_before=l_out_before[0]+": ["+l_out_before[1]+",\n"
                print("l_out_before", l_out_before)
                print("pointer before write",f_final.tell())
                f_final.write(l_out_before) #modifying the previous line
                print("pointer after write",f_final.tell())

                f_final.seek(current_position) #putting back the pointer in the current position.
                print("pointer after seek",f_final.tell())
                state="token" #updating State
            else:
                print("pass_line")

        elif(state=="token"):
            print("find_token with state token")
            if line.find("LIST_TOKEN_DECORATOR")!=-1:
                l_out_current="'"+line.split(",")[1]+"',\n"
                f_final.write(l_out_current) #modifying the current line
            else:
                f_final.seek(previous_position)
                l_out_before=f_final.readline().strip(",\n")+"]"+"\n"
                print(l_out_before)
                state="no_token"
                f_final.seek(current_position)

        #elif(state=="closing_token"):
        #    if line.find("LIST_TOKEN_DECORATOR")!=-1:
        else:
            print("ERROR NO STATE DETECTED")

        previous_position=current_position

for line in f_in:
    #print("printing line input for testing")
    #print(line)
    output_tmp=line_parser(line)
    f_out.write(output_tmp)

f_in.close()
f_out.close()

f_final=open(output_filename,'r+')
ListTok(f_final)
f_final.close()
