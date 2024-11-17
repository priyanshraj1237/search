from django.urls import path
from . import views

urlpatterns = [
    path('', views.search_page, name='search_page'),  # Home page for the search
    path('search/', views.search_students, name='search_students'),
]

