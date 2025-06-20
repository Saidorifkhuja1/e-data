from django.urls import path
from .views import *



urlpatterns = [
    path('files/create/', FileCreateView.as_view()),
    path('files/<uuid:uid>/', FileRetrieveView.as_view()),
    path('files/<uuid:uid>/update/', FileUpdateView.as_view()),
    path('files/<uuid:uid>/delete/', FileDeleteView.as_view()),
    path('files/user/<uuid:uid>/', FileListByUserAPIView.as_view()),
    path('files/my/', MyFileListAPIView.as_view()),
    path('files/all/', AllFileListAPIView.as_view()),
]
