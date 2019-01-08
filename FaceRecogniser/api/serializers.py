from rest_framework import serializers
from faceRecognitionWebsite.models import Group, Person, Attendance, Subject, Grade


class GroupSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Group
        fields = ('id', 'name')

class PersonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Person
        fields = ('id', 'name', 'surname', 'groups', 'encoding')

class AttendanceSerializer(serializers.ModelSerializer):
    members = PersonSerializer(many=True, read_only=True)
    class Meta:
        model = Attendance
        fields = ('id', 'group', 'date', 'members')

class SubjectSerializer(serializers.ModelSerializer):
    groups = GroupSerializer(many=True, read_only=True)
    class Meta:
        model = Subject
        fields = ('id', 'name', 'groups')

class GradeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Grade
        fields = ('id', 'subject', 'description', 'date', 'person', 'number')
