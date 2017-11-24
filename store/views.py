# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from store.models import Book


def index(request):
    return render(request, 'template.html')


def store(request):
    books = Book.objects.all()
    context = {
        'books':books,
    }
    return render(request,'base.html',context)


def book_details(request, book_id):
    context = {
        'book': Book.objects.get(pk=book_id)
    }
    return render(request,'store/detail.html',context)

