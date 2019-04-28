# from client_photolab import ClientPhotolab

# import client_photolab
from . import client_photolab

def do_stuff(content_filename,combo_id):
    resourses_filename = 'resources.zip'


    api = client_photolab.ClientPhotolab()


    content_url = api.image_upload(content_filename)
    print('content_url: {}'.format(content_url))

    template_name = api.template_upload(resourses_filename)
    print('template_name: {}'.format(template_name))

    result_url = api.template_process(template_name, [{
        'url' : content_url,
        'rotate' : 0,
        'flip' : 0,
        'crop' : '0,0,1,1'
    }])
    print('result_url: {}'.format(result_url))
    result_url = api.template_process(template_name, [{
        'url' : content_url
    }])
    print('result_url: {}'.format(result_url))

    print('')
    print('start process combo_id: {}'.format(combo_id))
    i = 0
    template_name=combo_id
    result_url = api.photolab_process(str(template_name), [{
        'url' : content_url,
        'rotate' : 0,
        'flip' : 0,
        'crop' : '0,0,1,1'
    }])
    i = i + 1
    if i != 0:
        content_url = result_url
        # print('for template_name: {}, result_url: {}'.format(template_name, result_url))

    print('result_url: {}'.format(result_url))

    return result_url