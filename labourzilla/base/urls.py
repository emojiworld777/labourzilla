from django.urls import path
from .views import *
urlpatterns = [
    path('', home, name='home'),
    path('login/', user_login, name='login'),
    path('jobs/', job_list, name='jobList'),
    path('publicsignup/', public_signup, name='pubsignup'),
    path('howitworks/', howitworks, name='howitworks'),
    path('post/', postproject, name='postproject'),
    path('workersignup/', worker_signup, name='worksignup'),
    path('account/', update_account, name='account'),
    path('jobs/<id>', bid, name='bid'),
    path('projects/',projectlist, name='projects'),
    path('projects/<id>', bidlist, name='bidlist'),
    path('logout/', user_logout, name='logout')
]
