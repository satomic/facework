# coding=utf-8

from MicroService.Service import BaseService
from config import CONFIG


class ServiceLoadBalancer(BaseService):

    TIMEOUT = 100

    def __init__(self, uri="/loadbalacner", service_name="loadbalacner", threaded=True,):
        BaseService.__init__(self, uri=uri, service_name=service_name, threaded=threaded)

    def process(self, dictReq):
        # ret = self.serviceCall("http://face-detect:5000/detect",dictReq) # call other microservice
        ret = self.serviceCall("http://47.104.5.241:30001/detect",dictReq)
        # dictReq = {
        #  "type": "local/url",
        #  "path": "path"
        # }
        return ret

if __name__ == "__main__":

    ms = ServiceFace()
    ms.start()
