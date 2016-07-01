from .models import Event, Participant
from employees.models import Employee
from rest_framework import serializers


class EventSerializer(serializers.ModelSerializer):
    collaborators = serializers.IntegerField(source='num_collaborators')
    participants = serializers.IntegerField(source='num_participants')

    class Meta:
        model = Event
        fields = ('pk',
                  'title',
                  'description',
                  'datetime',
                  'image',
                  'location',
                  'is_registration_open',
                  'collaborators',
                  'participants')


class EventSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('pk', 'title', 'image', 'is_registration_open')


class CollaboratorSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('pk', 'first_name', 'last_name', 'email', 'avatar', 'skype_id')


class EventParticipantListSerializer(serializers.ModelSerializer):
    count = serializers.IntegerField(source='num_participants')

    class Meta:
        model = Event
        depth = 1
        fields = ('pk', 'title', 'image', 'count', 'is_registration_open', 'participants')


class EventCollaboratorListSerializer(serializers.ModelSerializer):
    collaborators = CollaboratorSimpleSerializer(many=True)
    count = serializers.IntegerField(source='num_collaborators')

    class Meta:
        model = Event
        depth = 1
        fields = ('pk', 'title', 'image', 'count', 'is_registration_open', 'collaborators')


class ParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participant
