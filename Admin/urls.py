from django.urls import path
from Admin import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.LoginPage, name='login'),
   
    path('admin_dashboard', views.AdminDash, name='admin_dashboard'),
    path('admin_donation', views.AdminDonation, name='admin_donation'),
    path('admin_blood', views.admin_blood, name='admin_blood'), 
    path('admin_create_appt', views.admin_create_apptPage, name='admin_create_appt'),
    path('admin_submit_data', views.admin_submit_data, name='admin_submit_data'),
    path('admin_edit_appt', views.admin_edit_appt, name='admin_edit_appt'),
    path('logout', views.LogoutPage, name='logout'),
    path('updateData/<id>', views.updateData, name="updateData"),
    path('insert', views.insertData, name="insertData"),
    path('delete/<id>', views.deleteData, name="deleteData"),
]
