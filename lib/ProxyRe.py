from baseproxy.proxy import ReqIntercept, RspIntercept
import config,threading
from lib.TestSql import TestSql

class DebugInterceptor(ReqIntercept,RspIntercept):

    def deal_request(self,data):
        if config.url not in data.hostname:
            return data
        if self.filter_ext(data.path):
            threading.Thread(target=TestSql(self.z_url(data.hostname,data.port,data.path),data.command,data.get_header('cookie'),data.get_header('referer'),data.get_body_data()).action()).start()
        return data
    def deal_response(self,data):
        # print(data.status)
        return data

    def filter_ext(self,path):
        for ext in config.Ext_filter:
            if(ext in path):
                return False
        return True

    def z_port(self,port):
        if int(port) == 443:
            return 'https://'
        else:
            return 'http://'

    def z_url(self,url,port,path):
        schema = self.z_port(port)
        url = schema+url+':'+str(port)+path
        return url