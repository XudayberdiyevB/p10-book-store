from django.contrib import admin

from books.models import Book, BookAuthor, Category, Tag, WishList


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(BookAuthor)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(WishList)
