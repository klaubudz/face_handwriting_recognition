from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Group, Person, Attendance, Subject, Grade

def index(request):
	return render(request, 'faceRecognitionWebsite/index.html')

def groups(request):
	return render(request, 'faceRecognitionWebsite/groups.html', {
		'subjects': Subject.objects.all()
	})

def groupDetails(request, group_id):
	return render(request, 'faceRecognitionWebsite/groupDetails.html', {
		'group': Group.objects.get(id = group_id),
		'people': Person.objects.filter(groups__in = [group_id]).order_by('surname', 'name')
	})

def people(request):
	return render(request, 'faceRecognitionWebsite/people.html',{
		'people': Person.objects.all().order_by('surname', 'name')
	})

def personDetails(request, person_id):
	person = Person.objects.get(id = person_id)
	subjects = Subject.objects.filter(groups__in = person.groups.all())
	grades = Grade.objects.filter(person = person)
	table = list(map(lambda x: (x, Subject.objects.filter(groups__in = [x])), person.groups.all()))
	return render(request, 'faceRecognitionWebsite/personDetails.html', {
		'person': person,
		'subjects': subjects,
		'grades': grades,
		'table': table
	})

def lists(request):
	return render(request, 'faceRecognitionWebsite/lists.html', {
		'lists': Attendance.objects.all().order_by('date')
	})

def listDetails(request, attendance_id):
	attendance = Attendance.objects.get(id = attendance_id)
	present_people = Person.objects.filter(id__in = attendance.members.all())
	group_members = Person.objects.filter(groups__in = [attendance.group_id]).order_by('surname', 'name')
	not_group_members = ( set(present_people) - set(group_members) )
	return render(request, 'faceRecognitionWebsite/listDetails.html', {
		'list': attendance,
		'not_group_members': not_group_members,
		'group_members': group_members
	})

def subjects(request):
		return render(request, 'faceRecognitionWebsite/subjects.html', {
		'subjects': Subject.objects.all()
	})

def subjectDetails(request, subject_id):
	subject = Subject.objects.get(id = subject_id)
	groups = Group.objects.filter(id__in = subject.groups.all())
	return render(request, 'faceRecognitionWebsite/subjectDetails.html', {
		'subject': subject,
		'groups_assigned': groups
	})

def grades(request):
	grades = Grade.objects.all().order_by('subject', 'description', 'date', 'person', 'number')

	return render(request, 'faceRecognitionWebsite/grades.html', {
		'grades': grades	
	})