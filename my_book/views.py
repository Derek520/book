from datetime import date

from django.shortcuts import render,redirect,HttpResponse
from django.core.urlresolvers import reverse
from .models import BookInfo,HeroInfo
# Create your views here.
from PIL import Image, ImageDraw, ImageFont
from django.utils.six import BytesIO


def index(request):
    '''首页'''
    # 查询数据库所有数据
    booklist = BookInfo.objects.filter(is_delete=False)
    # 组织上下文
    context = {'boolist':booklist}

    request.session['hello']='abc'
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

# 模板继承
def jc_templates(request):
    '''继承模板'''
    return render(request,'my_book/inherit_base.html')

# 验证码
def verify_code(request):
    print('验证码')
    #引入随机函数模块
    import random
    #定义变量，用于画面的背景色、宽、高
    bgcolor = (random.randrange(20, 100), random.randrange(
        20, 100), 255)
    width = 100
    height = 25
    #创建画面对象
    im = Image.new('RGB', (width, height), bgcolor)
    #创建画笔对象
    draw = ImageDraw.Draw(im)
    #调用画笔的point()函数绘制噪点
    for i in range(0, 100):
        xy = (random.randrange(0, width), random.randrange(0, height))
        fill = (random.randrange(0, 255), 255, random.randrange(0, 255))
        draw.point(xy, fill=fill)
    #定义验证码的备选值
    str1 = 'ABCD123EFGHIJK456LMNOPQRS789TUVWXYZ0'
    #随机选取4个值作为验证码
    rand_str = ''
    for i in range(0, 4):
        rand_str += str1[random.randrange(0, len(str1))]
    #构造字体对象，ubuntu的字体路径为“/usr/share/fonts/truetype/freefont”
    font = ImageFont.truetype('FreeMono.ttf', 23)
    #构造字体颜色
    fontcolor = (255, random.randrange(0, 255), random.randrange(0, 255))
    #绘制4个字
    draw.text((5, 2), rand_str[0], font=font, fill=fontcolor)
    draw.text((25, 2), rand_str[1], font=font, fill=fontcolor)
    draw.text((50, 2), rand_str[2], font=font, fill=fontcolor)
    draw.text((75, 2), rand_str[3], font=font, fill=fontcolor)
    #释放画笔
    del draw
    #存入session，用于做进一步验证
    request.session['verifycode'] = rand_str
    #内存文件操作
    buf = BytesIO()
    #将图片保存在内存中，文件类型为png
    im.save(buf, 'png')
    #将内存中的图片数据返回给客户端，MIME类型为图片png
    return HttpResponse(buf.getvalue(), 'image/png')

# 调用验证码
def verify_show(request):
    '''调用验证码'''
    return render(request,'my_book/verify_show.html')

# 验证码验证
def verify_yz(request):
    '''验证验证码'''
    yzm = request.POST.get('yzm')
    verifycode = request.session['verifycode']
    if yzm != verifycode:
        return HttpResponse('no')
    return HttpResponse(yzm)

# 反向解析
def fan1(request):
    return render(request,'my_book/fan1.html')
def fan2(request):
    '''视图中重定向反向解析'''
    return redirect(reverse('my_book:fan2', args=(2, 3)))

def fan3(request,a,b):
    '''位置参数'''
    return HttpResponse(a+b)

def fan4(request, id, age):
    '''带关键字参数'''
    return HttpResponse(id+age)