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
import json
import neural
from types import SimpleNamespace

def post(reviews_list):
    url = 'http://localhost:60026/api/review/'

    pattern = r'(\\x[0-9,a-f]{2})'

    for it in reviews_list:
        first = replaceall(str(json.loads(json.dumps(it,default=lambda o: o.__dict__, indent=4))),'\"','\\"')
    
        second = replaceall(first, '\'',r'"')
        st = re.sub(pattern,' ',second)

        print(it.text)
        
        resp = requests.post(url, headers = {'Content-Type':'application/json'}, data=st.encode('utf-8'))
        print("Resp: %s" % resp)


tuple = web_parse.parse_web_irec()

print("\n\nWeb's been parsed")

reviews_list = tuple[0]
texts = tuple[1]

#s = review_source()
#s.name = "irecommend.ru"
#s.url = 'https://irecommend.ru/content/rzhd'
str = json.dumps(texts)

#marks_list = json.loads(str, object_hook=lambda d: SimpleNamespace(**d))

marks_list = neural.predict(texts)

for it in range(0, len(marks_list)):
    reviews_list[it].sence = marks_list[it]

post(reviews_list)


    

