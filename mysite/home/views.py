# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Student

def index(request):    
    students_obj = Student.objects.all()
    return render(request, 'home/student_list.html', locals())
 