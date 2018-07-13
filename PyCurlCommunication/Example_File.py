#!/home/leasanspy/anaconda3/bin/python
#This is using python3
import pycurl
import json
#from io import BytesIO
with open('myTest_cfg','wb') as f:
    #buffer = BytesIO()
    curl_obj = pycurl.Curl()
    curl_obj.setopt(curl_obj.URL, 'http://pycurl.io/')
    #curl_obj.setopt(pycurl.SSL_VERIFYPEER, 1)
    #curl_obj.setopt(pycurl.SSL_VERIFYHOST, 2)
    #curl_obj.setopt(pycurl.CAINFO, "~/.globus/usercert.pem")
    #curl_obj.setopt(curl_obj.WRITEDATA, buffer) #
    curl_obj.setopt(curl_obj.WRITEDATA, f)
    curl_obj.perform()
    curl_obj.close()
    #body = buffer.getvalue() #
    #print(body.decode('iso-8859-1'))
    #print(body) #
