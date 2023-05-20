import os
import datetime
from googleauth import Create_Service
from googleapiclient.http import MediaFileUpload


def run():
    try:
        CLIENT_SECRET_FILE = "client_secret.json"
        API_NAME = "youtube"
        API_VERSION = "v3"
        SCOPES = ["https://www.googleapis.com/auth/youtube.upload"]
        YEAR = datetime.datetime.now().year
        MONTH = str(datetime.datetime.now().month).zfill(2)
        DAY = str(datetime.datetime.now().day).zfill(2)
        VIDEO_FILE = f"/home/tester/Videos/TimeLapse/{YEAR}/{MONTH}/{DAY}/output.mp4"

        service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)
        # upload_date_time = datetime.datetime.now().isoformat() + ".000Z"
        request_body = {
            "snippet": {
                "categoryI": 19,
                "title": "",
                "description": "",
                "tags": [
                    "",
                    "",
                    "",
                    "",
                    "",
                ],
            },
            "status": {
                "privacyStatus": "unlisted",
                "madeForKids": False,
                "selfDeclaredMadeForKids": False,
            },
            "notifySubscribers": False,
        }

        mediaFile = MediaFileUpload("output.mp4")

        response_upload = (
            service.videos().insert(part="snippet,status", body=request_body, media_body=mediaFile).execute()
        )

        service.thumbnails().set(
            videoId=response_upload.get("id"),
            media_body=MediaFileUpload("thumnail.jpg"),
        ).execute()
    except Exception as e:
        print("Actual Error \n\t[+] ", e)


if __name__ == "__main__":
    run()
