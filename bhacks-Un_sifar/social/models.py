from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
# Create your models here.
class course(models.Model):
	teacher=models.CharField(max_length=20)
	price=models.IntegerField()
	name=models.CharField(max_length=30)
	logo=models.FileField()
	is_completed=models.BooleanField(default=False)
	description=models.CharField(max_length=50)
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	def __str__(self):
		return self.name
	def get_absolute_url(self):
		return reverse('lecture',kwargs={'pk':self.pk})
class newuser(models.Model):
	user=models.OneToOneField(User,on_delete=models.CASCADE)
	photo=models.FileField()
	rating=models.IntegerField(default=1)
	subscribed=models.ManyToManyField(course)
	mentor=models.BooleanField(default=False)
	def __str__(self):
		return self.user.username
	def is_mentor(self):
		return self.mentor

class reply(models.Model):
	answer=models.TextField()
	date=models.DateTimeField(default=timezone.now)
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	def __str__(self):
		return self.user.username
class problems(models.Model):
	prob=models.TextField()
	reply=models.ManyToManyField(reply)
	date=models.DateTimeField(default=timezone.now)
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	def __str__(self):
		return self.user.username


class lectures(models.Model):
	video=models.FileField()
	name=models.CharField(max_length=100)
	course=models.ForeignKey(course,on_delete=models.CASCADE)
	#para=models.ManyToManyField(practice)
	def __str__(self):
		return self.name