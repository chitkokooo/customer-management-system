from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from customers.models import Customer

def index(request):
	customers = Customer.objects.all()
	return render(request, 'customers/index.html', {'customers': customers})


class CustomerListView(LoginRequiredMixin, generic.ListView):
	model = Customer


class CustomerDetialView(LoginRequiredMixin, generic.DetailView):
	model = Customer


class CustomerCreate(PermissionRequiredMixin, CreateView):
	permission_required = 'customer.can_add'
	model = Customer
	fields = '__all__'


class CustomerUpdate(PermissionRequiredMixin, UpdateView):
	permission_required = 'customer.can_change'
	model = Customer
	fields = ['name', 'account', 'information', 'remarks']


class CustomerDelete(PermissionRequiredMixin, DeleteView):
	permission_required = 'customer.can_delete'
	model = Customer
	success_url = reverse_lazy('customers:customer-list')