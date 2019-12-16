import requests,json
import config

class TestSql:
    def __init__(self,url,method,cookie,referer,data=''):
        self.sqlmap = config.sqlmap
        self.url = str(url)
        self.cookie = str(cookie)
        self.referer = str(referer)
        self.data = str(data)
        self.method = str(method)

    def getTaskId(self):
        taskid = requests.get(url='http://' + self.sqlmap + '/task/new')
        taskid = json.loads(taskid.text)
        return str(taskid['taskid'])

    def startScan_P(self,taskid):
        start = requests.post(url = "http://"+self.sqlmap + '/scan/' + taskid + '/start',data=json.dumps({"url":self.url,"data":self.data,"referfer":self.referer,"cookie":self.cookie}),headers={"Content-Type":"application/json"})
        if json.loads(start.text)["success"] == True:
            return True
        else:
            return False
    def startScan_G(self,taskid):
        start = requests.post(url = "http://"+self.sqlmap + '/scan/' + taskid + '/start',data=json.dumps({"url":self.url,"referfer":self.referer,"cookie":self.cookie}),timeout=5,headers={"Content-Type":"application/json"})
        if json.loads(start.text)["success"] == True:
            return True
        else:
            return False

    def action(self):
        if self.method.upper() == 'GET' and '?' in self.url:
            task = self.getTaskId()
            print("GetToken:"+task)
            if self.startScan_G(task):
                print("[+]Get:{0} success".format(self.url))
                with open("sqlscan.txt","a+") as file:
                    file.write("token:"+task+" Url:"+self.url+"\n")
        elif self.method.upper() == 'POST':
            task = self.getTaskId()
            if self.startScan_P(task):
                print("[+]POST:{0} success".format(self.url))
                with open("sqlscan.txt","a+") as file:
                    file.write("token:"+task+" Url:"+self.url+"\n")