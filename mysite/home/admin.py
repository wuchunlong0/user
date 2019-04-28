# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Student
# Register your models here.

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):    
    list_display = ('id','name','age','sex')

admin.site.site_header = '用户登录' # 设置用户登录窗口标题
admin.site.site_title = 'login'    # 设置页面标题