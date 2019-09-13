from django.urls import path
from . import views
urlpatterns =[
    path('create/', views.create, name='create'),
    path('skill_create', views.skill_store, name='skill_store'),
    path('skill/delete/<int:x>',views.remove, name='skill_delete')

]