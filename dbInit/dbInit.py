import os
import re
import csv
import json
import requests
from replaceall import replaceall
import os
import glob
from review import review, review_source
import alg

def get_link(sPart: str):
    fPart = 'https://irecommend.ru'
    s_ind = sPart.index(':') + 1
    sPart = sPart[s_ind:-1]
    return fPart + sPart

folder_path = r'C:\Users\User\Downloads\TestEx\TestEx'
links_path = r'C:\Users\User\Downloads\TestEx\links.txt'

s = review_source()
s.name = "irecommend.ru"
s.url = 'https://irecommend.ru/content/rzhd'

positive = "positive-"
neutral = "neutral-"
negative = "negative-"

negNum = 0
neutNum = 0
posNum = 0

marks = []
markfile = open(r'C:\Users\User\Downloads\check_2.txt', encoding='utf-8')
for line in markfile.readlines():
    if line.find(positive) != -1:
        posNum = float(line[len(positive):])
    if line.find(neutral) != -1:
        neutNum = float(line[len(neutral):])
    if line.find(negative) != -1:
        negNum = float(line[len(negative):])
        marks.append(alg.formula_fedosa(posNum, neutNum, negNum))
reviews = []

num = 0
linksfile = open(links_path, encoding='utf-8')
all_links = linksfile.readlines()
link_num = 0
for filename in glob.glob(os.path.join(folder_path, '*.txt')):
    with open(filename, 'r', encoding='utf8') as f:
        r = review()
        r.text = f.read()
        r.source = 1
        if len(r.text) > 10:
            print("Num: %d. Text: %s" % (num,r.text))
            r.sence = marks[num]
            reviews.append(r)
            num = num + 1
            r.url = get_link(all_links[link_num])
    link_num = link_num + 1

print(len(marks))

url = 'http://localhost:58844/api/review/'

pattern = r'(\\x[0-9,a-f]{2})'

for it in reviews:
    first = replaceall(str(json.loads(json.dumps(it,default=lambda o: o.__dict__, indent=4))),'\"','\\"')
    
    second = replaceall(first, '\'',r'"')
    st = re.sub(pattern,' ',second)

    print(it.text)
    #print(st)
    resp = requests.post(url, headers = {'Content-Type':'application/json'}, data=st.encode('utf-8'))
    print("Resp: %s" % resp)
    

