from django.contrib import admin
from django.urls import path
from account.views import RegisterAPI,VerifyOTP
urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',RegisterAPI.as_view()),
    path('verify/',VerifyOTP.as_view()),
]
