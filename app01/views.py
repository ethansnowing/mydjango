from django.shortcuts import render
from app01 import models
# Create your views here.

category_list = models.Category.objects.filter(set_as_top_menu=True).order_by('position_index')
video_list = models.Video.objects.order_by('name')
def index(request):

    return render(request,'app01/index.html', {'category_list':category_list,
                                               'video_list':video_list})

def hehe(request):
    print('aaaaa')
    return render(request,'app01/hehe.html')

def showImg(request):
    return render(request,'app01/index.html')