#!/home/leasanspy/anaconda3/bin/python
####/usr/bin/python2.7
####/home/leasanspy/anaconda3/bin/python
import pycurl
import json
#from StringIO import StringIO
from io import BytesIO
#with open('myTest_cfg','w') as f:
#buffer = StringIO() #
buffer = BytesIO()
curl_obj = pycurl.Curl()
curl_obj.setopt(curl_obj.URL, 'http://pycurl.io/')
#curl_obj.setopt(pycurl.SSL_VERIFYPEER, 1)
#curl_obj.setopt(pycurl.SSL_VERIFYHOST, 2)
#curl_obj.setopt(pycurl.CAINFO, "~/.globus/usercert.pem")
curl_obj.setopt(curl_obj.WRITEDATA, buffer) #
#curl_obj.setopt(curl_obj.WRITEDATA, f)
curl_obj.perform()
curl_obj.close()
body = buffer.getvalue() #
print(body.decode('iso-8859-1'))
#print(body) #
