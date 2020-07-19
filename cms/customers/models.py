from django.db import models
from django.urls import reverse

class Customer(models.Model):
	name = models.CharField(max_length=200)
	account = models.CharField(max_length=200)
	information = models.TextField(null=True, blank=True)
	remarks = models.TextField(null=True, blank=True)
	info_created_at = models.DateTimeField(auto_now_add=True)
	info_updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('customers:customer-detail', args=[str(self.id)])

	class Meta:
		permissions = (('can_manage_customers', 'Customer CRUD Operations'),)