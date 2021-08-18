from .models import Student, Subject, Marks
from celery import shared_task
from django.core.mail import send_mail
from student_manager.settings import EMAIL_HOST_USER

def send_mail_to(subject, message, receivers):
    send_mail(subject,message,EMAIL_HOST_USER,[receivers],fail_silently= False)

@shared_task
def report_card_calculator(first_name,last_name):
	student_qs = Student.objects.filter(first_name = first_name, last_name = last_name)
	marks_qs = Marks.objects.filter(student = student_qs[0])
	total_marks = 100*len(marks_qs)
	obtained_marks = 0.0
	for i in marks_qs:
		obtained_marks+=i.mark
	percentage = obtained_marks/total_marks * 100	
	subject= 'Report Card'
	message= first_name+last_name + ' Your Report Card'
	receiver= student_qs[0].email
	task = send_mail_to(subject,message,receivers)
	return task
