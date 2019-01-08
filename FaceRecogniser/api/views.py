import os
import face_recognition
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer
from api.serializers import GroupSerializer, PersonSerializer, AttendanceSerializer, SubjectSerializer, GradeSerializer
from faceRecognitionWebsite.models import Group, Person, Attendance, Subject, Grade


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class GroupMembersViewSet(viewsets.ModelViewSet):
    serializer_class = PersonSerializer

    def get_queryset(self):
        people = Person.objects.filter(groups__in = [self.kwargs['group_id']])
        return people


class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer


class AttendancePostView(APIView):

    renderer_classes = (JSONRenderer, )

    def post(self, request):
        member_id = request.data['member_id']
        attendance_id = request.data['attendance_id']
        attendance = Attendance.objects.get(id=attendance_id)
        attendance.members.add(member_id)
        attendance.save()
        return Response(status=200)

class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

class GradeViewSet(viewsets.ModelViewSet):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer      

class FileUploadView(APIView):
    renderer_classes = (JSONRenderer, )

    def post(self, request, format=None):
        file_obj = request.FILES['file']
        file_name = file_obj.name

        with open(file_name, 'wb+') as destination:
            for chunk in file_obj.chunks():
                destination.write(chunk)

        img = face_recognition.load_image_file(file_name)
        encodings = face_recognition.face_encodings(img)
        if not encodings:
            response = {"error": True, "message": "No face detected"}
        elif len(encodings) > 1:
            response = {"error": True, "message": "Too many faces"}
        else:
            response = {"error": False, "encoding": encodings[0]}
        os.remove(file_name)
        return Response(response)
