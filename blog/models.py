from django.db import models
from django.utils import timezone

# Create your models here.

class post(models.Model):
	title = models.CharField(max_length=50)
	text=models.TextField()
	create_date = models.DateTimeField(default = timezone.now)
	pyblished_date = models.DateTimeField(null = True, blank=True)

	def publish(self):
		self.publish_date = timezone.now()