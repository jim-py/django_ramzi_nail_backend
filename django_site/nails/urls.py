from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('courses', courses, name='courses'),
    path('login', log_in, name='login'),
    path('registration', registration, name='registration'),
    path('logout', log_out, name='logout'),
    path('profile/<int:pk>', profile, name='profile'),
    path('enroll/<int:pk_user>/<int:pk_timesheet>', enroll, name='enroll'),
    path('delete_enroll/<int:pk_user>/<int:pk_request>', delete_enroll, name='delete_enroll'),
]
