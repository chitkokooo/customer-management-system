import csv
from django import forms
from django.core.exceptions import ValidationError


class CSVUploadFileForm(forms.Form):
	csv_file = forms.FileField(label="Select a CSV file with valid format to import data.", widget=forms.FileInput(attrs={'accept':'.csv', 'class': 'form-control'}))