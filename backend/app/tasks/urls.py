from django.urls import path
from .views import AllTasksView, TaksRetrieveView, TaskCreateView,TaskDeleteView, TaskUpdateView

urlpatterns = [
    path('tasks/', AllTasksView.as_view()),
    path('tasks/<int:pk>/', TaksRetrieveView.as_view(), name="detailTask"),
    path('tasks/create/', TaskCreateView.as_view(), name="createTask"),
    path('tasks/<int:pk>/delete/', TaskDeleteView.as_view(), name="deleteTask"),
    path('tasks/<int:pk>/update/', TaskUpdateView.as_view(), name="updateTask"),
]
