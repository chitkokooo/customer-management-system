import csv
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from customers.models import Customer
"""
def index(request):
	customers = Customer.objects.all()
	return render(request, 'customers/index.html', {'customers': customers})
"""

class CustomerListView(LoginRequiredMixin, generic.ListView):
	model = Customer


class CustomerDetialView(LoginRequiredMixin, generic.DetailView):
	model = Customer


class CustomerCreate(PermissionRequiredMixin, CreateView):
	permission_required = 'customers.can_manage_customers'
	model = Customer
	fields = '__all__'


class CustomerUpdate(PermissionRequiredMixin, UpdateView):
	permission_required = 'customers.can_manage_customers'
	model = Customer
	fields = ['name', 'account', 'information', 'remarks']


class CustomerDelete(PermissionRequiredMixin, DeleteView):
	permission_required = 'customers.can_manage_customers'
	model = Customer
	success_url = reverse_lazy('customers:customer-list')


@login_required
def export_as_csv(request):
	customers = Customer.objects.all()
	if customers.count() == 0:
		return redirect(reverse('customers:customer-list'))

	response_data = HttpResponse(content_type='text/csv')
	response_data['Content-Disposition'] = 'attachment; filename="customer_list.csv"'
	csv_headers = ['Name', 'Account', 'Information', 'Remarks']
	writer = csv.writer(response_data)
	writer.writerow(csv_headers)
	for customer in customers:
		csv_data = [customer.name, customer.account, customer.information, customer.remarks]
		writer.writerow(csv_data)
	return response_data