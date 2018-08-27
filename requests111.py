import requests

r = requests.get("http://www.baidu.com")

print(r.text)
hd = {'User-agent':'123','Connection':'close'}
r=requests.get("http://www.baidu.com",headers=hd,)
print(r.request.headers)
#{'User-Agent': 'python-requests/2.19.1', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive'}
#'User-Agent': 'python-requests/2.19.1'   告诉HTTP服务器， 客户端使用的操作系统和浏览器的名称和版本.
#Accept-Encoding': 'gzip,deflate'  浏览器申明自己接收的编码方法，通常指定压缩方法，是否支持压缩，支持什么压缩方法（gzip，deflate）
#'Accept': '*/*'   浏览器端可以接受的媒体类型,       Accept: */*  代表浏览器可以处理所有类型,(一般浏览器发给服务器都是发这个)
#'Connection': 'keep-alive'

# Connection: keep-alive   当一个网页打开完成后，客户端和服务器之间用于传输HTTP数据的TCP连接不会关闭，
# 如果客户端再次访问这个服务器上的网页，会继续使用这一条已经建立的连接