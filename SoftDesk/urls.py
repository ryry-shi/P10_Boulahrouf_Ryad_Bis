from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from user.views import MyUserAPIView

from web.views import ProjectAPIView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = routers.SimpleRouter()

router.register('signup', MyUserAPIView, basename='signup')
router.register('projects', ProjectAPIView, basename='project')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', include(router.urls)),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
