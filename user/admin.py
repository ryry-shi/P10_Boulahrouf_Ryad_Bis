from django.contrib import admin
from user.models import MyUser


class MyUserAdmin(admin.ModelAdmin):
    list_display = ("username", "password")


admin.site.register(MyUser)

# Register your models here.
