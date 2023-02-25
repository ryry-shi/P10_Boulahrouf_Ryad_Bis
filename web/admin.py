from django.contrib import admin
from .models import Contributors, Projects

class ProjectAdmin(admin.ModelAdmin):

    list_display = ('username', 'password')

class IssueAdmin(admin.ModelAdmin):

    list_display = ("title", "tag")

class ContributorAdmin(admin.ModelAdmin):

    list_display = ("role", "project_id", "user_id")


admin.site.register(Projects)
admin.site.register(Contributors)
