from django.contrib import admin
from .models import Category, blogs

class CategoryAdmin(admin.ModelAdmin):
    list_display=('id', 'category_name', 'created_at', 'updated_at')
    search_fields=('id', 'category_name')

class blogAdmin(admin.ModelAdmin):
    list_display=('id', 'title', 'author', 'blog_image', 'short_discription', 'staus', 'created_at', 'updated_at')
    search_fields=('id','title','category__category_name', 'status')


admin.site.register(Category, CategoryAdmin)
admin.site.register(blogs, blogAdmin )
