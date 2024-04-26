import json
import base64 
import cv2
import numpy as np
import req_tencent_api

def data_uri_to_cv2_img(uri): 
    encoded_data = uri.split(',')[1]  # iVBORw0KG...
    nparr = np.fromstring(base64.b64decode(encoded_data), np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    return img

def do_gray(request):
    fp_grayed = './static/after/grayed.png'
    route_grayed = '/after/grayed.png'
    res = {}

    try:
        json_dict = request.get_json()
        img_uri = json_dict['content'] # data:image/png;base64,iVBORw0KG...
        img = data_uri_to_cv2_img(img_uri)

        # img_base64_string = img_uri_str.split(',')[1] # iVBORw0KG...
        # img_data = base64.b64decode(img_base64_string)
        # print(json_dict)
        # with open("tmp.png", "wb") as f:
        #     f.write(img_data)
        
        # img = cv2.imread('filename.png')
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        cv2.imwrite(fp_grayed, img_gray) 

        res = {
            'status':'OK',
            'msg':'Success',
            'route_grayed':route_grayed,
        }

    except Exception as e:
        print("Error occured: " + str(e))
        res = {
            'status':'ERROR',
            'msg': str(e),
        }

    return json.dumps(res ,indent=4, sort_keys=True)




    # JSON_sent = request.get_json()
    # print(JSON_sent)
    # print(request.__dict__)
    # print(json.dumps(request.__dict__,indent=4, sort_keys=True))
    # return json.dumps(request.__dict__,indent=4, sort_keys=True)
    return '111'


def do_ocr(request):
    # fp_grayed = './static/after/grayed.png'
    # route_grayed = './after/grayed.png'
    res = {}

    try:
        json_dict = request.get_json()
        # img_uri = "data:image/png;base64,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"
        img_uri = json_dict['content'] # data:image/png;base64,iVBORw0KG...

        text = req_tencent_api.req_thirdparty_ocr(img_uri)
        # text = '我知道'
        res = {
            'status':'OK',
            'msg':'Success',
            'ocr_result':text,
        }

    except Exception as e:
        print("Error occured: " + str(e))
        res = {
            'status':'ERROR',
            'msg': str(e),
        }

    return json.dumps(res ,indent=4, sort_keys=True)



 




 

