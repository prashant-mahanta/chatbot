from django.db import models
from datetime import datetime
# Create your models here.

def user_directory_path(instance, filename):
    name, extension = filename.split('.')
    return '{0}.{1}'.format(name, extension)
class Messages(models.Model):
	text = models.TextField(blank = True, null=True)
	file = models.FileField(blank=True, null=True)
	created_at = models.DateTimeField(default=datetime.now, blank=False)

	def __str__(self):
		if self.text != None:
			return self.text
		else:
			return self.file

