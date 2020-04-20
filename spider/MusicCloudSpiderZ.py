'''
仅供学习使用
by 久违  2019.12.12
'''
import re  #正则用库
import os
import json
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

#生成随机请求头
for i in range(50):
    headers = {"user-agent": UserAgent().random}

def download_by_music_id(music_id):
    #根据歌词id下载
    url = 'http://music.163.com/api/song/lyric?'+ 'id=' + str(music_id)+ '&lv=1&kv=1&tv=-1'
    r = requests.get(url,headers=headers)
    json_obj = r.text
    
    j = json.loads(json_obj)#json解析
    lrc = j['lrc']['lyric']
    pat = re.compile(r'\[.*\]')#去除除歌词之外的一些符号
    lrc = re.sub(pat,"",lrc)
    lrc = lrc.strip()
    return lrc

def get_music_ids_by_musican_id(singer_id):
    #通过一个歌手id下载这个歌手的所有歌词
    singer_url = 'http://music.163.com/artist?'+ 'id='+str(singer_id)
    r = requests.get(singer_url,headers=headers)
    soupObj = BeautifulSoup(r.text,'lxml')
    song_ids = soupObj.find('textarea')#获取<textarea>标签里的信息 歌名name和歌id
    jobj = json.loads(song_ids.text)#json解析

    ids = {}
    for item in jobj:
        ids[item['name']] = item['id']
    return ids

def get_singer_name_by_musican_id(singer_id):
    singer_url = 'http://music.163.com/artist?'+ 'id='+str(singer_id)
    r = requests.get(singer_url,headers=headers)
    soupOb = BeautifulSoup(r.text,'lxml')
    singer = soupOb.find('title')#获取<title>标签信息 <title>薛之谦 - 歌手 - 网易云音乐</title>
    singer_name=singer.text.split('-')
    return singer_name[0]#获取歌手姓名
    
def download_lyric(uid):
    #下载歌词到本地
    SingerName=get_singer_name_by_musican_id(uid)#获取歌手的姓名
    os.mkdir(SingerName)#以歌手姓名新建文件夹
    os.chdir(SingerName)#用于改变当前工作目录到指定路径

    music_ids = get_music_ids_by_musican_id(uid)#获取一个歌手所有歌名和对应的歌id号 字典
    for key in music_ids:
        text = download_by_music_id(music_ids[key])#对每一个歌id爬取歌词
        file = open(key + '.txt','a',encoding='utf-8')#以歌名命名每个TXT文本
        file.write(key +'\n')
        file.write(text)
        file.close()

try:
   print("*****根据歌手ID爬取所有歌的歌词*****")
   singer_id = input("请输入歌手的ID:")
   download_lyric(singer_id)
except Exception as err:
    print(err)
else:
    print("已完成数据爬取！")
