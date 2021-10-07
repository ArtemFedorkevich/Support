from django.urls import path
from . import views
app_name = 'staff_part'
urlpatterns = [
    path('problemsforstaff/<int:pk>/', views.PostListStaff.as_view()),
    path('problemsforstaffindetail/<int:pk>/', views.PostDetailListStaff.as_view()),
]