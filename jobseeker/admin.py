from django.contrib import admin
from .models import Jobseeker,Skill,Experience,Project

# Register your models here.
admin.site.register(Jobseeker)
admin.site.register(Skill)
admin.site.register(Experience)
admin.site.register(Project)
