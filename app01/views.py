from django.shortcuts import render
from app01 import models
import os
# Create your views here.

category_list = models.Category.objects.filter(set_as_top_menu=True).order_by('position_index')
video_list = models.Video.objects.order_by('name')
def index(request):
    f = open('httpurl.txt','rb')
    for line in f.readlines():
        httpurl = line.decode('utf-8')
        name = os.path.split(httpurl)[1][:-2]
        # print(name, httpurl)

        # dic = {"name":name,"httpurl":httpurl}
        # models.Video.objects.create(**dic)
    f.close()
    # models.Video.objects.filter(id=5).delete()        # 数据库列删除
    return render(request,'app01/index.html', {'category_list':category_list,
                                               'video_list':video_list})

def hehe(request):
    print('aaaaa')
    return render(request,'app01/hehe.html')

def showImg(request):
    return render(request,'app01/index.html')