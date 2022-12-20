from django.db import models
from django.contrib.auth.models import User

class Skill(models.Model):
    title = models.CharField(max_length=155)

    def __str__(self):
        return self.title

class Freelancer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, default='John Doe')
    title = models.CharField(max_length=255, default='web developer')
    photo = models.FileField(upload_to='media/ProfilePic')
    description = models.TextField(max_length=4000)
    skills = models.ManyToManyField(Skill)
    
    def __str__(self):
        return self.name

class Job(models.Model):
    creater = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    description = models.TextField(max_length=4000)
    file = models.FileField(upload_to='media/JobPost')
    tags = models.ManyToManyField(Skill)
    def __str__(self):
        return self.title