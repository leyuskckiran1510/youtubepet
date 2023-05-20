import os
import json
import random
import requests
from threading import Thread

pjoin = os.path.join
C_dir = os.getcwd()
NOFVTDFEU = 30  # NUMBER_OF_VIDS_TO_DOWNLOAD_FROM_EACH_USER


class DownloadReturn:
    def __init__(self, url: str, stat: bool):
        self.url = url
        self.stat = stat


def down(url, thm, of):
    res = requests.get(url)

    if not res.status_code == 200:
        return DownloadReturn(url, False)

    _videopath = pjoin(C_dir, "youtube", of, "video")
    _thumnailpath = pjoin(C_dir, "youtube", of, "thumb")
    os.makedirs(_videopath, exist_ok=True)
    os.makedirs(_thumnailpath, exist_ok=True)

    _ct = str(len(os.listdir(_videopath)) + 1)
    VIDEO_PATH = pjoin(_videopath, f"{of}{_ct}.mp4")
    with open(VIDEO_PATH, "wb") as fl:
        fl.write(res.content)

    res = requests.get(thm)
    if not res.status_code == 200:
        return DownloadReturn(thm, False)

    THUMNAIL_PATH = pjoin(_thumnailpath, f"{of}{_ct}.jpg")
    with open(THUMNAIL_PATH, "wb") as fl:
        fl.write(res.content)

    return DownloadReturn(url, True)


def prep(of: str, data_list: list) -> None:
    os.makedirs(pjoin(C_dir, "youtube", of), exist_ok=True)
    if not os.path.exists(pjoin(C_dir, "youtube", of, "log.txt")):
        with open(pjoin(C_dir, "youtube", of, "log.txt"), "w") as fl:
            fl.write("")
    with open(pjoin(C_dir, "youtube", of, "log.txt"), "a+") as fl:

        def check_dups(of, url):
            fl.seek(0)
            return url.split("?")[0] in fl.read().split("\n")

        choosed = random.choices(data_list, k=NOFVTDFEU)
        for i in choosed:
            if check_dups(i["of"], i["url"]):
                print("Not contnidawds")
                continue
            res = down(i["url"], i["thm"], i["of"])
            fl.write(i["url"].split("?")[0] + "\n")
            fl.flush()


def start():
    thread_list = []
    with open("data.json", "r") as fl:
        TO_DOWNLOAD = json.load(fl)

    for i in TO_DOWNLOAD:
        thread = Thread(
            target=prep,
            args=(
                i,
                TO_DOWNLOAD[i],
            ),
        )
        thread.start()
        thread_list.append(thread)

    for i in thread_list:
        i.join()


if __name__ == "__main__":
    start()