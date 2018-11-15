from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=255)
    brief = models.CharField(null=True,blank=True,max_length=255)
    category = models.ForeignKey("Category")
    content = models.TextField(u"文章内容")
    author = models.ForeignKey("UserProfile")
    pub_date = models.DateTimeField(auto_now_add=True)
    last_modify = models.DateTimeField(auto_now=True)
    priority = models.IntegerField(u"优先级",default=1000)
    status_choices = (('draft',u"草稿"),
                      ('published',u"已发布"),
                      ('hidden',u"隐藏"))
    status = models.CharField(choices=status_choices,default='published')
    def clean(self):
        if self.status == 'draft' and self.pub_date is not None:
            raise ValidationError('Draft entries may not have a publish data')
        if self.status == 'published' and self.pub_date is None:
            self.pub_date = datetime.date.today()
    def __unicode__(self):
        return self.title

class Comment(models.Model):
    article = models.ForeignKey(Article,verbose_name=u"所属文章")
    parent_comment = models.ForeignKey('self',related_name='my_children',blank=True,null=True)
    comment_choices = ((1,u'评论'),
                       (2,u'点赞'))
    comment_type = models.IntergerField(choices=comment_choices,default=1)
    user = models.DateTimeField(auto_now_add=True)
    comment = models.TextField(blank=True,null=True)
    date = models.DateTimeField(auto_now_add=True)
    def __unicode__(self):
        return "%s,P:%s,%s" %(self.articel,self.parent_comment.id,self.comment)

class Category(models.Model):
    name = models.CharField(max_length=64)
    brief = models.CharField(null=True,blank=True,max_length=255)
    set_as_top_menu = models.BooleanField(default=False)
    position_index = models.SmallIntergerField()
    admins = models.ManyToManyField("UserProfile",blank=True)
    def __unicode__(self):
        return self.name

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    name = models.CharField(max_length=32)
    signature = models.CharField(max_length=255,blank=True,null=True)
    head_img = models.ImageField(height_field=150,width_field=150,blank=True,null=True)

    def __unicode__(self):
        return self.name


# 多个产品的播放情况列表、一个视频的CPU内存详情表