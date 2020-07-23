from django.urls import path, include
from . import views

app_name = "customers"
urlpatterns = [
	# path('', views.index, name="index"),
	path('', views.CustomerListView.as_view(), name="customer-list"),
	path('<int:pk>/', views.CustomerDetialView.as_view(), name="customer-detail"),

	path('create/', views.CustomerCreate.as_view(), name='customer-create'),
	path('<int:pk>/update/', views.CustomerUpdate.as_view(), name='customer-update'),
	path('<int:pk>/delete/', views.CustomerDelete.as_view(), name='customer-delete'),

	path('csv/', views.export_as_csv, name="export-csv"),
    path('pdf/', views.export_as_pdf , name="export-pdf"),
]