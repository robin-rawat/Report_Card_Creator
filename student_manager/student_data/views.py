from django.shortcuts import render
from rest_framework import viewsets
from django.views.generic.edit import FormView
from django.contrib import messages
from django.shortcuts import redirect
from django.http import JsonResponse
from celery.result import AsyncResult
from .serializers import MarksSerializer, StudentSerializer, SubjectSerializer
from .models import Student, Subject, Marks
from .forms import StudentInputForm
from .tasks import report_card_calculator
# Create your views here.

class StudentDataSubmitView(FormView):
	template_name = 'base.html'
	form_class = StudentInputForm
	def form_valid(self,form):
		first_name = form.cleaned_data.get('first_name')
		last_name = form.cleaned_data.get('last_name')
		print(first_name+last_name)
		task = report_card_calculator.delay(first_name, last_name)
		return JsonResponse({"task_id": task.id}, status=202)

def get_status(request, task_id):
    task_result = AsyncResult(task_id)
    result = {
        "task_id": task_id,
        "task_status": task_result.status,
        "task_result": task_result.result
    }
    return JsonResponse(result, status=200)

class MarksViewSet(viewsets.ModelViewSet):
	queryset = Marks.objects.all()
	serializer_class =  MarksSerializer

class StudentViewSet(viewsets.ModelViewSet):
	queryset = Student.objects.all()
	serializer_class = StudentSerializer

class SubjectViewSet(viewsets.ModelViewSet):
	queryset = Subject.objects.all()
	serializer_class = SubjectSerializer