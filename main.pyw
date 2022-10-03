import ctypes
from PIL import Image, ImageFont, ImageDraw
import os
import datetime

text = datetime.datetime.now().strftime("%A %d %B, %Y")

my_image = Image.open("wallpaper_base.tif")

image_editable = ImageDraw.Draw(my_image)
image_editable.text((1890 * 2, 1050 * 2), text, (255, 255, 255), font=ImageFont.truetype('font.ttf', 100), anchor="rb")

my_image.save("wallpaper.png")
ctypes.windll.user32.SystemParametersInfoW(20, 0, os.getcwd() + "\\wallpaper.png", 3)
