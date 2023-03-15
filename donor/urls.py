from django.urls import path
from django.contrib.auth.views import LoginView
from . import views

urlpatterns = [
    #index Page View
    path('', views.index, name='index'),
    #Login Page View
    path('donorlogin/', LoginView.as_view(template_name='pages-login.html'),name='pages-login'),
    #SignUp Page View
    path('donorsignup/', views.donor_signup_view,name='pages-register'),
    #Donation History Page View
    path('donation-history/<donor_email>', views.donation_history_view,name='donation-history'),
    #Questionnaire Page View
    path('questionnaire/', views.questionnare_view,name='questionnaire'),
    #Questionnaire Fail Page View
    path('questionnairefail/', views.questionnairefail_view,name='questionnairefail'),
    #Users Profile Page View
    path('users-profile/<donor_email>', views.users_profile,name='users-profile'),
    #Updating Profile Page View
    path('updateProfile/<int:donor_id>', views.updateProfile, name="updateData"),
    #Booking Appointment Page View
    path('donor_bookappt/', views.donor_bookappt,name='donor_bookappt'),
    #Needs Questionnaire View Page View
    path('donor_bookappNoQ/', views.donor_bookappNoQ,name='donor_bookappNoQ'),
    #Current Appointment Page View
    path('donor_currentappt/<int:e_id>/<donor_email>', views.donor_currentappt, name="donor_currentappt"),
    #Current appointment Page Page View
    path('donor_currentappt/<donor_email>', views.donor_currentappt_specific, name="bookAppt"),
    #Cancelling Appointment Page View
    path('donor_delete_currentappt/<int:e_id>/<donor_email>', views.donor_delete_currentappt, name="donor_delete_currentappt"),
]
