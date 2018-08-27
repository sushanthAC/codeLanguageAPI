from django.db import models

class Language(models.Model):
	name = models.CharField(max_length=25)
	paradigm = models.CharField(max_length=25)

	def __str__(self):
		return self.name
