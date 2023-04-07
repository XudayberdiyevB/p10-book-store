from django.contrib import admin

from .models import Book, BookAuthor, Category

admin.site.register(BookAuthor)
admin.site.register(Book)
admin.site.register(Category)
