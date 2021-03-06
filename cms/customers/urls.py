from django.conf.urls import handler403, handler404, handler500
from django.contrib.auth import views as auth_views
from django.urls import path, include
from . import views

app_name = "customers"
urlpatterns = [

	path(
		'change-password/', 
		auth_views.PasswordChangeView.as_view(
			template_name="user/change_password.html", 
			success_url="/"), 
		name='change-password'),

	path('', views.CustomerListView.as_view(), name="customer-list"),
	path('<int:pk>/', views.CustomerDetialView.as_view(), name="customer-detail"),

	path('create/', views.CustomerCreate.as_view(), name='customer-create'),
	path('<int:pk>/update/', views.CustomerUpdate.as_view(), name='customer-update'),
	path('<int:pk>/delete/', views.CustomerDelete.as_view(), name='customer-delete'),
    path('delete-all/', views.delete_all_customers, name="delete-all"),

	# path('import-csv/', views.import_as_csv, name="import-csv"),
	path('export-csv/', views.export_as_csv, name="export-csv"),
    path('export-pdf/', views.export_as_pdf , name="export-pdf"),
]

handler403 = views.error_403
handler404 = views.error_404
handler500 = views.error_500
