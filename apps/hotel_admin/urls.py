from django.urls import path
from .views import LoginHotelAdminView, ForgotPasswordView, ActivateAccountView, DashboardView, LogoutHotelAdminView, \
    ForgotPasswordSuccessView

app_name = "hotel_admin"
urlpatterns = [
    path('', LoginHotelAdminView.as_view(), name='login'),
    path('login', LoginHotelAdminView.as_view(), name='login'),
    path('logout', LogoutHotelAdminView.as_view(), name='logout'),
    path('forgot-password', ForgotPasswordView.as_view(), name='forgot-password'),
    path('forgot-password-success', ForgotPasswordSuccessView.as_view(), name='forgot-password-success'),
    path('activate-account', ActivateAccountView.as_view(), name='activate-account'),
    path('home', DashboardView.as_view(), name='home')
]