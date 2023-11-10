from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet, TodecideView

router = DefaultRouter()
router.register(r'task', viewset = TaskViewSet, basename='task')




urlpatterns = [
    path('task_solution/<int:task_id>/', TodecideView.as_view(), name='solution_of_task'),
    path('', include(router.urls)),
]