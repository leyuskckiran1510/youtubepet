import os
import json
import random
import requests
from multiprocessing import Pool
from threading import Thread
import compiler

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

    THUMBNAIL_PATH = pjoin(_thumnailpath, f"{of}{_ct}.jpg")
    with open(THUMBNAIL_PATH, "wb") as fl:
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

        choosed = random.choices(data_list, k=min(len(data_list) - 1, NOFVTDFEU))
        threads = []
        for i in choosed:
            if check_dups(i["of"], i["url"]):
                print("Not contnidawds")
                continue
            thread = Thread(
                target=down,
                args=(i["url"], i["thumb"], i["of"]),
            )
            thread.start()
            threads.append(thread)

        for thread in threads:
            thread.join()


def start():
    process_list = []
    with open("data.json", "r") as fl:
        TO_DOWNLOAD = json.load(fl)
    if len(TO_DOWNLOAD) == 0:
        exit()
    pool = Pool(processes=len(TO_DOWNLOAD))

    for i in TO_DOWNLOAD:
        process = pool.apply_async(prep, args=(i, TO_DOWNLOAD[i]))
        process_list.append(process)

    for process in process_list:
        process.get()

    pool.close()
    pool.join()
    compiler.compile(pjoin(C_dir, "youtube"))


if __name__ == "__main__":
    start()
