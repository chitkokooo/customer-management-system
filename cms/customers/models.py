from django.db import models

class Customer(models.Model):
	name = models.CharField(max_length=200)
	account = models.CharField(max_length=200)
	information = models.TextField()
	info_created_at = models.DateTimeField(auto_now_add=True)
	info_updated_at = models.DateTimeField(auto_now=True)
	remarks = models.TextField()

	def __str__(self):
		return self.name

