from .models import Event, Participant
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
                  'location',
                  'collaborators',
                  'participants')


class EventSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('pk', 'title')


class ParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participant
