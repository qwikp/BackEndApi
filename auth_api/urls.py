from django.urls import path
from .views import login, sample_api, get_registration_token, Logout, SendSMS


urlpatterns = [
    path('login/', login),
    path('register/', get_registration_token),
    path('sampleapi/', sample_api),
    path('logout/', Logout.as_view()),
    path('send_sms/', SendSMS.as_view()),
]