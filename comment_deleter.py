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
            f_out.write(line)
            counter_lines=counter_lines+1
    return(str(counter_comment),str(counter_lines))

(counter_comment,counter_lines)=comment_deleter(f_in,f_out)

print("the file have %s comments" % (counter_comment))
print ("the output file have %s lines" % (counter_lines))

f_in.close()
f_out.close()
print("End of the program")
