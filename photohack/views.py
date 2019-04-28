from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import logging
import json
import base64
from . import new
# from new import do_stuff
# from tanya_ideas import get_idiom_for_phrase
from . import tanya_ideas
# import filter_picture
from . import filter_picture
logger = logging.getLogger(__name__)
import base64
from PIL import Image
from io import BytesIO
import os
os.chdir('D:\\Education\\Hackathones\\photohack2\\back\\photohack')

def photo(request):
    return render(request, 'index.html', {})

@csrf_exempt
def process_image(request):
    logger.info(type(request.body))
    jsonka = json.loads(request.body.decode('utf-8')) #.decode('utf-8')
    print("message {}".format(jsonka["message"]))

    response = dict()
    response['img'] = 'AAAA'
    response = json.dumps(response)
    return HttpResponse(response, content_type="application/json")

@csrf_exempt
def return_gif(request):
    
    print(type(request.body.decode('utf-8')))
    jsonka = json.loads(request.body.decode('utf-8'))
    print("message {}".format(jsonka["message"]))

    # imgdata = base64.b64decode(jsonka['img'])
    filename = 'imagege.jpg'  # I assume you have a way of picking unique filenames
    with open(filename, 'wb') as f:
        f.write(base64.decodebytes(jsonka['img'].encode('utf-8')))
    print('saved')
    url = os.path.join(os.getcwd(), 'imagege.jpg')
    # url = 'D:\\Education\\Hackathones\\photohack2\\back\\photohack\\imagege.jpg'

    # with open('D:\\Education\\Hackathones\\photohack2\\back\\photohack\\uiuiui.jpg', 'rb') as file:
    #     encoded_string = base64.b64encode(file.read())

    # вызов функций

    filter_picture.dodododo(tanya_ideas.get_idiom_for_phrase(jsonka["message"]), url)
    #
    input_file = 'final.jpg'
    with open(input_file, 'rb') as f:
        # image = f.read()
        encoded_string = base64.b64encode(f.read())
    
    response = dict()
    # response['image'] = str(encoded_string.decode("utf-8") )
    response['image'] = encoded_string.decode("utf-8")
    response = json.dumps(response)
    return HttpResponse(response, content_type="application/json")