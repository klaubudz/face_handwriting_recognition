from django.urls import path

from . import views

app_name = 'faceRecognitionWebsite'
urlpatterns = [
    path('', views.index, name='index'),
    path('groups/', views.groups, name='groups'),
    path('groups/<int:group_id>/', views.groupDetails, name='groupDetails'),
    path('people/', views.people, name='people'),
    path('people/<int:person_id>', views.personDetails, name='personDetails'),
    path('lists/', views.lists, name='lists'),
    path('lists/<int:attendance_id>/', views.listDetails, name='listDetails'),
    path('subjects/', views.subjects, name='subjects'),
    path('subjects/<int:subject_id>/', views.subjectDetails, name='subjectDetails'),
    path('grades/', views.grades, name='grades'),
]
