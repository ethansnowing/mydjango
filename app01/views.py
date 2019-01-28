from django.shortcuts import render,HttpResponse
from app01 import models
import os
from django.core.paginator import Paginator
from django.db import connection
# Create your views here.

category_list = models.Category.objects.filter(set_as_top_menu=True).order_by('position_index')
video_list = models.Video.objects.order_by('name')
def index(request):
    f = open('httpurl.txt','rb')
    for line in f.readlines():
        httpurl = line[:-2].decode('utf-8')
        name = os.path.split(httpurl)[1]
        try:
            i_video = models.Video.objects.get(httpurl=httpurl)
            # print(httpurl,i_video.id)
        except :
            # dic = {"name":name,"httpurl":httpurl}
            # models.Video.objects.create(**dic)
            pass
        # imgpath = "./statics/qrcode/" + name
        # img = qrcode.make(httpurl)
        # id = models.Video.objects.filter(name=imgpath)
        # print(type(img))
    print(len(video_list))
    # models.Video.objects.filter(id=5).delete()        # 数据库列删除
    paginator = Paginator(video_list,50)    # show 50 contacts per page
    page = request.GET.get('page')
    video_list_page = paginator.get_page(page)
    return render(request,'app01/index.html', {'category_list':category_list,
                                               'video_list_page':video_list_page})

def hehe(request):
    print('aaaaa')
    cursor = connection.cursor()
    # list = cursor.execute('select * from (select * from video order by name desc) where rownum <=20')
    list = cursor.execute('select * from app01_video where id<=20')
    # return render(request,'app01/hehe.html')
    return HttpResponse(list)

def showImg(request):
    return render(request,'app01/index.html')