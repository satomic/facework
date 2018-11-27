# coding=utf-8

from MicroService.Service import BaseService
from PythonSDK.facepp import API,File
from backend.config import CONFIG

class ServiceFace(BaseService):

    TIMEOUT = 100

    def __init__(self, uri="/app", service_name="app"):
        BaseService.__init__(self, uri=uri, service_name=service_name)
        self.api = API(API_KEY=CONFIG.get("API_KEY"), API_SECRET=CONFIG.get("API_SECRET"))

    def process(self, dictReq):
        # ret = "hello!", self.serviceCall("http://127.0.0.1:5001/test",dictReq) # call other microservice
        # dictReq = {
        #  "type": "local/url",
        #  "path": "path"
        # }
        return self.api.beauty(dictReq)

if __name__ == "__main__":

    ms = ServiceFace()
    ms.start()
