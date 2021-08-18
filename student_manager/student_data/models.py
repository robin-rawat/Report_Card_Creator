from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Student(models.Model):
	#student = models.OneToOneField(User, on_delete=models.CASCADE)
	first_name = models.TextField(default="Bot")
	last_name = models.TextField(default="Man")
	email = models.EmailField(max_length = 254,blank=False,unique=True)

	class Meta:
		unique_together = ("first_name", "last_name")

	def __str__(self):
		return self.first_name + " " + self.last_name

class Subject(models.Model):
	name = models.CharField(max_length=30, unique = True)
	def __str__(self):
		return self.name

class Marks(models.Model):
	student = models.ForeignKey(Student, on_delete=models.CASCADE)
	subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
	mark = models.FloatField()

	class Meta:
		unique_together = ("student", "subject")

	def __str__(self):
		return self.student.first_name + "/" + self.subject.name + "/" + str(self.mark) 

