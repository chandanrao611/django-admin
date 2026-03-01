import csv

from django.conf import settings
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.core import signing
from django.core.paginator import Paginator
from django.core.signing import BadSignature, SignatureExpired
from django.db import transaction
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required

from utils.EmailService import EmailService
from utils.FileHandlerService import FileHandlerService
from utils.HelperService import HelperService
from utils.MessageHandler import MessageHandler
from .forms import LoginForm, ForgotPasswordForm, OtpForm, AdminUserForm, FileForm
from django.contrib.auth.hashers import make_password
# SUPER ADMIN
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, logout
from django.contrib.auth.hashers import check_password
from django.http import HttpResponse
from django.contrib.auth import authenticate, login

from .models import AdminUser

User = get_user_model()
class LoginHotelAdminView(LoginView):
    """
    If User already logged in,
    and try to open login page, then it will redirect to the home page.
    """
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/home')
        return super().dispatch(request, *args, **kwargs)
    # Loading login page
    def get(self, request):
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

    #Handling login form submission
    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            username = cd["username"]
            password = cd["password"]
            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                messages.error(request, "Invalid username or password")
                return render(request, 'login.html', {'form': form})

            # ✅ Manually check password
            if not check_password(password, user.password):
                messages.error(request, "Invalid username or password")
                return render(request, 'login.html', {'form': form})

            # ✅ Check super admin
            # if not user.is_superuser:
            #     return HttpResponse("You are not a super admin")
            # ✅ Manual session creation
            request.session['superadmin_id'] = user.id
            request.session['is_superadmin'] = True
            login(request, user)
            return redirect('/home')
        else:
            return render(request, 'login.html', {'form': form})

# Logout the user when click on the logout icon
class LogoutHotelAdminView(View):
    def get(self, request):
        logout(request)
        messages.success(request, "You have been logged out.")
        return redirect('/login')


class ForgotPasswordView(View):
    """
    If User already logged in,
    and try to open login page, then it will redirect to the home page.
    """
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/home')
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        form = ForgotPasswordForm()
        return render(request, 'forgot-password.html', {'form': form})

    def post(self, request):
        form = ForgotPasswordForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            username = cd["username"]
            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                MessageHandler.error(request, MessageHandler.INVALID_CREDENTIALS)
                return render(request, 'forgot-password.html', {'form': form})
            if not user:
                MessageHandler.error(request, MessageHandler.INVALID_CREDENTIALS)
                return render(request, 'forgot-password.html', {'form': form})
            otp = HelperService.generate_otp()
            encrypted_data = signing.dumps({"username": user.get_username(), "_id": user.id, "otp": otp})
            encrypted_data_url = signing.dumps({"username": user.get_username(), "_id": user.id, "otp": otp, "verified": True})
            reset_url = request.build_absolute_uri(
                reverse('hotel_admin:forgot-password-success') + f'?token={encrypted_data_url}'
            )
            EmailService.send_email(
                subject="Reset Password",
                template_name="forgot-password-email.html",
                context={"username": user, "reset_url": reset_url, "otp": otp},
                recipient_list=['raologictech@gmail.com']
            )
            return redirect(f'/forgot-password-success?token={encrypted_data}')
        else:
            return render(request, 'forgot-password.html', {'form': form})

class ForgotPasswordSuccessView(View):
    def get(self, request):
        token = request.GET.get('token')
        try:
            username = signing.loads(token, max_age=60000) #600 seconds = 10 minutes
        except SignatureExpired:
            return render(request, "expired_link.html")
        except BadSignature:
            return render(request, "invalid_link.html")
        optForm = OtpForm()
        return render(request, 'forgot-password-success.html', {"username": username, "optForm": optForm})

    def post(self, request):
        optForm = OtpForm(request.POST)
        token = signing.loads(request.GET.get('token'), max_age=60000)
        if optForm.is_valid():
            cd = optForm.cleaned_data
            entered_otp = cd['first']+cd['second']+cd['third']+cd['four']+cd['five']+cd['six']
            # Now you can access your data
            otp = token.get("otp")
            if otp == entered_otp:
                encrypted_data = signing.dumps({"username": token.get("username"), "_id": token.get("_id"), "otp": otp, "verified": True})
                return redirect(f'/activate-account?token={encrypted_data}')
            else:
                MessageHandler.error(request, MessageHandler.INVALID_CREDENTIALS)
                return render(request, 'forgot-password-success.html', {"username": token.get("username"), "optForm": optForm})
        else:
            return render(request, 'forgot-password-success.html', {"username": token.get("username"), "optForm": optForm})


class ActivateAccountView(View):
    def get(self, request):
        token = request.GET.get('token')
        try:
            username = signing.loads(token, max_age=60000)  # 600 seconds = 10 minutes
        except SignatureExpired:
            return render(request, "expired_link.html")
        except BadSignature:
            return render(request, "invalid_link.html")
        return redirect(f'/login')

class DashboardView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'dashboard.html')

class AdminRegistrationView(View):
    def get(self, request):
        form = AdminUserForm()
        return render(request, 'admin-registration.html', {'form': form})

    def post(self, request):
        form = AdminUserForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            AdminUser.objects.create(
                first_name=cd['first_name'],
                last_name=cd['last_name'],
                username=cd['username'],
                email=cd['email'],
                dob=cd['dob'],
                gender=cd['gender'],
                city=cd['city'],
                district=cd['district'],
                state=cd['state'],
                pincode=cd['pincode'],
                password=make_password('12345A'),
                mobile=cd['mobile'],
                status='pending',
                is_staff= True
            )
            return redirect('/admin-list')
        return render(request, 'admin-registration.html', {'form': form})


class AdminProfileView(LoginRequiredMixin, View):
    def get(self, request, admin_id):
        print(request, admin_id)
        return render(request, 'admin-profile.html')


class AdminListView(LoginRequiredMixin, View):
    def get(self, request):
        staff_users = User.objects.all()
        # Create paginator: 10 employees per page
        limit = int(request.GET.get('limit', 10))
        paginator = Paginator(staff_users, limit)
        # Get current page number from query string (?page=2)
        page_number = request.GET.get('page', 1)
        # Get the page object
        page_obj = paginator.get_page(page_number)
        fileForm = FileForm()
        return render(request, 'admin-list.html', {'page_obj': page_obj, 'fileForm':fileForm})

    def post(self, request):
        form = FileForm(request.POST, request.FILES)
        if not form.is_valid():
            MessageHandler.error(request, MessageHandler.INVALID_CREDENTIALS)
            print('----------')
            return self.get(request)
        file = request.FILES.get("csv_file")
        if not file:
            MessageHandler.error(request, MessageHandler.INVALID_CREDENTIALS)
            return self.get(request)

        for batch in FileHandlerService.read_csv(file, 1000):
            users = []

            for row in batch:
                users.append(
                    AdminUser(
                        first_name=row.get('first_name'),
                        last_name=row.get('last_name'),
                        username=row.get('username'),
                        email=row.get('email'),
                        city=row.get('city'),
                        district=row.get('district'),
                        password=make_password(row.get('password', '123456')),
                        mobile=row.get('mobile'),
                        status='pending',
                        is_staff=True
                    )
                )

            try:
                with transaction.atomic():
                    AdminUser.objects.bulk_create(users)
                print("Inserted:", len(users))
            except Exception as e:
                print("Insert Error:", e)

        return self.get(request)
