import csv
import io
from weasyprint import HTML
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from customers.forms import CSVUploadFileForm
from customers.models import Customer


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


@permission_required('customers.can_manage_customers')
def delete_all_customers(request):
	Customer.objects.all().delete()
	return redirect(reverse('customers:customer-list'))


@login_required
def import_as_csv(request):
	if request.method == 'POST':
		form = CSVUploadFileForm(request.POST, request.FILES)
		if form.is_valid():
			#handle_csv_import(request.FILES['csv_file'])
			# return redirect(reverse('customers:customer-list'))
			return HttpResponse(handle_csv_import(request.FILES['csv_file']))
	else:
		form = CSVUploadFileForm()
	return render(request, 'customers/csv_upload_form.html', {'form': form})


def handle_csv_import(csv_file):
	csv_file.seek(0)  # go to starting point
	rows = csv.DictReader(io.StringIO(csv_file.read().decode('utf-8')))
	for row in rows:
		row = ', '.join(row)
		# customer = Customer.objects.create(name=row[1], account=row[2], information=row[3], remarks=row[4])
		# customer.save()



@login_required
def export_as_csv(request):
	customers = Customer.objects.order_by('name')
	if customers.count() == 0:
		return redirect(reverse('customers:customer-list'))

	response_data = HttpResponse(content_type='text/csv')
	response_data['Content-Disposition'] = 'attachment; filename="customer_list.csv"'
	# csv_headers = ['Name', 'Account', 'Information', 'Remarks']
	writer = csv.writer(response_data)
	# writer.writerow(csv_headers)
	for customer in customers:
		csv_data = [customer.name, customer.account, customer.information, customer.remarks]
		writer.writerow(csv_data)
	return response_data


@login_required
def export_as_pdf(request):
	customers = Customer.objects.order_by('name')
	if customers.count() == 0:
		return redirect(reverse('customers:customer-list'))
	# return render(request, 'customers/pdf.html', {'customers': customers})
	html_string = render_to_string('customers/pdf.html', {'customers': customers})
	html = HTML(string=html_string)
	html.write_pdf(target='tmp_storage/customer_list.pdf')
	fss = FileSystemStorage('tmp_storage/')
	with fss.open('customer_list.pdf') as pdf:
		response_data = HttpResponse(pdf, content_type="application/pdf")
		response_data['Content-Disposition'] = 'attachment; filename="customer_list.pdf"'
	return response_data


""" Error pages """

def error_403(request, exception):
	return render(request, '403.html', {})


def error_404(request, exception):
	return render(request, '404.html', {})


def error_500(request):
	return render(request, '500.html', {})
