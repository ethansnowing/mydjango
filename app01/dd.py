import os
import requests
import sqlite3
from dbutil import DBUtil
from django.db import connection

a = {'format': {'format_long_name': 'Matroska / WebM', 'tags': {'encoder': 'libebml v1.3.0 + libmatroska v1.4.1', 'creation_time': '2014-04-14T09:38:32.000000Z'}, 'filename': 'U://MediaLib/multiple/G(Matroska)_V(AVC,High@L4.0,1080P)_A(AAC,LC)_T(UTF-8).flv', 'format_name': 'matroska,webm', 'size': '848270775', 'bit_rate': '5117463', 'start_time': '0.000000', 'probe_score': 100, 'nb_streams': 3, 'duration': '1326.080000', 'nb_programs': 0}, 'streams': [{'color_range': 'tv', 'profile': 'High', 'chroma_location': 'topleft', 'field_order': 'progressive', 'disposition': {'attached_pic': 0, 'karaoke': 0, 'dub': 0, 'visual_impaired': 0, 'hearing_impaired': 0, 'lyrics': 0, 'default': 1, 'clean_effects': 0, 'timed_thumbnails': 0, 'comment': 0, 'original': 0, 'forced': 0}, 'sample_aspect_ratio': '1:1', 'width': 1916, 'codec_tag': '0x0000', 'refs': 1, 'bits_per_raw_sample': '8', 'height': 1076, 'pix_fmt': 'yuv420p', 'has_b_frames': 1, 'r_frame_rate': '24000/1001', 'is_avc': 'true', 'color_space': 'bt709', 'color_transfer': 'bt709', 'codec_type': 'video', 'coded_width': 1916, 'avg_frame_rate': '24000/1001', 'codec_long_name': 'H.264 / AVC / MPEG-4 AVC / MPEG-4 part 10', 'start_time': '0.000000', 'display_aspect_ratio': '479:269', 'time_base': '1/1000', 'color_primaries': 'bt709', 'index': 0, 'codec_time_base': '1001/48000', 'tags': {'title': 'H.264'}, 'nal_length_size': '4', 'level': 40, 'codec_tag_string': '[0][0][0][0]', 'codec_name': 'h264', 'start_pts': 0, 'coded_height': 1076}, {'disposition': {'attached_pic': 0, 'karaoke': 0, 'dub': 0, 'visual_impaired': 0, 'hearing_impaired': 0, 'lyrics': 0, 'default': 1, 'clean_effects': 0, 'timed_thumbnails': 0, 'comment': 0, 'original': 0, 'forced': 0}, 'start_pts': 0, 'codec_time_base': '1/48000', 'sample_rate': '48000', 'time_base': '1/1000', 'avg_frame_rate': '0/0', 'codec_long_name': 'AAC (Advanced Audio Coding)', 'start_time': '0.000000', 'codec_tag': '0x0000', 'tags': {'title': 'AAC2.0', 'language': 'eng'}, 'index': 1, 'codec_name': 'aac', 'sample_fmt': 'fltp', 'channel_layout': 'stereo', 'r_frame_rate': '0/0', 'profile': 'LC', 'bits_per_sample': 0, 'channels': 2, 'codec_tag_string': '[0][0][0][0]', 'codec_type': 'audio'}, {'disposition': {'attached_pic': 0, 'karaoke': 0, 'dub': 0, 'visual_impaired': 0, 'hearing_impaired': 0, 'lyrics': 0, 'default': 0, 'clean_effects': 0, 'timed_thumbnails': 0, 'comment': 0, 'original': 0, 'forced': 0}, 'codec_tag': '0x0000', 'codec_time_base': '0/1', 'avg_frame_rate': '0/0', 'time_base': '1/1000', 'codec_long_name': 'SubRip subtitle', 'start_time': '0.000000', 'start_pts': 0, 'index': 2, 'codec_name': 'subrip', 'tags': {'title': 'CC', 'language': 'eng'}, 'r_frame_rate': '0/0', 'codec_tag_string': '[0][0][0][0]', 'duration': '1326.080000', 'codec_type': 'subtitle', 'duration_ts': 1326080}]}
for stream in a['streams']:
    print(stream)
print(a.get('format3',{}))
d = {'a':'1','b':'2'}
# print(d.has_key('a'))
# print(help(d))


conn = sqlite3.connect('./../db.sqlite3')
cursor = conn.cursor()  # 链接数据库
query = 'select id from app01_video where httpurl="{}"'.format(r'http://10.10.1.7/MediaLib/备份视频/岳磊/fftest.mp4\r\n')
cursor.execute(query)
video_list = cursor.fetchall()
print(video_list)
conn.close()
