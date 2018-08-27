import requests

def getHtmlText(url):
    try:
        r= requests.get(url,timeout=30)
        #获取页面内容
        r.raise_for_status()
        #如果状态码不是200，则提示异常
        r.encoding =r.apparent_encoding
        #设置正确的编码格式
        return r.text
        #返回页面内容
    except:
        return "something wrong!"