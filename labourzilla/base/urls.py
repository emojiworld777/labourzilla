from django.urls import path
from .views import *
urlpatterns = [
    path('', home, name='home'),
    path('login/', user_login, name='login'),
    path('jobs/', job_list, name='jobList'),
    path('signup/', public_signup, name='signup'),
    path('howitworks/', howitworks, name='howitworks'),
    path('post/', postproject, name='postproject')
]
