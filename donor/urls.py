from django.urls import path
from django.contrib.auth.views import LoginView
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('donorlogin/', LoginView.as_view(template_name='pages-login.html'),name='pages-login'),
    path('donorsignup/', views.donor_signup_view,name='pages-register'),
    path('donation-history/<donor_email>', views.donation_history_view,name='donation-history'),
    path('questionnaire/', views.questionnare_view,name='questionnaire'),
    path('questionnairefail/', views.questionnairefail_view,name='questionnairefail'),
    path('users-profile/<donor_email>', views.users_profile,name='users-profile'),
    path('updateProfile/<int:donor_id>', views.updateProfile, name="updateData"),
    path('donor_bookappt/', views.donor_bookappt,name='donor_bookappt'),
    path('donor_bookappNoQ/', views.donor_bookappNoQ,name='donor_bookappNoQ'),
    path('donor_currentappt/<int:e_id>/<donor_email>', views.donor_currentappt, name="donor_currentappt"),
    path('donor_currentappt/<donor_email>', views.donor_currentappt_specific, name="bookAppt"),
    path('donor_delete_currentappt/<int:e_id>/<donor_email>', views.donor_delete_currentappt, name="donor_delete_currentappt"),
]
