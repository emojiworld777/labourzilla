from django.urls import path
from .views import *
urlpatterns = [
    path('', home, name='home'),
    path('login/', user_login, name='login'),
    path('jobs/', job_list, name='jobList'),
    path('publicsignup/', public_signup, name='pubsignup'),
    path('howitworks/', howitworks, name='howitworks'),
    path('post/', postproject, name='postproject'),
    path('workersignup/', worker_signup, name='worksignup')
]
