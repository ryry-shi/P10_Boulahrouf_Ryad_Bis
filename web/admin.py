from django.contrib import admin
from .models import Contributors, Projects, Issue, Comment


class ProjectAdmin(admin.ModelAdmin):
    list_display = ("username", "password")


class IssueAdmin(admin.ModelAdmin):
    list_display = ("title", "tag")


class ContributorAdmin(admin.ModelAdmin):
    list_display = ("role", "project_id")


class IssueAdmin(admin.ModelAdmin):
    list_display = ("title", "tag")


class CommentAdmin(admin.ModelAdmin):
    list_display = "description"


admin.site.register(Projects)
admin.site.register(Contributors)
admin.site.register(Issue)
admin.site.register(Comment)
