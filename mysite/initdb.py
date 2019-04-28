# -*- coding: UTF-8 -*-
import os
import sys
import django
import random
import datetime

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
    django.setup()
    from django.contrib.auth.models import User, Group, Permission
    from home.models import Student
    
    user = User.objects.create_superuser('admin', 'admin@test.com','1234qazx')
    user.save()
    
    user = User.objects.create_user('test1', 'test1@test.com','1234qazx')
    user.is_staff = True
    user.is_superuser = False
    user.save()      
    
    user = User.objects.create_user('test2', 'test2@test.com','1234qazx')
    user.is_staff = True
    user.is_superuser = False
    user.save() 

        
    s = Student()
    s.name = '李奎' 
    s.age = 28
    s.sex = 1
    s.save()  
    
    s = Student()
    s.name = '张兰' 
    s.age = 18
    s.sex = 2
    s.save()       
