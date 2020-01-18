from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader, RequestContext
from booktest.models import BookInfo


def my_render(request, template_path, context_dict={}):
    # 加载模板文件
    temp = loader.get_template(template_path)

    # 定义模板上下文对象，给模板传递参数
    context = RequestContext(request, context_dict)

    # 渲染
    res_html = temp.render(context.flatten())

    return HttpResponse(res_html)


# Create your views here.
def index(request):
    # 进行处理和M & T 进行交互
    # return HttpResponse('草泥马')
    # return my_render(request, 'booktest/index.html')
    return render(request, 'booktest/index.html', {'Jason': 'Zhipeng'})


def subpage(request):
    return HttpResponse('Hello Python')


def show_books(request):
    '''显示图书信息'''
    books = BookInfo.objects.all()
    return render(request, 'booktest/show_books.html', {'books': books})


def detail(request, bid):
    '''图书详细'''
    book = BookInfo.objects.get(id=bid)
    heros = book.heroinfo_set.all()
    return render(request, 'booktest/detail.html', {'book': book, 'heros': heros})
