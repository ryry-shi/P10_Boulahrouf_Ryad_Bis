from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .permission import IsAuthor
from rest_framework import status
from user.serializer import MyUserSerializer

from user.models import MyUser


class MyUserAPIView(viewsets.ModelViewSet):
    permission_classes = [IsAuthor]
    serializer_class = MyUserSerializer
    queryset = MyUser.objects.all()

    def get_queryset(self, *args, **kwargs):
        return MyUser.objects.filter(id=self.request.user.id)


    def post(self, request, *args, **kwargs):
        users_data = request.data
        serializer = self.serializer_class(data=users_data)
        if serializer.is_valid():
            if not MyUser.objects.filter(username=serializer["username"]).exists():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response({'message':'User Already Exists'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


