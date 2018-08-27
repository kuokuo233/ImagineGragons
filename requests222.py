import requests

r = requests.get("http://www.baidu.com")

print(r.status_code)
#状态码  200成功 404失败
print(r.headers)
#{'Cache-Control': 'private, no-cache, no-store, proxy-revalidate, no-transform',
# private只能作为私有缓存，不能共享  no-cache 响应不会被缓存，而是实时向服务器请求资源，不会影响缓存效率，还能保证安全  no-store 任何情况响应不会被缓存，不会写入磁盘
#proxy-revalidate 响应在特定条件下会被重用，必须到服务器上验证是否是最新的
#no-trasform
# 'Connection': 'Keep-Alive',
# 'Content-Encoding': 'gzip',
# 'Content-Type': 'text/html',代表浏览器可以接受服务器回发的类型为 text/html  也就是我们常说的html文档
# 'Date': 'Mon, 16 Jul 2018 09:55:26 GMT',原始服务器消息发出的时间
#  'Last-Modified': 'Mon, 23 Jan 2017 13:27:32 GMT',
# 'Pragma': 'no-cache',
#  'Server': 'bfe/1.0.8.18', web服务器软件名称
#  'Set-Cookie': 'BDORZ=27315;
# max-age=86400;
# domain=.baidu.com;
# path=/',
#  'Transfer-Encoding': 'chunked'}

print(r.encoding)
print(r.apparent_encoding)
print(r.content)