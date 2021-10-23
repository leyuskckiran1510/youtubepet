from data import final
import downloder

def run():
    with open('.\\log.txt','r') as fl:
            check=fl.read()

    new_final=[]
    for i in final:
        if i['url'] not in check:
            new_final.append(i)
        else:
            print("Removing Duplicate URL ....\n\t\t[-]  ",i['url'])

    with open(r'.\data.py','w',encoding="utf-8") as fl:
        fl.write("final="+str(new_final))
    downloder.run()
#this is to remove the redundacy of some files 
