#!/usr/bin/env Python
# -*- coding:utf-8 -*-
# dbutil.py
# 数据库操作工具类
# author:Ethan
import sqlite3
import re
import os

import getfileinfo


class DBUtil():

    def add_video(self, conn, httpurl):
        relative_path = re.sub(r'http://10.10.1.7/', '', httpurl)
        abs_path = 'U://' + relative_path
        suffix = os.path.splitext(abs_path)[1]
        cursor = conn.cursor()  # 链接数据库
        fi = getfileinfo.file_info(abs_path)
        # print(fi.info)
        name = os.path.split(httpurl)[1]
        httpurl_db = httpurl + '\r\n'
        ftpurl = re.sub('^ht', 'f', httpurl)
        path = re.sub(r'http://10.10.1.7/', '/data1/', httpurl)
        video_coding = fi.get_codec_name()['codec_name']
        audio_coding = fi.get_audio_coding()['audio_coding']
        format = fi.get_format_name()['format_name']
        px_result = fi.get_px()
        distinguishability = px_result['nArea']
        # 如果没有获取到媒体信息，获取的结果是''；媒体信息本身也可能是''
        if px_result['width'] == '':
            width = -1
        else:
            width = int(px_result['width'])
        if px_result['height'] == '':
            height = -1
        else:
            height = int(px_result['height'])
        avg_frame_rate = fi.get_avg_frame_rate()['avg_frame_rate']
        duration = fi.get_duration()['duration']
        bit_rate = fi.get_bit_rate()['bit_rate']
        subtitle = fi.get_subtitle_counts()['subtitle_counts']
        audio_track = fi.get_audio_counts()['audio_counts']
        # 增加video信息到数据库
        sql = "insert into app01_video(name,httpurl,ftpurl,path,video_coding," \
              "audio_coding,format,suffix,distinguishability,width,height,avg_frame_rate," \
              "duration,bit_rate,subtitle,audio_track) values('{}', '{}', '{}', '{}'," \
              "'{}', '{}', '{}', '{}', '{}', {}, {}, {}, {}, {}, {}, {})".format(name, httpurl_db, \
                ftpurl, path, video_coding, audio_coding, format, suffix, distinguishability, width, \
                height, avg_frame_rate, duration, bit_rate, subtitle, audio_track)
        # cursor.execute(sql)


    def update_video(self, conn, httpurl):
        relative_path = re.sub(r'http://10.10.1.7/', '', httpurl)
        abs_path = 'U://' + relative_path
        suffix = os.path.splitext(abs_path)[1]
        cursor = conn.cursor()  # 链接数据库
        fi = getfileinfo.file_info(abs_path)
        # print(fi.info)
        name = os.path.split(httpurl)[1]
        httpurl_db = httpurl + r'\r\n'
        ftpurl = re.sub('^ht', 'f', httpurl)
        path = re.sub(r'http://10.10.1.7/', '/data1/', httpurl)
        video_coding = fi.get_codec_name()['codec_name']
        audio_coding = fi.get_audio_coding()['audio_coding']
        format = fi.get_format_name()['format_name']
        px_result = fi.get_px()
        distinguishability = px_result['nArea']
        # 如果没有获取到媒体信息，获取的结果是''；媒体信息本身也可能是''
        if px_result['width'] == '':
            width = -1
        else:
            width = int(px_result['width'])
        if px_result['height'] == '':
            height = -1
        else:
            height = int(px_result['height'])
        avg_frame_rate = fi.get_avg_frame_rate()['avg_frame_rate']
        duration = fi.get_duration()['duration']
        bit_rate = fi.get_bit_rate()['bit_rate']
        subtitle = fi.get_subtitle_counts()['subtitle_counts']
        audio_track = fi.get_audio_counts()['audio_counts']
        # 无论是否有改变，统一更新video信息到数据库
        sql = "insert into app01_video(name,httpurl,ftpurl,path,video_coding," \
              "audio_coding,format,suffix,distinguishability,width,height,avg_frame_rate," \
              "duration,bit_rate,subtitle,audio_track) values('{}', '{}', '{}', '{}'," \
              "'{}', '{}', '{}', '{}', '{}', {}, {}, {}, {}, {}, {}, {})".format(name, httpurl_db, \
                ftpurl, path, video_coding, audio_coding, format, suffix, distinguishability, width, \
                height, avg_frame_rate, duration, bit_rate, subtitle, audio_track)


def main():
    httpurl = 'http://10.10.1.7/MediaLib/multiple/G(Matroska)_V(AVC,High@L4.0,1080P)' \
    '_A(AAC,LC)_T(UTF-8).flv'
    conn = sqlite3.connect('./../db.sqlite3')
    dbutil = DBUtil()
    dbutil.add_video(conn, httpurl)
    conn.commit()  # 必须要提交才生效
    conn.close()

if __name__ == '__main__':
    main()



