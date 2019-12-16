from baseproxy.proxy import AsyncMitmProxy
from lib.ProxyRe import DebugInterceptor
from lib.GetSql import GetSql
import threading



def action():
    baseproxy = AsyncMitmProxy(server_addr=('', 8081), https=True,)
    baseproxy.register(DebugInterceptor)
    baseproxy.serve_forever()

if __name__ == '__main__':
    threading.Thread(target=action).start()
    threading.Thread(target=GetSql().Foreach()).start()
