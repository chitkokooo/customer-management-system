from django.contrib import admin
from customers.models import Customer

class CustomerAdmin(admin.ModelAdmin):
	list_display = ('name', 'account', 'information', 'remarks')

admin.site.register(Customer, CustomerAdmin)