# coding=utf-8

import urllib2
import json

# curl -X POST "https://api-cn.faceplusplus.com/facepp/v3/detect" -F "api_key=B1eul1h0WJNC5GfPzBu9Nc-VS8pQKpNX" \
# -F "api_secret=g0N3RcCQR4HwlQbEcJY__SNkTDQ4jFik" \
# -F "image_file=@demo.jpg" \
# -F "return_landmark=1" \
# -F "return_attributes=gender,age,beauty"

def http_post(url, data_json):
    jdata = json.dumps(data_json)
    req = urllib2.Request(url, jdata)
    response = urllib2.urlopen(req)
    return response.read()

def gen_post_para(image_file,
                  api_key="B1eul1h0WJNC5GfPzBu9Nc-VS8pQKpNX",
                  api_secret="g0N3RcCQR4HwlQbEcJY__SNkTDQ4jFik",
                  return_landmark=1,
                  return_attributes="gender,age,beauty"
                  ):
    para = {
        "image_file":  open(image_file, 'rb'),
        "api_key": api_key,
        "api_secret": api_secret,
        "return_landmark": return_landmark,
        "return_attributes": return_attributes
    }

if __name__ == "__main__":
    url = "https://api-cn.faceplusplus.com/facepp/v3/detect"
    para = gen_post_para("demo.jpg")
    print http_post(url, para)


