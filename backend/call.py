# coding=utf-8

# 导入系统库并定义辅助函数
from pprint import pformat

# import PythonSDK
from PythonSDK.facepp import API,File

# 导入图片处理类
import PythonSDK.ImagePro






# 此方法专用来打印api返回的信息
def print_result(hit, result):
    print(hit)
    print('\n'.join("  " + i for i in pformat(result, width=75).split('\n')))

def printFuctionTitle(title):
    return "\n"+"-"*60+title+"-"*60;

# 初始化对象，进行api的调用工作
api = API()
# -----------------------------------------------------------人脸识别部分-------------------------------------------

faceSet_img = 'demo5.jpg'       # 用于创建faceSet
# 人脸检测：https://console.faceplusplus.com.cn/documents/4888373
# res = api.detect(image_url=detech_img_url, return_attributes="gender,age,smiling,headpose,facequality,"
res = api.detect(image_file=File(faceSet_img), return_attributes="gender,age,smiling,"
                                                       "emotion,ethnicity,beauty,"
                                                       "skinstatus")
# print_result(printFuctionTitle("人脸检测"), res)

for face in res["faces"]:
    print "-------------------"
    print "年龄:", face["attributes"]["age"]["value"]
    print "性别:", face["attributes"]["gender"]["value"]
    print "女人眼中颜值:", face["attributes"]["beauty"]["female_score"]
    print "男人眼中颜值:", face["attributes"]["beauty"]["male_score"]

