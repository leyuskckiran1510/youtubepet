import os
from PIL import Image, ImageDraw, ImageFont
from math import ceil, floor
import random


images = []


def dry(i):
    try:
        for j in os.listdir(i):
            if j.split(".")[-1] == "jpg":
                images.append(i + f"\\{j}")
            dry(i + f"\\{j}")
    except:
        pass


print("Starting engine")
for i in os.listdir(r".\youtube"):
    di = f".\\youtube\\{i}"
    dry(di)

print("Colledted files")
print("Suffling")
random.shuffle(images)


def run(images):
    frame_width = 1280
    frame_height = 720
    images_per_row = 9
    padding = 1
    img_width, img_height = Image.open(images[0]).size
    sf = (frame_width - (images_per_row - 1) * padding) / (
        images_per_row * img_width
    )  # scaling factor
    scaled_img_width = ceil(img_width * sf)  # s
    scaled_img_height = ceil(img_height * sf)

    number_of_rows = ceil(len(images) / images_per_row)

    new_im = Image.new("RGB", (frame_width, frame_height))

    i, j = 0, 0
    for num, im in enumerate(images):
        if num % images_per_row == 0:
            i = 0
        im = Image.open(im)
        im.thumbnail((scaled_img_width, scaled_img_height))
        y_cord = (j // images_per_row) * scaled_img_height
        new_im.paste(im, (i, y_cord))
        i = (i + scaled_img_width) + padding
        j += 1
    emoj = Image.open(
        r".\fire.png"
    )  # Emoji or any other png file like your logo or any other sorts
    emoj = emoj.resize((150, 150))
    new_im.paste(emoj, (50, 280), emoj)
    draw = ImageDraw.Draw(new_im)
    font = ImageFont.truetype(".\\SitkaB.ttc", size=170)  # font you want to use
    draw.text(
        (150, 280),
        "Test you want to insert in thumnail",
        font=font,
        fill=(255, 20, 20, 100),
    )  # like XMillion views ..
    new_im.show()
    new_im.save(r".\thumnail.jpg", "JPEG", quality=100, optimize=True, progressive=True)


run(images)
