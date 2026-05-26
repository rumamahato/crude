from django.urls import path
from .import views

urlpatterns = [
    path('', views.form, name='form'),
    path('home/', views.home, name='home'),
    path('edit/<int:id>/', views.edit, name='edit'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('recycle/', views.recycle, name='recycle'),    
    path('restore/<int:id>/', views.restore, name='restore'),
    path('restore/<int:id>/', views.restore, name='restore'),
    path('permanent-delete/<int:id>/', views.permanent_delete, name='permanent_delete'),
  
]