# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from store.models import Author, Book, BookOrder, Cart


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name')


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'price', 'stock')


class BookOrderAdmin(admin.ModelAdmin):
    list_display = ('book', 'cart', 'quantity')


class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'active', 'order_date')


admin.site.register(Author,AuthorAdmin)
admin.site.register(Book,BookAdmin)
admin.site.register(BookOrder,BookOrderAdmin)
admin.site.register(Cart,CartAdmin)


