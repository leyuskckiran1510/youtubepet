import json
import requests
from threading import Thread, Lock


VAR_LOCK = Lock()
DATA_DIC = {}


def json_out(ide):
    global DATA_DIC
    GRAPHQL_URL = "https://www.instagram.com/graphql/query/"
    QUERY = {
        "query_hash": "8c2a529969ee035a5063f2fc8602a0fd",
        "variables": '{"id":"' + str(ide) + '","first":50}',
    }
    HEADERS = {
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "en-US,en;q=0.8",
        "Connection": "keep-alive",
        "Content-Length": "0",
        "Referer": "https://www.instagram.com/",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36",
        "sessionid": "",
        "mid": "",
        "ig_pr": "1",
        "ig_vw": "1920",
        "csrftoken": "",
        "s_network": "",
        "ds_user_id": "",
        "x-ig-app-id": "936619743392459",
    }
    # {
    #     "x-ig-app-id": "936619743392459",
    # }

    res = requests.request("GET", GRAPHQL_URL, params=QUERY, headers=HEADERS)
    DIC = (
        res.json()
        .get("data", {})
        .get("user", {})
        .get("edge_owner_to_timeline_media", {})
        .get("edges", None)
    )
    if not DIC:
        print(res.json())
        return
    data = DIC
    for m in range(0, len(DIC)):
        if data[m]["node"]["is_video"]:
            dat = {}
            # delete
            with open("analyze.json", "a") as fl:
                fl.write(json.dumps(data, indent=6))
            # end
            dat["url"] = data[m]["node"]["video_url"]
            dat["thumb"] = data[m]["node"]["display_resources"][0]["src"]
            dat["of"] = data[m]["node"]["owner"]["username"]
            dat["bio"] = data[m]["node"]["edge_media_to_caption"].get(
                "edges", [{"node": {"text": f"#{dat['of']}'s  New Video!!"}}]
            )[0]["node"]["text"]
            VAR_LOCK.acquire()
            DATA_DIC[dat["of"]] = DATA_DIC.get(dat["of"], []) + [dat]
            VAR_LOCK.release()


def download_module(version: int = 0):
    if version == 0:
        import downloder

        downloder.start()
    elif version == 2:
        import downloder_2

        downloder_v2.start()
    elif version == 3:
        import downloder_3

        downloder_v3.start()
    else:
        print("Defaulting to slowest download method/moduel")
        import downloder

        downloder.start()


def main():
    with open("id.txt", "r") as flk:
        ids = flk.read().split("\n")
    threads = []
    for i in ids:
        t = Thread(target=json_out, args=(i.strip(),))
        threads.append(t)
        t.start()

    for k in threads:
        k.join()

    with open("data.json", "w") as fl:
        fl.write(json.dumps(DATA_DIC, indent=4))

    download_module(0)


if __name__ == "__main__":
    main()
