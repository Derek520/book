from datetime import date

from django.shortcuts import render,redirect
from .models import BookInfo,HeroInfo
# Create your views here.

def index(request):
    '''首页'''
    # 查询数据库所有数据
    booklist = BookInfo.objects.filter(is_delete=False)
    # 组织上下文
    context = {'boolist':booklist}
    # 返回数据
    return render(request,'my_book/index.html',context)

# 显示英雄数据
def show(request,id):
    '''英雄数据'''
    # 查询对应的id图书
    book = BookInfo.objects.get(id=id)
    # 根据外键查询对应的英雄
    bookinfo = book.heroinfo_set.all()
    # 组织乡下文
    context = {'bookinfo':bookinfo,'title':book}
    # 返回数据
    return render(request,'my_book/show.html',context)

# 创建新书
def create(request):
    '''创建新书'''
    # 创建数据库表对象
    book = BookInfo()
    # 添加数据
    book.btitle = '白发魔女'
    book.bdate = date(1991,5,9)
    # 数据添加完,需要保存方能生效
    book.save()
    # 页面跳转到首页
    return redirect('/')

# 逻辑删除书籍
def delete(request,id):
    '''删除书籍'''
    # 查询数据库
    bookinfo = BookInfo.objects.get(id=id)
    bookinfo.is_delete = True
    bookinfo.save()
    return redirect('/')