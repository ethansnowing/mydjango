from django.shortcuts import render
from app01 import models
# Create your views here.

category_list = models.Category.objects.filter(set_as_top_menu=True).order_by('position_index')
def index(request):

    return render(request,'app01/index.html', {'category_list':category_list})