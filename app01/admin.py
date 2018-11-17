from django.contrib import admin
from app01 import models
# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','category','author','pub_date','last_modify','status','priority')
class CommentAdmin(admin.ModelAdmin):
    list_display = ('article','parent_comment','comment_type','comment','user','date')
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','set_as_top_menu','position_index')

admin.site.register(models.Article)
admin.site.register(models.Comment)
admin.site.register(models.UserProfile)
admin.site.register(models.Category)
