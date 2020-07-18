# customer-management-system #

Simple Customer Management System with Basic CRUD Operations written in django


## Resources ##

[Python](https://python.org) | [Django](https://www.djangoproject.com)


## Installation Insturaction ##

- `git clone https://github.com/chitkokooo/customer-management-system`
- `cd customer-management-system\cms` in GNU/linux (or) `cd customer-management-system/cms` in Windows
- `touch db.sqlite3` in GNU/Linux (or) create a file named `db.sqlite3` in Windows
- `python manage.py makemgrations`
- `python manage.py migrate`
- `python manage.py collectstatic`
- `python manage.py createsuperuser` and enter information as instructions
- `python manage.py runserver`
- Open `http://127.0.0.1:8000` in web browser


## Creating Groups ##
Create a group named `Authorizers` and give permissions `customers | customer | Customer CRUD Operations`
![auth_group](resources/2_authorizers_group.png)

Create a group named `Tellers` and give permissions `customers | customer | Can view customer`
![teller_group](resources/4_tellers_group.png)


## Creating Users ##
Add a user and add to `Tellers` Group, and Add a user and add to `Authorizers` Group.
They have different permissions.


## Some Screenshots ##

Login
![login](resources/1_login_page.png)

Create new Customer
![new_customer](resources/3_add_new_customer.png)


## About Me ##

[Facebook](https://www.faceboook.com/artisan443)

Email: chitkokooo.cu (at) gmail (dot) com

