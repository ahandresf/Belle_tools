#!/usr/bin/env python
import json

#input_filename="Test_BelleCertification.json"
input_filename='BelleCertification.json'
output_filename="Belle_noc.json"
f_in=open(input_filename,'r')
f_out=open(output_filename,'w')

def comment_deleter(f_in,f_out):
    counter_lines=0
    counter_comment=0
    for line in f_in:
        if line.find("#")!=-1:       #lines with the "#"
            counter_comment=counter_comment+1;
        else:
            if line.find("AccessProtocol.1")!=-1:
                line=line.replace("AccessProtocol.1","AccessProtocol_1") #this is going to be a dictionary key and the dot cause problems
            if line.find("AccessProtocol.0")!=-1:
                line=line.replace("AccessProtocol.0","AccessProtocol_0") #this is going to be a dictionary key and the dot cause problems
            if line.find("AccessProtocol.davs")!=-1:
                line=line.replace("AccessProtocol.davs","AccessProtocol_davs")
            if line.find("AccessProtocol.https")!=-1:
                line=line.replace("AccessProtocol.https","AccessProtocol_https") #this is going to be a dictionary key and the dot cause problems
            counter_lines=counter_lines+1
            f_out.write(line)

    return(str(counter_comment),str(counter_lines))

(counter_comment,counter_lines)=comment_deleter(f_in,f_out)

print("the file have %s comments" % (counter_comment))
print ("the output file have %s lines" % (counter_lines))

f_in.close()
f_out.close()
print("End of the program")
