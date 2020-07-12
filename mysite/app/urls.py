from django.urls import path
from . import views

urlpatterns = [path('', views.index, name=" "),
               path('add/<int:id>', views.add_new_program, name="program")]
