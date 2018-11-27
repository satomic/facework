# coding=utf-8

from MicroService.Service import BaseService
from config import CONFIG


class ServiceLoadBalancer(BaseService):

    TIMEOUT = 100

    def __init__(self, uri="/loadbalacner", service_name="loadbalacner", threaded=True,):
        BaseService.__init__(self, uri=uri, service_name=service_name, threaded=threaded)

    def process(self, dictReq):
        # todo 保存图片到某路径，拼接出公网url传递下去

        ret = self.serviceCall(CONFIG.get("BACKEND_URL"),dictReq)
        # dictReq = {
        #  "type": "local/url",
        #  "path": "path"
        # }
        return ret

if __name__ == "__main__":

    ms = ServiceLoadBalancer()
    ms.start()
