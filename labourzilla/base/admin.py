from django.contrib import admin
from .models import Freelancer, Skill, Job

admin.site.register(Skill)
admin.site.register(Freelancer)
admin.site.register(Job)