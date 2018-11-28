# coding=utf-8

import os
from flask import Flask, request, redirect, url_for
from werkzeug import secure_filename
import platform
import uuid
import datetime,time
from MicroService.serviceRequest import serviceCall

sysstr = platform.system()
UPLOAD_FOLDER = 'tmp'
if (sysstr != "Windows"):
    UPLOAD_FOLDER = '/tmp'

ALLOWED_EXTENSIONS = set(['jpg'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

def current_time():
    return datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S_%f')[:-3]


def detectCall(serviceUri, dictRequest, timeout=30):
    # 0 input check
    if not isinstance(dictRequest, dict):
        return (500, {"error": "error in client input"})
    # 1 service call
    serviceName = os.path.basename(os.path.normcase(serviceUri)).lower()
    ret = serviceCall(serviceUri, dictRequest, timeout)
    return ret

def formate_detect_ret(detect_result):
    if len(detect_result) == 0:
        return ""
    # print type(detect_result), detect_result
    # detect_result = eval(detect_result)
    print type(detect_result),detect_result
    ret = ""
    face_counter = 0
    for face in detect_result["faces"]:
        ret = ret + u"-------------------<br>年龄: %s<br>性别: %s<br>女人眼中颜值: %s<br>男人眼中颜值: %s<br> " % (
            face["attributes"]["age"]["value"],
            u"女" if face["attributes"]["gender"]["value"] == u"Female" else u"男",
            face["attributes"]["beauty"]["female_score"],
            face["attributes"]["beauty"]["male_score"]
        )
        face_counter += 1
        if face_counter == 5:
            break
    print "ret: ", ret
    return ret

global ret_detect, image_path
ret_detect = ""
image_path = ""

@app.route("/check", methods=['GET', 'POST'])
def check():
    image_show_html = ""
    for image_name in os.listdir(app.config['UPLOAD_FOLDER']):
        image_show_html += '''<img src="http://47.104.5.241:30080/images/%s" /><br>''' % image_name

    return """
    <!doctype html>
    <title>图片检查</title>
    <h1>已有图片列表</h1>
    %s
    """ % image_show_html

@app.route("/", methods=['GET', 'POST'])
def index():

    try:
        if request.method == 'POST':
            file = request.files['file']
            if file and allowed_file(file.filename):
                filename = "%s_%s_%s" % (current_time(), uuid.uuid1(),secure_filename(file.filename))
                filename = filename[:-4] + ".jpg"
                print "filename:", filename
                filename = filename.replace(' ','_')
                print "filename:", filename
                # filename = file.filename
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                global image_path
                image_path = "http://47.104.5.241:30080/images/%s" % filename
                dict_req = {
                    "type": "url",
                    "path": image_path
                }
                # dict_req = {
                #    "type":"url",
                #    "path": "https://ss2.baidu.com/6ONYsjip0QIZ8tyhnq/it/u=303579710,2051412562&fm=173&app=25&f=JPEG?w=640&h=772&s=E7901B8D168B42FF07A8089503005083g"
                # }
                global  ret_detect
                ret_detect = detectCall("http://47.104.5.241:30001/detect", dict_req)
                print "ret_detect internal: ", ret_detect
                return redirect(url_for('index'))
    except Exception:
        return redirect(url_for('index'))

    global ret_detect, image_path
    print "ret_detect global: ", ret_detect
    return """
    <!doctype html>
    <title>颜值检测</title>
    <h1>选择需要检测的图片(最多5张脸)</h1>
    <form action="" method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=检测>
    </form>
    <img src="%s" />
    <p>%s</p><br>
    """ % (image_path, formate_detect_ret(ret_detect))
    # """ % ("<br>".join(os.listdir(app.config['UPLOAD_FOLDER'],)), ret_detect)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
