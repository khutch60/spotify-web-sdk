from inky.auto import auto
from PIL import Image, ImageDraw, ImageFont
import requests
from io import BytesIO


def update_screen(data):
    width, height = (600, 448)
    
    image = requests.get(data['img'])
    artist = data['artist']
    if len(artist) >= 17:
        artist = artist[:17] + '...' 
    album = data['album']  
    if len(album) >= 29:
        album = album[:29] + '...' 
      
    album_img = Image.open(BytesIO(image.content)).convert("RGBA")
    album_img = album_img.rotate(90)
    album_img = album_img.resize((height, height))   
    
    background = Image.new("RGB", (width, height), "#212121")
    background.paste(album_img, (0,0, height, height), mask = album_img)
    text_image = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(text_image)   
    
    fnt_1 = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 25)
    fnt_2 = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 40)
    
    draw.text((100, 350), album, font=fnt_1, fill=(255, 255, 255, 255))
    draw.text((100, 400), artist, font=fnt_2, fill=(255, 255, 255, 255))
    
    rotated_text_image = text_image.rotate(90, expand=True, fillcolor="#212121") 

    rot_width, rot_height = rotated_text_image.size
    center_x = (width - rot_width) // 2
    center_y = (height - rot_height) // 2

    background.paste(rotated_text_image, (center_x + 50, center_y), mask=rotated_text_image)

    display = auto()

    display.set_image(background)
    try:
        display.show()
    except SystemExit:
        pass

