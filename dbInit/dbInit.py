import os
import re
import csv
import json
import requests
from replaceall import replaceall
import os
import glob
from review import review, review_source
import web_parse

def post(reviews_list):
    url = 'http://localhost:58844/api/review/'

    pattern = r'(\\x[0-9,a-f]{2})'

    for it in reviews_list:
        first = replaceall(str(json.loads(json.dumps(it,default=lambda o: o.__dict__, indent=4))),'\"','\\"')
    
        second = replaceall(first, '\'',r'"')
        st = re.sub(pattern,' ',second)

        print(it.text)
        #print(st)
        resp = requests.post(url, headers = {'Content-Type':'application/json'}, data=st.encode('utf-8'))
        print("Resp: %s" % resp)


#tuple = web_parse.parse_web_irec()

#reviews_list = tuple[0]
#texts = tuple[1]

#s = review_source()
#s.name = "irecommend.ru"
#s.url = 'https://irecommend.ru/content/rzhd'
from io import StringIO
io = StringIO()
reviews_list = ["sfhdiugfjdigjf", "dfuyegrhowisjne", "dbufhgjdiopfl"]
str = json.dumps(reviews_list)

#post(reviews_list)


    

