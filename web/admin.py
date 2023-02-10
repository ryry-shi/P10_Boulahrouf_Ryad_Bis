from django.contrib import admin
from .models import Projects, Issues

class ProjectsAdmin(admin.ModelAdmin):

    list_display = ('username', 'password')

class IssueAdmin(admin.ModelAdmin):

    list_display = ("title", "tag")

admin.site.register(Projects)
admin.site.register(Issues)
# Register your models here.
