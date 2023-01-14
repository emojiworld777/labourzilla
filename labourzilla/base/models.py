from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Worker(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length= 255)
    mobile = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return self.name

class Public(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    mobile = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return self.name

class Jobs(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=500)
    support_file = models.FileField(upload_to='uploads')
    min_price = models.PositiveIntegerField()
    max_price = models.PositiveIntegerField()
    category = models.CharField(max_length = 50)

    def __str__(self):
        return self.title

class Bid(models.Model):
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE)
    job = models.ForeignKey(Jobs, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()
    def __str__(self):
        return self.job.title

