from django.db import models
from django.contrib.auth.models import User
from phone_field import PhoneField

# Create your models here.
class Comapany(models.Model):
    address = models.CharField(max_length=100)
    contacts = PhoneField(unique=True)
    website = models.URLField(null=True, blank=True,unique=True)
    company_type = models.CharField(max_length=100, blank=True,null=True)
    description = models.TextField(blank=True,null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class Job(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True,null=True)
    image = models.ImageField(upload_to='image/', null=True, blank=True)
    company = models.ForeignKey(Comapany, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


