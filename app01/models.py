from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=255)
    brief = models.CharField(null=True,blank=True,max_length=255)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    content = models.TextField(u"文章内容")
    author = models.ForeignKey("UserProfile", on_delete=models.CASCADE)
    pub_date = models.DateTimeField(blank=True,null=True)
    last_modify = models.DateTimeField(auto_now=True)
    priority = models.IntegerField(u"优先级",default=1000)
    head_img = models.ImageField(u"文章标题图片", upload_to='uploads')
    status_choices = (('draft',u"草稿"),
                      ('published',u"已发布"),
                      ('hidden',u"隐藏"))
    status = models.CharField(choices=status_choices,default='published',max_length=255)
    def __str__(self):
        return self.title
    def clean(self):
        if self.status == 'draft' and self.pub_date is not None:
            raise ValidationError('Draft entries may not have a publish data')
        if self.status == 'published' and self.pub_date is None:
            self.pub_date = datetime.date.today()


class Video(models.Model):
    name = models.CharField(max_length=255,null=True,blank=True)    # 视频名称
    httpurl = models.CharField(max_length=255)      # 视频httpurl
    ftpurl = models.CharField(max_length=255)       # 视频ftpur
    path = models.CharField(max_length=255)     # 视频路径
    qrcode = models.CharField(max_length=64)   # 二维码的路径名
    screenshot = models.CharField(max_length=64)    # 缩略图的路径名
    video_coding = models.CharField(max_length=255)     # 视频编码格式
    audio_coding = models.CharField(max_length=255)     # 音频编码格式
    format = models.CharField(max_length=255)       # 视频封装格式
    suffix = models.CharField(max_length=16)    # 后缀名
    distinguishability = models.CharField(max_length=16,blank=True) # 分辨率
    width = models.IntegerField(u'宽',blank=True)     # 宽
    height = models.IntegerField(u'高',blank=True)        # 高
    avg_frame_rate = models.DecimalField(u'平均帧率', max_digits=5, decimal_places=2, blank=True)      #平均帧率
    duration = models.IntegerField(u'时长', blank=True)       # 时长
    bit_rate = models.IntegerField(u'码率', blank=True)       # 码率
    subtitle = models.BooleanField(default=False)
    audio_track = models.IntegerField(u"音轨数量",default=1)

    def __str__(self):
        return self.name

class PlayRecord(models.Model):
    name = models.ForeignKey(Video,on_delete=models.CASCADE)
    status_choices = (('0','unknown'),
                      ('1',u"正常"),
                      ('2',u"崩溃"),
                      ('3',u"失败"))
    status = models.CharField(choices=status_choices,default='0',max_length=16)
    process_cpu = models.CharField(max_length=16)   # 进程平均占用CPU
    peak_cpu = models.CharField(max_length=16)      # 进程峰值CPU
    total_cpu = models.CharField(max_length=16)     # PC总使用CPU
    process_mem = models.CharField(max_length=16)      # 进程平均占用内存
    peak_mem = models.CharField(max_length=16)      # 进程峰值内存
    used_mem = models.CharField(max_length=16)      # 已使用内存
    used_gpu = models.CharField(max_length=16)      # 已使用gpu
    peak_gpu = models.CharField(max_length=16)      # 峰值gpu
    product = models.CharField(max_length=16)       # 产品名
    version = models.CharField(max_length=16)       # 版本号

    def __str__(self):
        return self.name





class Comment(models.Model):
    article = models.ForeignKey(Article,verbose_name=u"所属文章", on_delete=models.CASCADE)
    parent_comment = models.ForeignKey('self',related_name='my_children',blank=True,null=True,on_delete=models.CASCADE)
    comment_choices = ((1,u'评论'),
                       (2,u'点赞'))
    comment_type = models.IntegerField(choices=comment_choices,default=1)
    user = models.ForeignKey("UserProfile",on_delete=models.CASCADE)
    comment = models.TextField(blank=True,null=True)
    date = models.DateTimeField(auto_now_add=True)
    def clean(self):
        if self.comment_type ==1 and len(self.comment)==0:
            raise ValidationError('评论不能为空')

    def __str__(self):
        return "%s,P:%s,%s" %(self.articel,self.parent_comment.id,self.comment)

class Category(models.Model):
    name = models.CharField(max_length=64)
    brief = models.CharField(null=True,blank=True,max_length=255)
    set_as_top_menu = models.BooleanField(default=False)
    position_index = models.SmallIntegerField()
    admins = models.ManyToManyField("UserProfile",blank=True)
    def __str__(self):
        return self.name

class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=32)
    signature = models.CharField(max_length=255,blank=True,null=True)
    head_img = models.ImageField(height_field=150,width_field=150,blank=True,null=True)

    def __str__(self):
        return self.name


# 多个产品的播放情况列表、一个视频的CPU内存详情表