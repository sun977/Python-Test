'''
仅供学习使用
by 久违  2019.12
'''
import requests
import json
from fake_useragent import UserAgent
import re

print("*****根据歌手音乐ID爬取歌词*****")
music_id=input("请输入歌手音乐的id：")

#随机生成请求头
for i in range(50):
    headers = {"user-agent": UserAgent().random}

'''
固定的请求头
headers={"User-Agent" : "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9.1.6) ",
  "Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
  "Accept-Language" : "en-us",
  "Connection" : "keep-alive",
  "Accept-Charset" : "GB2312,utf-8;q=0.7,*;q=0.7"}
'''

url = 'http://music.163.com/api/song/lyric?'+ 'id=' + music_id+ '&lv=1&kv=1&tv=-1'
r = requests.get(url,headers=headers,allow_redirects=False)
#allow_redirects设置为重定向

json_obj = r.text
j = json.loads(json_obj)#进行json解析

lrc = j['lrc']['lyric']
pat = re.compile(r'\[.*\]')#去除[04:27.737]
lrc = re.sub(pat,"",lrc)
lrc = lrc.strip()

#print(j['lrc']['lyric'])
print(lrc)

fp=open('Music_Lyric_'+music_id+'.txt','w')
fp.writelines(lrc)
fp.close()
print("歌词已经导出！")
