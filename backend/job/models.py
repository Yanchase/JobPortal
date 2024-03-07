from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.gis.db import models as gismodels
from django.contrib.gis.geos import Point
from datetime import *
from django.contrib.auth.models import User
import geocoder
import os

# Create your models here.

def return_date_time():
    now = datetime.now()
    return now + timedelta(days = 10)

class JobType(models.TextChoices):
    Permanent = 'Permanent'
    Temporary = 'Temporary'
    Intership = 'Intership'

class Education(models.TextChoices):
    Bachlor = 'Bachlor'
    Master = 'Master'
    Phd = 'Phd'

class Industry(models.TextChoices):
    Business = 'Business'
    Banking = 'Banking'
    IT = 'Information Technology'
    Education = 'Education/Training'
    Telecommunication = 'Telecommunication'
    Others = 'Others'

class Experience(models.TextChoices):
    NO_EXPERIENCE = 'No experience'
    ONE_YEAR = '1 Years'
    TWO_YEAR = '2 Years'
    THREE_YEAR_PLUS = '3 Years Above' 

class Job(models.Model):
    title = models.CharField(max_length = 100, null = True)
    description = models.TextField(null = True)
    email = models.EmailField(null = True)
    address = models.CharField(max_length = 200, null = True)
    jobType = models.CharField(max_length = 10, choices = JobType.choices, default = JobType.Permanent)
    education = models.CharField(max_length = 100, choices = Education.choices, default = Education.Bachlor)
    industry = models.CharField(max_length = 100, choices = Industry.choices, default = Industry.Business)
    experience = models.CharField(max_length = 20, choices = Experience.choices, default = Experience.NO_EXPERIENCE)
    salary = models.IntegerField(default = 1, validators = [MinValueValidator(1), MaxValueValidator(1000000)])
    position = models.IntegerField(default = 1)
    company = models.CharField(max_length=20, null=True)
    point = gismodels.PointField(default = Point(0.0,0.0))
    lastDate = models.DateTimeField(default = return_date_time)
    user = models.ForeignKey(User, on_delete = models.SET_NULL, null = True)
    createAt = models.DateTimeField(auto_now_add = True)

def save(self, *args, **kwargs): 
    g = geocoder.mapquest(self.address, key = os.environ.get('GEOCODER_API')) 
    print(g)
    lng = g.lng
    lat= g.lat
    self.point = Point(lng,lat)
    super(Job, self).save(*args, **kwargs)