from PIL import Image, ImageFont, ImageDraw
import json
import uuid
import os

def short(string):
    if len(string)>16:
        string = string[: 12]
        string = string + '...'
    return string

def draw(semple, text):
    text = short(text)
    file = os.path.join('samples', semple + '.json')
    f = open(file, 'r')
    json_f = f.read()
    f.close()

    json_f = json.loads(json_f)

    file = os.path.join('ttf', json_f['font'])

    font = ImageFont.truetype(file , json_f['size_text'])

    file = os.path.join('samples', semple + ".png")

    im1=Image.open(file)

    # Drawing the text on the picture
    draw = ImageDraw.Draw(im1)
    draw.text((json_f['x'], json_f['y']), text, (0,0,0), font=font)

    # Save the image with a new name
    uid_now = uuid.uuid4()
    file = os.path.join('result', str(uid_now) + '.png')
    im1.save(file)

    img_uid_now = file
    return str(uid_now)