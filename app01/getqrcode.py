#!/usr/bin/env Python
# -*- coding:utf-8 -*-
# make_qrcode.py
# 生成二维码图片
# author:Ethan

from django.shortcuts import render

import os,sys
import qrcode
import sqlite3
import re
import getfileinfo
import requests
from dbutil import DBUtil
from django.db import connection



def update_video_info():
    conn = sqlite3.connect('./../db.sqlite3')
    cursor = conn.cursor()    # 链接数据库
    url = 'http://10.10.1.7/MediaLib/httpurl.txt'   # 服务器视频播放列表httpurl.txt的下载地址
    r = requests.get(url)       # 下载该txt并保持到本地
    with open('httpurl.txt', 'wb') as f:
        f.write(r.content)
    with open('httpurl.txt','rb') as f:
        for line in f.readlines():
            httpurl = line.decode('utf-8')      # 数据库里面的httpurl是有/r/n的
            name = os.path.split(httpurl[:-2])[1]
            query = 'select id from app01_video where httpurl="{}"'.format(httpurl)
            cursor.execute(query)
            video_list = cursor.fetchall()
            if not video_list:
                dbutil = DBUtil()
                dbutil.add_video(conn, httpurl[:-2])     # ffmpeg是不能有/r/n的


    conn.commit()
    conn.close()

# def make_qrcode(str, file):
#     img = qrcode.make(str)
#     img.save(file)

# print(dir(qrcode))
# img = qrcode.make('haha')
# img.save("./../statics/qrcode/hehe.jpg")
#

def con_sql3():
    conn = sqlite3.connect('./../db.sqlite3')
    cursor = conn.cursor()
    video_list = cursor.execute("select id,httpurl from app01_video")
    for video in video_list:
        httpurl = video[1]
        id = video[0]
        img = qrcode.make(httpurl)
        img_file_name = "./../statics/qrcode/"+str(id)+".jpg"
        img.save(img_file_name)


def get_info():
    conn = sqlite3.connect('./../db.sqlite3')
    c = conn.cursor()
    url_list = c.execute("select httpurl from app01_video")
    i = 0
    j = 0
    for url in url_list:
        if j > 2:      # 测试30个视频
            break
        try:
            relative_path = re.sub(r'http://10.10.1.7/', '', url[0])
            abs_path = 'U://'+ relative_path
            fi = getfileinfo.file_info(abs_path)
            str_width =  fi.get_px()['width']
            str_height = fi.get_px()['height']
            nArea = fi.get_px()['nArea']
            if nArea=='':
                width = -1
                height = -1
            else:
                width = int(str_width)
                height = int(str_height)
            print("宽：%s, 高：%s, 分辨率：%s" %(width, height, nArea))
            print(fi.get_avg_frame_rate())
            print(fi.get_codec_name())
            print(fi.get_display_aspect_ratio())
            print(fi.get_format_name())
            print(fi.get_duration())
            print(fi.get_bit_rate())
            j += 1
        except Exception as e:
            print(e)
            i += 1
    print("%s个视频获取视频信息失败" % i)
    conn.close()

def main():
    update_video_info()

if __name__ == '__main__':
    main()