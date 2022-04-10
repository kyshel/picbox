import json
import base64 
import cv2
import numpy as np

def data_uri_to_cv2_img(uri): 
    encoded_data = uri.split(',')[1]  # iVBORw0KG...
    nparr = np.fromstring(base64.b64decode(encoded_data), np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    return img

def do_gray(request):
    fp_grayed = './static/after/grayed.png'
    route_grayed = './after/grayed.png'
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