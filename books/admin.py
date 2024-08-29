from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Book)
class BooksAdmin(admin.ModelAdmin):
    pass



@admin.register(Comment)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ('user', 'book', 'text' , 'datetime_created' , 'is_active' , 'recommend' ,)