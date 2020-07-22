from django.urls import path
from . import views

urlpatterns = [
    path('', views.advertisement_list, name='advertisement_list'),
    path('advertisement/', views.advertisement_details, name='advertisement_details'),
    path('contacts/', views.contacts, name='contacts'),
    path('about/', views.about, name='about'),
    path('categories/', views.categories, name='categories'),
    path('regions/', views.RegionsView.as_view(), name='regions'),
]
