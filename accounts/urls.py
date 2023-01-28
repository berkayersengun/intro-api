from django.urls import include, path
from rest_framework import routers

from accounts import views
from accounts.views import UserViewSet, SchoolViewSet, CompanyViewSet, JobTitleViewSet, \
    HometownViewSet, LocationViewSet

router = routers.DefaultRouter(trailing_slash=False)
router.register('users', UserViewSet)
router.register('school', SchoolViewSet)
router.register('company', CompanyViewSet)
router.register('jobtitle', JobTitleViewSet)
router.register('hometown', HometownViewSet)
router.register('location', LocationViewSet)
# router.register('groups', GroupViewSet)

urlpatterns = [
    path('accounts/', include(router.urls)),
    path('dash', views.dashboard, name='dashboard'),
]