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
        try:
            self.info = n.video_info()
        except Exception as e:
            print(e)
            self.info = {}

    def get_px(self):
        result = {'width': '', 'height':'', 'nArea':'unknown'}
        if 'streams' in self.info:
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
                        result['nArea'] = 'unknown'
        return result

    def get_avg_frame_rate(self):
        result = {'avg_frame_rate':0.02}
        if 'streams' in self.info:
            for stream in self.info['streams']:
                if stream['codec_type'] == 'video':
                    if 'avg_frame_rate' in stream:
                        if stream['avg_frame_rate']=='0/0' or stream['avg_frame_rate']=='':
                            result['avg_frame_rate'] = 0.02
                        else:
                            avg_frame_rate = eval(stream['avg_frame_rate'])
                            result['avg_frame_rate'] = float('%.2f' % avg_frame_rate)
        return result

    def get_codec_name(self):
        result = {'codec_name':'unknown'}
        if 'streams' in self.info:
            for stream in self.info['streams']:
                if stream['codec_type'] == 'video':
                    if 'codec_name' in stream:
                        result['codec_name'] = stream['codec_name']
        return result

    def get_audio_coding(self):
        result = {'audio_coding':'unknown'}
        if 'streams' in self.info:
            for stream in self.info['streams']:
                if stream['codec_type'] == 'audio':
                    if 'codec_name' in stream:
                        result['audio_coding'] = stream['codec_name']
        return result


    def get_display_aspect_ratio(self):
        result = {'display_aspect_ratio':'unknown'}
        if 'streams' in self.info:
            for stream in self.info['streams']:
                if stream['codec_type'] == 'video':
                    if 'display_aspect_ratio' in stream:
                        result['display_aspect_ratio'] = stream['display_aspect_ratio']
        return result

    def get_format_name(self):
        result = {'format_name':'unknown'}
        result['format_name'] = self.info.get('format',{}).get('format_name','unknown')
        return result

    def get_duration(self):
        result = {'duration':0}
        duration = self.info.get('format',{}).get('duration',0)
        result['duration'] = int(float(duration))
        # result['duration'] = self.info['format']['duration']
        return result

    def get_bit_rate(self):
        result = {'bit_rate':0}
        bit_rate = self.info.get('format',{}).get('bit_rate',0)
        if int(bit_rate)>0:
            result['bit_rate'] = int(float(bit_rate)/1000)
        return result

    def get_subtitle_counts(self):
        result = {'subtitle_counts':0}
        subtitle_counts = 0
        if 'streams' in self.info:
            for stream in self.info['streams']:
                if stream.get('codec_type') == 'subtitle':
                    subtitle_counts += 1
            result['subtitle_counts'] = subtitle_counts
        return result

    def get_audio_counts(self):
        result = {'audio_counts':0}
        audio_counts = 0
        if 'streams' in self.info:
            for stream in self.info['streams']:
                if stream.get('codec_type') == 'audio':
                    audio_counts += 1
            result['audio_counts'] = audio_counts
        return result

def main():
    file = r'U://MediaLib/异常视频/PC/我们比PotPlayer强/G(AVC)_V(Baseline@L2.0,240P).mp4'
    # file = 'G(MPEG-PS)_V(Main@Main,480P)_A(Layer2).mpeg'
    print(os.path.splitext(file)[1])
    fi = file_info(file)
    print(fi.info)
    # fi.get_video_info(file)
    # print(fi.get_px())
    # print(fi.get_avg_frame_rate())
    # print(fi.get_codec_name())
    # print(fi.get_display_aspect_ratio())
    # print(fi.get_format_name())
    # print(fi.get_duration())
    # print(fi.get_bit_rate())
    # print(fi.get_subtitle_counts())
    # print(fi.get_audio_counts())




if __name__ == '__main__':
    main()