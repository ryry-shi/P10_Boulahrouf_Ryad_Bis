from django.contrib import admin
from django.urls import path, include
from rest_framework_nested import routers
from user.views import MyUserAPIView

from web.views import ContributorAPIView, ProjectAPIView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = routers.SimpleRouter()
router.register(r'projects', ProjectAPIView, basename="test")

project_router = routers.NestedSimpleRouter(router, r'projects', lookup='projects')
project_router.register(r'users', ContributorAPIView, basename="users")
router.register('signup', MyUserAPIView, basename='signup')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', include(router.urls)),
    path('', include(project_router.urls)),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
