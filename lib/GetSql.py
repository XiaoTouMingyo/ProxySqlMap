import requests,json,config,time

class GetSql:

    def __init__(self):
        pass

    def GetList(self):
        jsonlist = requests.get(url="http://"+config.sqlmap+"/admin/"+config.admin_token+"/list")
        return json.loads(jsonlist.text)['tasks']

    def GetTask(self,taskid):
        jsonlist = requests.get(url="http://"+config.sqlmap+"/scan/"+taskid+"/data")
        return json.loads(jsonlist.text)['data']

    def DelTask(self,taskid):
        jsonlist = requests.get(url="http://" + config.sqlmap + "/task/" + taskid + "/delete")
        return json.loads(jsonlist.text)['success']

    def Foreach(self):
        print("开始判断是否存在注入!")
        while True:
            for k,v in self.GetList().items():
                if v == 'terminated' and len(self.GetTask(k)) == 0:
                    print("[-] task:"+k+'   not inject')
                    self.DelTask(k)
                elif v == 'terminated' and len(self.GetTask(k)) >= 1:
                    print("[+] task:"+k+'    is inject')
                    with open("SQL.txt",'a+') as file:
                        file.write(str(self.GetTask(k))+"\n")
                    self.DelTask(k)
            time.sleep(60)
