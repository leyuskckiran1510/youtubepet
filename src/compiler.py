import os
import random
import datetime
import subprocess

FILE_PATHS = []
SELECTED_FILES = []
LOG_DATA = ""
NUMBER_OF_VIDS_TO_COMBINE = 10
MY_PATH = __file__.replace("./", "").replace(".\\", "").replace("compiler.py", "")

pjoin = os.path.join


def load_log():
    with open(pjoin(MY_PATH, "vidlog.txt"), "r") as fl:
        LOG_DATA = fl.read()


def recursive_folder_travel(base_dir):
    if not os.path.isdir(base_dir):
        return
    for child_dir in os.listdir(base_dir):
        _path = pjoin(base_dir, child_dir)
        if os.path.isdir(_path):
            recursive_folder_travel(_path)
        if child_dir.lower().endswith("mp4") and _path not in LOG_DATA:
            FILE_PATHS.append(_path)


def ffmpeg_call(files_txt):
    command = [
        "ffmpeg",
        "-safe",
        "0",
        "-f",
        "concat",
        "-i",
        f"{pjoin(MY_PATH, files_txt)}",
        "-c:v",
        "libx264",
        "-preset",
        "fast",
        "-pix_fmt",
        "yuv420p",
        f"{pjoin(MY_PATH, 'output.mp4')}",
    ]
    process = subprocess.Popen(
        command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )
    _, stderr = process.communicate()
    process.wait()
    with open(pjoin(MY_PATH, "compile.log"), "w") as fl:
        fl.write(str(stderr.decode(encoding="utf-8")))
    print("Read Compile.log to See any errors or problems if exists")


def compile(PATH=MY_PATH):
    for i in os.listdir(PATH):
        fodlers = pjoin(PATH, i)
        recursive_folder_travel(fodlers)

    random.shuffle(FILE_PATHS)
    L = random.choices(FILE_PATHS, k=min(len(FILE_PATHS), NUMBER_OF_VIDS_TO_COMBINE))
    with open(pjoin(MY_PATH, "to_compile.txt"), "w") as fl:
        fl.write("file '")
        fl.write("'\nfile '".join(L))
        fl.write("'\n")

    ffmpeg_call("to_compile.txt")
    with open(pjoin(MY_PATH, "vidlog.txt"), "w") as fl2:
        for i in L:
            fl2.write(i + "\n")
    print("Logging completed")


# recursive_folder_travel("/home/tester/Videos")
# print("\n".join(FILE_PATHS).replace("compiler.py", ""))
compile()
