from datetime import date

from django.shortcuts import render, redirect
from booktest.models import BookInfo, HeroInfo
from django.http import HttpResponse, HttpResponseRedirect


# Create your views here.
def index(request):
    '''show book information'''
    books = BookInfo.objects.all()

    return render(request, 'booktest/index.html', {'books': books})


def create(request):
    '''adding one more book'''
    b = BookInfo()
    b.btitle = 'New Book'
    b.bpub_date = date(1992, 12, 1)
    b.save()

    return HttpResponseRedirect('/index')


def delete(request, bid):
    book = BookInfo.objects.get(id=bid)
    book.delete()

    return redirect('/index')
