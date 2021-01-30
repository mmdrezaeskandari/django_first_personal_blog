from django.urls import path
from . import views

app_name = 'basic_app'

urlpatterns = [
    path('', views.SchoolList.as_view(), name = 'list'),
    path('<int:pk>/', views.SchoolDetail.as_view(), name = 'detail'),
    path('create/', views.SchoolCreate.as_view(), name = 'create'),
    path('update/<int:pk>/', views.SchoolUpdate.as_view(), name = 'update'),
    path('delete/<int:pk>/', views.SchoolDelete.as_view(), name = 'delete'),
]
