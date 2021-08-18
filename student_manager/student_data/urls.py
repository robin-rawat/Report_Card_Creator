from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StudentDataSubmitView, MarksViewSet, StudentViewSet, SubjectViewSet, get_status

app_name = 'student_data'

router = DefaultRouter()
router.register(r'marks', MarksViewSet, basename='marks')
router.register(r'student', StudentViewSet, basename='student')
router.register(r'subject', SubjectViewSet, basename='subject')

urlpatterns = [
    path('', StudentDataSubmitView.as_view(), name = 'home'),
    path('task/<str:task_id>/', get_status, name='task'),
    path('api/', include(router.urls)),
    
]