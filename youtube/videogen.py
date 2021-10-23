import requests
from threading import Thread
#import main
#this is for scraping the recent uplods of the given user ids
url="https://www.instagram.com/graphql/query/"


with open(r'.\id.txt',"r") as flk: # make a file with all the user instagram id you want to scrape of
    idks=flk.readlines()

final=[]
dat={}
res=''
querystring=''
def json_out(ide):
    global final,dat
    querystring = {"query_hash":"8c2a529969ee035a5063f2fc8602a0fd","variables":"{\"id\":\""+str(ide)+"\",\"first\":50}"}
    headers = {"cookie": "sessionid=44894681598%3ARhwyJ11URpx6ML%3A24;"}
    res= requests.request("GET", url, params=querystring,headers=headers)
    data=res.json()['data']['user']['edge_owner_to_timeline_media']['edges']
    for m in range(0,len(res.json()['data']['user']['edge_owner_to_timeline_media']['edges'])):
        if data[m]['node']['is_video'] :
            thumnail=data[m]['node']['display_resources'][0]['src']
            video_url=data[m]['node']['video_url']
            data[m]['node']['display_resources'][0]['src']
            try:
                discription=data[m]['node']['edge_media_to_caption']['edges'][0]['node']['text']
            except IndexError: 
                discription="#"+data[m]['node']['owner'][ 'username']+"  New Video"
            dat['url']=video_url
            dat['thumb']=thumnail
            dat['bio']=discription
            dat['of']=data[m]['node']['owner'][ 'username']
            final.append(dat)
            dat={}
            video_url=''
            thumnail=''
            discription=''
        else:
            pass

th_lis=[]
for i in idks:
    t=Thread(target=json_out,args=(i.strip(),))
    th_lis.append(t)
    t.start()



for k in th_lis:
    k.join()

with open(r'.\data.py','w',encoding="utf-8") as fl:
    fl.write("final="+str(final))


import remover
remover.run()
