from django.db import models
from phone_field import PhoneField
from django.contrib.auth.models import User

# Create your models here.
gender = (('male', 'Male'), ('female', 'Female'), ('others', 'Other'))
class Jobseeker(models.Model):
    address = models.CharField(max_length=100)
    experience_year = models.IntegerField(default=0, null=True, blank=True)
    cv = models.FileField(upload_to='cv/')
    profile = models.ImageField(upload_to='profile/')
    professional_title = models.CharField(max_length=100, null=True, blank=True)
    contact_number = PhoneField(blank=True, null=True, unique=True)
    description = models.TextField(null=True, blank=True, help_text="About yourself")
    url = models.URLField(blank=True, null=True, unique=True)
    gender = models.CharField(max_length=100, choices=gender)
    qualification = models.CharField(max_length=100, help_text="your highest degree here")
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class Skill(models.Model):
    skill_title =models.CharField(max_length=100,blank=True,null=True)
    proffecency_level = models.IntegerField()
    jobseeker = models.ForeignKey(Jobseeker, on_delete=models.CASCADE)

    def __str__(self):
        return self.skill_title

class Experience(models.Model):
    company = models.CharField(max_length=100)
    post = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    Jobseeker = models.ForeignKey(Jobseeker, on_delete=models.CASCADE)

    def __str__(self):
        return self.jobseeker.user.username

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    link = models.URLField(null=True,blank=True,unique=True)
    Jobseeker = models.ForeignKey(Jobseeker, on_delete=models.CASCADE)

    def __str__(self):
        return self.Jobseeker.user.username

