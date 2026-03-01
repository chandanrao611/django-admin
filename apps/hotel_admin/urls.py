from django.urls import path
from .views import LoginHotelAdminView, ForgotPasswordView, ActivateAccountView, DashboardView, LogoutHotelAdminView, \
    ForgotPasswordSuccessView, AdminRegistrationView, AdminProfileView, AdminListView

app_name = "hotel_admin"
urlpatterns = [
    path('', LoginHotelAdminView.as_view(), name='login'),
    path('login', LoginHotelAdminView.as_view(), name='login'),
    path('logout', LogoutHotelAdminView.as_view(), name='logout'),
    path('forgot-password', ForgotPasswordView.as_view(), name='forgot-password'),
    path('forgot-password-success', ForgotPasswordSuccessView.as_view(), name='forgot-password-success'),
    path('activate-account', ActivateAccountView.as_view(), name='activate-account'),
    path('home', DashboardView.as_view(), name='home'),
    path('admin-add', AdminRegistrationView.as_view(), name='admin-add'),
    path('admin-update/<int:admin_id>/', AdminRegistrationView.as_view(), name='admin-update'),
    path('admin-profile/<int:admin_id>/', AdminProfileView.as_view(), name='admin-profile'),
    path('admin-list', AdminListView.as_view(), name='admin-list')
]