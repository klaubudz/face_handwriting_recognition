from django.contrib import admin

from .models import Group, Person, Attendance, Subject, Grade

admin.site.register(Group)

class PersonAdmin(admin.ModelAdmin):
	fields = ['name', 'surname', 'groups', 'encoding']
	list_display = ('name', 'surname')
	filter_horizontal = ('groups',)
admin.site.register(Person, PersonAdmin)

class AttendanceAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, {'fields': ['group','members']}),
		('Date information', {'fields': ['date']}),
	]
	list_display = ('group', 'date')
	list_filter = ['date']
	filter_horizontal = ('members',)
admin.site.register(Attendance, AttendanceAdmin)

class GradeAdmin(admin.ModelAdmin):
	fields = ['subject', 'description', 'date', 'person', 'number']
	list_display = ('subject', 'description', 'date', 'person', 'number')
admin.site.register(Grade, GradeAdmin)

class SubjectAdmin(admin.ModelAdmin):
	fields = ['name', 'groups']
	list_display = ['name']
	filter_horizontal = ('groups',)
admin.site.register(Subject, SubjectAdmin)
