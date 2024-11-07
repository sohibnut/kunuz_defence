from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(New)
class NewAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'create_at', 'type', 'view_count']
    readonly_fields = ['view_count']
    search_fields = ['title', 'body']


admin.site.register(Category)
admin.site.register(Tag)

@admin.register(Social)
class SocialAdmin(admin.ModelAdmin):
    list_display = ['name', 'link']
    search_fields = ['name']

admin.site.register(AboutUs)
@admin.register(Comments)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'theme', 'tel_number']
    search_fields = ['name', 'theme']

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['name', 'position']
    search_fields = ['name']