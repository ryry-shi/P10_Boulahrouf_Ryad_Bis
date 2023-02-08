from django.contrib import admin
from .models import Projects

class ProjectsAdmin(admin.ModelAdmin):

    list_display = ('username', 'password')

admin.site.register(Projects)
# Register your models here.
