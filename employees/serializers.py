from .models import Employee, Location, Role
from rest_framework import serializers


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        depth = 1
        fields = ('pk',
                  'username',
                  'email',
                  'first_name',
                  'last_name',
                  'location',
                  'skype_id',
                  'avatar',
                  'base_profile_complete',
                  'last_month_score',
                  'last_year_score',
                  'current_month_score',
                  'current_year_score',
                  'level',
                  'total_score',
                  'is_active',
                  'last_login')


class EmployeeCreationSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=100)


class EmployeeCreationListSerializer(serializers.Serializer):
    password = serializers.CharField(max_length=20)
    emails = serializers.ListField(
        child=serializers.CharField(max_length=100)
    )


class EmployeeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('pk',
                  'username',
                  'email',
                  'first_name',
                  'last_name',
                  'level',
                  'avatar',
                  'total_score',
                  'last_month_score',
                  'last_year_score',
                  'current_month_score',
                  'current_year_score')


class EmployeeLocationListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('pk', 'name', 'icon')


class EmployeeRoleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ('pk', 'name')


class EmployeeTopListSerializer(serializers.Serializer):
    pk = serializers.IntegerField()
    username = serializers.CharField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    avatar = serializers.CharField()
    value = serializers.IntegerField()


class EmployeeTopTotalScoreList(serializers.ModelSerializer):
    value = serializers.IntegerField(source='total_score')

    class Meta:
        model = Employee
        fields = ('pk', 'username', 'first_name', 'last_name', 'avatar', 'value')


class EmployeeTopLevelList(serializers.ModelSerializer):
    value = serializers.IntegerField(source='level')

    class Meta:
        model = Employee
        fields = ('pk', 'username', 'first_name', 'last_name', 'avatar', 'value')


class EmployeeTopCurrentMonthList(serializers.ModelSerializer):
    value = serializers.IntegerField(source='current_month_score')

    class Meta:
        model = Employee
        fields = ('pk', 'username', 'first_name', 'last_name', 'avatar', 'value')


class EmployeeTopCurrentYearList(serializers.ModelSerializer):
    value = serializers.IntegerField(source='current_year_score')

    class Meta:
        model = Employee
        fields = ('pk', 'username', 'first_name', 'last_name', 'avatar', 'value')


class EmployeeTopLastMonthList(serializers.ModelSerializer):
    value = serializers.IntegerField(source='last_month_score')

    class Meta:
        model = Employee
        fields = ('pk', 'username', 'first_name', 'last_name', 'avatar', 'value')


class EmployeeTopLastYearList(serializers.ModelSerializer):
    value = serializers.IntegerField(source='last_year_score')

    class Meta:
        model = Employee
        fields = ('pk', 'username', 'first_name', 'last_name', 'avatar', 'value')


class EmployeeAvatarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('pk', 'avatar')


class EmployeeAuthenticationResponse(serializers.Serializer):
    token = serializers.CharField(max_length=40)
    user_id = serializers.IntegerField()
