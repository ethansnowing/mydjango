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




def getqrcode():
    f = open('httpurl.txt','rb')
    for line in f.readlines():
        httpurl = line[:-2].decode('utf-8')
        name = os.path.split(httpurl)[1][:-2]
        # dic = {"name":name,"httpurl":httpurl}
        # models.Video.objects.create(**dic)
        print(httpurl)
    f.close()


# def make_qrcode(str, file):
#     img = qrcode.make(str)
#     img.save(file)

# print(dir(qrcode))
# img = qrcode.make('haha')
# img.save("./../statics/qrcode/hehe.jpg")
#

def con_sql3():
    conn = sqlite3.connect('./../db.sqlite3')
    c = conn.cursor()
    video_list = c.execute("select id,httpurl from app01_video")
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
    # make_qrcode("哈哈", "/qrcode/haha.jpg")
    get_info()

if __name__ == '__main__':
    main()