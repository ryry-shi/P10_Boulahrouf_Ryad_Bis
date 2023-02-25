from django.contrib import admin
from .models import Contributors, Projects, Issue

class ProjectAdmin(admin.ModelAdmin):

    list_display = ('username', 'password')

class IssueAdmin(admin.ModelAdmin):

    list_display = ("title", "tag")

class ContributorAdmin(admin.ModelAdmin):

    list_display = ("role")

class Issues(admin.ModelAdmin):

    list_display = ("title", "tag")


admin.site.register(Projects)
admin.site.register(Contributors)
admin.site.register(Issue)