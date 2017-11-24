# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from store.models import Author, Book


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name')


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'price', 'stock')


admin.site.register(Author,AuthorAdmin)
admin.site.register(Book,BookAdmin)
