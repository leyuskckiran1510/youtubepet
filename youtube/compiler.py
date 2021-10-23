from moviepy.editor import * #this import also takes long time if you don't have that good specs
import os
import random


'''

This is the longest process of all it takes longer accoring to the number of files you are going to compile
One two or 10 20 your choice




'''
L =[]
fin=[]
def dry(i):
    global di
    try:
        for j in os.listdir(i):
            if j.split(".")[-1] =="mp4":
                L.append(i+f"\\{j}")
                print("\r",i+f"\\{j}",)
            dry(i+f"\\{j}")
    except:
        pass

for i in os.listdir(r".\\"):
    di=f".\\{i}"
    dry(di)
exit()
with open(r".\vidlog.txt","r") as fl:
    vidlog=fl.read()
fake=[]
for i in L:
    if i not in vidlog:
        fake.append(i)
    else:
        continue
L=fake    
random.shuffle(L)

#L=random.choices(L,k=50)   #Uncomment this and replace the value of k with any other number
                                                 # the number denotes the number of videos files to combine   

for i in L:
    video=VideoFileClip(i)
    fin.append(video)

    
print("\rFile Collected",end='')
print("\rPreperaing to compile",end='')
final_clip = concatenate_videoclips(fin)
final_clip.to_videofile(r".\output.mp4", fps=60, remove_temp=False)#output file
print("Complied")

print("Logging the video file names to prevent repetetion later on next time")
with open(r".\vidlog.txt","w") as fl2:
    for i in L:
        fl2.write(i+"\n")
print("Logging completed")
