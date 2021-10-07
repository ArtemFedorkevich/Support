from django.urls import path

from . import views

app_name = 'useractions'
urlpatterns = [
    path('problems/', views.PostList.as_view()),
    path('problemindetail/<int:pk>/', views.PostDetailList.as_view()),
]
