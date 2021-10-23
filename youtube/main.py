import datetime
from Google import Create_Service
from googleapiclient.http import MediaFileUpload

def run():
    try:
        CLIENT_SECRET_FILE = r'.\client_secret.json'#download this from goole dev console Youtube data Api 3 part
        API_NAME = 'youtube'
        API_VERSION = 'v3'
        SCOPES = ['https://www.googleapis.com/auth/youtube.upload']
        
        service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)
        upload_date_time = datetime.datetime(2020, 12, 25, 12, 30, 0).isoformat() + '.000Z'

        request_body = {
            'snippet': {
                'categoryI': 19,#and number betwen 0-25 it describes which category like 19 means travell and blogs i think
                                        #you can google it
                'title': '',#video title
                'description': '', #Video discription
                'tags': ['','','','','',]#Put your tags of videos here
            },
            'status': {
                'privacyStatus': 'private',
                'publishAt': upload_date_time,#if you want to upload now and make it public after some time
                'selfDeclaredMadeForKids': False, 
            },
            'notifySubscribers': False
        }

        mediaFile = MediaFileUpload(r".\output.MP4")

        response_upload = service.videos().insert(
            part='snippet,status',
            body=request_body,
            media_body=mediaFile
        ).execute()

        service.thumbnails().set(                                                       #this is for setting video Title
                                                                                                    #you can get more details in google api python section
            videoId=response_upload.get('id'),
            media_body=MediaFileUpload(r".\thumnail.jpg")
        ).execute()
    except Exception as e:
        print("[*]Most probably your quota is expired change the youtbe api plan or add credit card to get extra quotas ")
        print("Actual Error \n\t[+] ",e)
        
if __name__=="__main__":
    run()
