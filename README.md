# ProxySqlMap

From Proxy to SqlMapApi

## 使用方法:

修改config.py:
1. Ext_filter 为过滤的后缀名
2. sqlmap 为SQLmap地址
3. url 为需要拦截的url
4. admin_token 为sqlmap的adminid

修改代理：127.0.0.1:8081

## 支持库:

1. requests
2. baseproxy(已经内置了，不需要再进行安装)

## https 支持:

访问:baseproxy.ca即可下载

## 输出:

sqlsan.txt 为已创建的taskid与URL

ok.txt为存在注入的URL以及taskid

## BUG以及建议:

http://www.f4ckweb.top/
