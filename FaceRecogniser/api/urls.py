from django.conf.urls import url, include
from rest_framework import routers
from api.views import GroupViewSet, GradeViewSet, FileUploadView, GroupMembersViewSet, AttendanceViewSet, AttendancePostView, PersonViewSet, SubjectViewSet

router = routers.DefaultRouter()
router.register(r'groups', GroupViewSet)
router.register(r'attendances', AttendanceViewSet)
router.register(r'groups/members/(?P<group_id>[0-9]+)', GroupMembersViewSet,"people")
router.register(r'people', PersonViewSet)
router.register(r'subjects', SubjectViewSet)
router.register(r'grades', GradeViewSet)

urlpatterns = [
    url(r'^attendances/addmember/$', AttendancePostView.as_view()),
    url(r'^upload/$', FileUploadView.as_view()),
    url(r'^', include(router.urls)),
]
