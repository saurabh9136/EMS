from django.contrib import admin
from django.urls import include, path
from .views import *
urlpatterns = [
    path('home/', emp_home),
    path('add-emp/', add_emp),
    path('delete-emp/<int:id>', delete_emp), 
    path('update-emp/<int:id>', update_emp),
    path('do-update-emp/<int:id>', do_update_emp)
]