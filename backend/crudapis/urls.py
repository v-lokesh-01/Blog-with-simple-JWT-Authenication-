from django.urls import path
from .views import * 


urlpatterns = [
    path('list/', BlogList.as_view()),
    path('create/', BlogCreate.as_view()),
    path('delete/<int:pk>/',BlogDelete.as_view()),
]