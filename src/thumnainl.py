from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance
from math import ceil
import random


WIDTH, HEIGHT = 1280, 720


def enhance(image: Image):
    blurred_image = image.filter(ImageFilter.GaussianBlur(radius=0.5))
    enhancer = ImageEnhance.Brightness(blurred_image)
    adjusted_image = enhancer.enhance(1.5)
    return adjusted_image


def add_tl(image: Image, text: str, logo_path: str):
    image = enhance(image)
    if logo_path:
        logog = Image.open("fire.png")
        logog = logog.resize((75, 75))
        image.paste(logog, (50, 280), logog)
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(
        "font.ttf",
        size=int((WIDTH / (len(Image_Text) * 4)) * 7),
    )
    draw.text(
        (WIDTH / 2, HEIGHT / 2),
        Image_Text,
        font=font,
        fill=(255, 100, 100, 100),
        anchor="ms",
        stroke_width=int((WIDTH / HEIGHT) / len(Image_Text)) + 1,
    )


def generate_collage(images):
    Image_Text = "Compilation"
    num_images = len(images)
    rows = int(num_images**0.5)
    cols = int((num_images + rows - 1) / rows)

    num_grids = rows * cols
    if num_grids > num_images:
        diff = num_grids - num_images

        images = random.sample(images, num_images - diff)
        num_images = len(images)
        rows = int(num_images**0.5)
        cols = int((num_images + rows - 1) / rows)

    canvas_width = cols * WIDTH
    canvas_height = rows * HEIGHT
    tile_width = canvas_width // cols
    tile_height = canvas_height // rows

    canvas = Image.new("RGB", (canvas_width, canvas_height), (0, 0, 0))

    for i, image_path in enumerate(images):
        image = Image.open(image_path)

        image = image.resize((tile_width, tile_height), Image.Resampling.LANCZOS)

        row = i // cols
        col = i % cols
        x = col * tile_width
        y = row * tile_height

        canvas.paste(image, (x, y))

    bbox = canvas.getbbox()
    canvas = canvas.crop(bbox)

    canvas = canvas.resize((WIDTH, HEIGHT), Image.Resampling.LANCZOS)
    add_tl(canvas, Image_Text, "fire.png")
    canvas.show()
    canvas.save("thumbnails.jpg", "JPEG", quality=100, optimize=True, progressive=True)


images = [
    "/home/tester/Pictures/wallpaper/wallhaven-zxleqw.png",
    "/home/tester/Pictures/wallpaper/wallpaper1.png",
    "/home/tester/Pictures/wallpaper/wallpaper2.jpg",
    "/home/tester/Pictures/wallpaper/wallpaper3.png",
    "/home/tester/Pictures/wallpaper/wallpaper4.png",
    "/home/tester/Pictures/wallpaper/wallpaper5.png",
    "/home/tester/Pictures/wallpaper/wallpaper6.png",
    "/home/tester/Pictures/wallpaper/wallpaper7.png",
    "/home/tester/Pictures/wallpaper/wallpaper8.png",
    "/home/tester/Pictures/wallpaper/wallpaper9.jpg",
    "/home/tester/Pictures/wallpaper/wallpaper.png",
    "/home/tester/Pictures/wallpaper/wallpaperQW.png",
    "/home/tester/Pictures/wallpaper/wallpaper_the_copy.png",
]
images += images
images += images

random.shuffle(images)


generate_collage(images)
