from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from customers.models import Customer

def index(request):
	customers = Customer.objects.all()
	return render(request, 'customers/index.html', {'customers': customers})


class CustomerListView(LoginRequiredMixin, generic.ListView):
	model = Customer


class CustomerDetialView(LoginRequiredMixin, generic.DetailView):
	model = Customer