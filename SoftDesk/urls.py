from django.contrib import admin
from django.urls import path, include
from rest_framework_nested import routers
from user.views import MyUserAPIView

from web.views import ContributorAPIView, IssueAPIView, ProjectAPIView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = routers.SimpleRouter()
router.register(r'project', ProjectAPIView, basename="test")
router.register(r'signup', MyUserAPIView, basename='signup')

project_router = routers.NestedSimpleRouter(router, r'project', lookup='project')
project_router.register(r'user', ContributorAPIView, basename="user")
project_router.register(r'issue', IssueAPIView, basename='issue')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', include(router.urls)),
    path('', include(project_router.urls)),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
