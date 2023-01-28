from django.contrib.auth.models import Group
from rest_framework import serializers

from accounts.models import User, Company, School, JobTitle, Hometown, Location


class UserSerializer(serializers.ModelSerializer):
    nationality = serializers.SlugRelatedField(
        queryset=Hometown.objects.all(),
        slug_field='nationality'
    )
    hometown = serializers.SlugRelatedField(
        queryset=Hometown.objects.all(),
        slug_field='country'
    )
    location = serializers.SlugRelatedField(
        queryset=Location.objects.all(),
        slug_field='city'
    )
    job_title = serializers.SlugRelatedField(
        queryset=JobTitle.objects.all(),
        slug_field='name'
    )
    company = serializers.SlugRelatedField(
        queryset=Company.objects.all(),
        slug_field='name'
    )
    school = serializers.SlugRelatedField(
        queryset=School.objects.all(),
        slug_field='name'
    )

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user

    def update(self, instance, validated_data):
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)
        return super(UserSerializer, self).update(instance, validated_data)

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'gender',
            'age',
            'weight',
            'height',
            'birth_date',
            'marital_status',
            'nationality',
            'hometown',
            'location',
            'school',
            'education_level',
            'company',
            'job_title',
            'zodiac',
            'smoke',
            'bio',
            'religion',
            'politics',
            'password'
        ]


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(
        max_length=100,
        style={'placeholder': 'Email', 'autofocus': True}
    )
    password = serializers.CharField(
        max_length=100,
        style={'input_type': 'password', 'placeholder': 'Password'}
    )
    remember_me = serializers.BooleanField()


class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = '__all__'


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


class JobTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobTitle
        fields = '__all__'


class HometownSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hometown
        fields = '__all__'


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'
