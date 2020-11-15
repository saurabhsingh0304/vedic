from django.db import models
from django.conf import settings

# Create your models here.


class Student(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
	date_of_birth = models.DateField(blank=True, null=True)
	#photo = models.ImageField(upload_to='users/%Y/%m/%d/',
    #                       blank=True)

	def __str__(self):
	    return 'Profile	for	user {}'.format(self.user.username)


class Question(models.Model):
    text = models.TextField(blank=True,)
    image = models.ImageField(blank=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
