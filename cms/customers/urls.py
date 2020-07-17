from django.urls import path, include
from . import views

app_name = "customers"
urlpatterns = [
	# path('', views.index, name="index"),
	path('', views.CustomerListView.as_view(), name="customer-list"),
	path('<int:pk>/', views.CustomerDetialView.as_view(), name="customer-detail")
]