from django.contrib.auth.models import User, Group
from django.shortcuts import render
from rest_framework import permissions
from rest_framework import viewsets, renderers
from rest_framework.decorators import action
from rest_framework.response import Response

from accounts.models import User, School, Company, JobTitle, Hometown, Location
from accounts.serializers import GroupSerializer, UserSerializer, SchoolSerializer, CompanySerializer, \
    JobTitleSerializer, HometownSerializer, LocationSerializer
from data.models import Food


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    # permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'username'


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


def dashboard(request):
    context = {'foods': Food.objects.all(),
               'users': User.objects.all()}
    return render(request, 'users/drf.html', context)


class SchoolViewSet(viewsets.ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    # lookup_field = 'name'


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class JobTitleViewSet(viewsets.ModelViewSet):
    queryset = JobTitle.objects.all()
    serializer_class = JobTitleSerializer


class HometownViewSet(viewsets.ModelViewSet):
    queryset = Hometown.objects.all()
    serializer_class = HometownSerializer


class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
