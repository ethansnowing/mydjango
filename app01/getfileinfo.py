#!/usr/bin/env Python
# -*- coding:utf-8 -*-
# getfileinfo.py
# 获取视频信息
# author:Ethan

from ffmpeg import stream
import os
from decimal import Decimal
# import ffmpeg

# print(dir(stream))
# print(help(stream))
# s.input('G(MPEG-PS)_V(Main@Main,480P)_A(Layer2).mpeg')
# print(a.get('a'))

class file_info():
    def __init__(self,file):
        n = stream.Stream()
        print(file)
        n.input(file)
        self.info = n.video_info()

    def get_px(self):
        result = {'width': '', 'height':'', 'nArea':''}
        for stream in self.info['streams']:
            # print(stream)
            if stream['codec_type'] == 'video':
                if 'width' in stream:
                    width = stream['width']
                    result['width'] = width
                if 'height' in stream:
                    height = stream['height']
                    result['height'] = height
                if width!=''and height!='':
                    try:
                        nArea = int(width)*int(height)
                        if(nArea <= 0):
                            result['nArea'] = ''
                        elif(nArea > 20000000):
                            result['nArea'] = '8K'
                        elif(nArea > 5000000):
                            result['nArea'] = '4K'
                        elif(nArea > 3000000):
                            result['nArea'] = '2K'
                        elif(nArea > 1500000):
                            result['nArea'] = '1080P'
                        elif(nArea > 500000):
                            result['nArea'] = '720P'
                        elif(nArea > 200000):
                            result['nArea'] = '480P'
                        else:
                            result['nArea'] = '240P'
                    except:
                        print('计算int(width)*int(height)出错！！！')
                else:
                    result['nArea'] = ''
        return result

    def get_avg_frame_rate(self):
        result = {'avg_frame_rate':''}
        for stream in self.info['streams']:
            if stream['codec_type'] == 'video':
                if 'avg_frame_rate' in stream:
                    if stream['avg_frame_rate']=='0/0' or stream['avg_frame_rate']=='':
                        result['avg_frame_rate'] = 0.00
                    else:
                        avg_frame_rate = eval(stream['avg_frame_rate'])
                        result['avg_frame_rate'] = float('%.2f' % avg_frame_rate)
        return result

    def get_codec_name(self):
        result = {'codec_name':''}
        for stream in self.info['streams']:
            if stream['codec_type'] == 'video':
                if 'codec_name' in stream:
                    result['codec_name'] = stream['codec_name']
        return result

    def get_display_aspect_ratio(self):
        result = {'display_aspect_ratio':''}
        for stream in self.info['streams']:
            if stream['codec_type'] == 'video':
                if 'display_aspect_ratio' in stream:
                    result['display_aspect_ratio'] = stream['display_aspect_ratio']
        return result

    def get_format_name(self):
        result = {'format_name':''}
        result['format_name'] = self.info['format']['format_name']
        return result

    def get_duration(self):
        result = {'duration':''}
        duration = self.info['format']['duration']
        result['duration'] = int(float(duration))
        # result['duration'] = self.info['format']['duration']
        return result

    def get_bit_rate(self):
        result = {'bit_rate':''}
        bit_rate = self.info['format']['bit_rate']
        if float(bit_rate)>0:
            result['bit_rate'] = str(int(float(bit_rate)/1000))
        else:
            result['bit_rate'] = bit_rate
        return result

def main():
    file = r'E:\\xmp资料\\测试用视频\\各类型视频\\apple-iphone4-design_video-us-20100607_848x480.mov'
    # file = 'G(MPEG-PS)_V(Main@Main,480P)_A(Layer2).mpeg'
    fi = file_info(file)
    # fi.get_video_info(file)
    print(fi.get_px())
    print(fi.get_avg_frame_rate())
    print(fi.get_codec_name())
    print(fi.get_display_aspect_ratio())
    print(fi.get_format_name())
    print(fi.get_duration())
    print(fi.get_bit_rate())




if __name__ == '__main__':
    main()