from django.shortcuts import render,redirect   # 加入 redirect 套件
from django.http import HttpResponse

def grade(request):
    return render (request, 'grade.html')
    