# from new import do_stuff
# https://curl.trillworks.com/
from . import new

# print(do_stuff(content_filename2,template_id))
# print('Done')



from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import requests


def dodododo(aforism, jpeg):

    content_filename2 = jpeg
    template_id = '10000277'

    item=new.do_stuff(content_filename2,template_id)
    frames=[]
    the_aphorism=aforism
    the_img = Image.open(requests.get(item, stream=True).raw)
    draw = ImageDraw.Draw(the_img)


    font = ImageFont.truetype("Roboto-Medium.ttf", 24)
    print("h")
    draw.text((150, 550), the_aphorism, (0, 0, 0), font=font)

    # base64
    the_img.save('final.jpg')