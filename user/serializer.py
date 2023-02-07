from .models import MyUser
from rest_framework import serializers
from django.contrib.auth.hashers import (
    make_password,
)

class MyUserSerializer(serializers.ModelSerializer):

    class Meta:

        model = MyUser
        fields = ['username', 'password']

    def create(self, validated_data):
        user = MyUser.objects.create(
            username=validated_data["username"],
            password=make_password(validated_data["password"]),
        )
        user.save()
        return user