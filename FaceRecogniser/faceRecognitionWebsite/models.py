from django.db import models
from django.contrib.postgres.fields import ArrayField

class Group(models.Model):
	name = models.CharField(max_length=100)
	#students = models.ManyToManyField(Person, verbose_name = "list of students in the group")

	def __str__(self):
		return self.name

class Subject(models.Model):
	name = models.CharField(max_length=100)
	#groups_ids = ArrayField(models.IntegerField())
	groups = models.ManyToManyField(Group, verbose_name = 'groups')

	def __str__(self):
		return self.name

class Person(models.Model):
	#group = models.ForeignKey(
	#	Group, on_delete=models.SET_NULL, blank=True, null=True)
	groups = models.ManyToManyField(Group, verbose_name = 'groups')
	name = models.CharField(max_length=100)
	surname = models.CharField(max_length=100)
	encoding = ArrayField(models.FloatField())

	def __str__(self):
		return "{} {}".format(self.name, self.surname)
	class Meta:
		verbose_name_plural = 'People'

class Grade(models.Model):
	number = models.FloatField()
	subject = models.ForeignKey(
		Subject, on_delete=models.CASCADE, blank=False, null=False)
	person = models.ForeignKey(
		Person, on_delete=models.CASCADE, blank=False, null=False)
	description = models.CharField(max_length=150)
	date = models.DateTimeField('date', null=True)

	def __str__(self):
		return str(self.number)

class Attendance(models.Model):
	group = models.ForeignKey(
		Group, on_delete=models.SET_NULL, blank=True, null=True)
	date = models.DateTimeField('date')
	#members_ids = ArrayField(models.IntegerField())
	members = models.ManyToManyField(Person, verbose_name = 'members')

	def __str__(self):
		return "{} {}".format(self.group.name, self.date)
