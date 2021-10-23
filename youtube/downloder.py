from data import final
from threading import Thread
import requests
import os
import random



def down(url,thm,of):
    res=requests.get(url)
    if of not in os.listdir('.\\youtube\\'):
        os.mkdir('.\\youtube\\'+of)
    if 'video' not in os.listdir('.\\youtube\\'+of):
        os.mkdir('.\\youtube\\'+of+'\\video')
        os.mkdir('.\\youtube\\'+of+'\\thumb')
    name='video\\'+of+str((str(os.listdir('.\\youtube\\'+of+'\\video')).casefold().count(of))+1)+".mp4"
    with open('.\\youtube\\'+of+'\\'+name,'wb') as fl:
        fl.write(res.content)
    res=requests.get(thm)
    name='thumb\\'+of+str((str(os.listdir('.\\youtube\\'+of+'\\thumb')).casefold().count(of))+1)+".jpg"
    with open('.\\youtube\\'+of+'\\'+name,'wb') as fl:
        fl.write(res.content)
    print("Downloaded")

def run():
    global final
    thr=[]
    final=random.choices(final,k=30)#you can change the 30 to any given number as it is the number of videos to be downloded from
                                                        #from the scraped list of urls
    with open('.\\youtube\\log.txt','a') as fl:
        for i in final:
            a=Thread(target=down,args=(i['url'],i['thumb'],i['of'],))
            a.start()
            thr.append(a)
            fl.write(i['url']+"\n")       

    for i in thr:
        print("Joining Thread ,  ",i)
        i.join()

    
    
if __name__=="__main__":
    run()


