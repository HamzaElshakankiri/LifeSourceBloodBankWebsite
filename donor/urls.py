from django.urls import path
from django.contrib.auth.views import LoginView
from . import views

urlpatterns = [
     path('', views.index, name='index'),
     path('donorlogin/', LoginView.as_view(template_name='pages-login.html'),name='pages-login'),
    
    path('donorsignup/', views.donor_signup_view,name='pages-register'),
  
   # path('donor-dashboard/', views.donor_dashboard_view,name='donor-dashboard'),
   # path('donate-blood/', views.donate_blood_view,name='donate-blood'),
   
    path('donation-history/', views.donation_history_view,name='donation-history'),
   
    path('questionnaire/', views.questionnare_view,name='questionnaire'),
    
    path('questionnairefail/', views.questionnairefail_view,name='questionnairefail'),
    
    path('users-profile/', views.users_profile_view,name='users-profile'),

    path('donor_bookappt/', views.donor_bookappt,name='donor_bookappt')
]