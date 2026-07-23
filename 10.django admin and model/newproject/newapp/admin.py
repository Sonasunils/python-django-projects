from django.contrib import admin
from .models import Author,Book

# Register your models here.
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display=('name','email','date_of_birth')
    search_fields=('name',)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display=('title','author','published_date','price','available')
    search_fields=('title',)
    
