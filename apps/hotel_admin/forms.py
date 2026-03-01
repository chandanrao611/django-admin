from django import forms

def common_attrs(name, placeholder, className=None, maxLength=None):
    attrs = {
        'name': name,
        'placeholder': placeholder,
    }
    return {
        'class': 'form-control ' + (className if className else ''),
        'name': name,
        'placeholder': placeholder,
        'maxlength': maxLength if maxLength else '100'
    }
class EmployeeForm(forms.Form) :
    def __init__(self, *args, **kwargs):
        self.employee_id = kwargs.pop('employee_id', None)  # 👈 ALWAYS SET
        super().__init__(*args, **kwargs)

    first_name = forms.CharField(label='First Name', max_length=50, widget=forms.TextInput(attrs=common_attrs('first_name','Enter your first name')))
    last_name = forms.CharField(label='Last Name', max_length=50, required=False,widget=forms.TextInput(attrs=common_attrs('last_name','Enter your last name')))
    email = forms.EmailField(label='Email', max_length=20, widget=forms.TextInput(attrs=common_attrs('email','Enter your email')))
    dob = forms.DateField(label='DOB', input_formats=['%Y-%m-%d'], widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control', 'placeholder': 'DD/MM/YYYY', 'name': 'dob'}))
    gender = forms.ChoiceField(label='Gender',
                               initial='male',
                               choices=[
                                   ('male', 'Male'),
                                   ('female', 'Female'),
                                   ('other', 'Other'),
                               ],
                               widget=forms.Select(attrs=common_attrs('gender', 'Select your gender'))
                            )
    city = forms.CharField(label='City',widget=forms.TextInput(attrs=common_attrs('city','Enter your city')))
    district = forms.CharField(label='District', widget=forms.TextInput(attrs=common_attrs('district','Enter your district')))
    state = forms.CharField(label='State', widget=forms.TextInput(attrs=common_attrs('state', 'Enter your state')))
    pincode = forms.CharField(label='Pin Code', widget=forms.TextInput(attrs=common_attrs('pincode', 'Enter your pin code', 'number notwhitespace', '6')))
    mobile = forms.CharField(label='Mobile', widget=forms.TextInput(attrs=common_attrs('mobile', 'Enter your mobile', 'number notwhitespace', '10')))

    def clean(self):
        cleaned_data = super().clean()
        first_name = self.cleaned_data.get('first_name')
        if first_name == '':
            self.add_error('first_name', 'Please enter a first name')
        if first_name and len(first_name.strip()) < 3:
            self.add_error('first_name', 'Please enter at least 3 characters')

        return cleaned_data

    def clean_email(self):
        email = self.cleaned_data['email']
        # qs = Employee.objects.filter(email=email)
        # # ✅ Ignore same record during edit
        # if self.employee_id is not None:
        #     qs = qs.exclude(id=self.employee_id)
        # if qs.exists():
        #     raise forms.ValidationError("This email is already registered")

        return email

class LoginForm(forms.Form):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs=common_attrs('username','Enter your username', 'form-control-lg', '20')))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs=common_attrs('password','Password', 'form-control-lg')))

    def clean(self):
        cleaned_data = super().clean()
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        if username == '':
            self.add_error('username', 'Please enter a username')
        if password == '':
            self.add_error('password', 'Please enter a password')
        return cleaned_data

class ForgotPasswordForm(forms.Form):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs=common_attrs('username','Enter your username', 'form-control-lg', '20')))
    def clean(self):
        cleaned_data = super().clean()
        username = self.cleaned_data.get('username')
        if username == '':
            self.add_error('username', 'Please enter a username')
        return cleaned_data

class OtpForm(forms.Form):
    first = forms.CharField(widget=forms.TextInput(attrs=common_attrs('first','*', 'm-2 text-center form-control rounded', '1')))
    second = forms.CharField(
        widget=forms.TextInput(attrs=common_attrs('second', '*', 'm-2 text-center form-control rounded', '1')))
    third = forms.CharField(
        widget=forms.TextInput(attrs=common_attrs('third', '*', 'm-2 text-center form-control rounded', '1')))
    four = forms.CharField(
        widget=forms.TextInput(attrs=common_attrs('four', '*', 'm-2 text-center form-control rounded', '1')))
    five = forms.CharField(
        widget=forms.TextInput(attrs=common_attrs('five', '*', 'm-2 text-center form-control rounded', '1')))
    six = forms.CharField(
        widget=forms.TextInput(attrs=common_attrs('six', '*', 'm-2 text-center form-control rounded', '1')))

    def clean(self):
        cleaned_data = super().clean()
        first = self.cleaned_data.get('first')
        second = self.cleaned_data.get('second')
        third = self.cleaned_data.get('third')
        four = self.cleaned_data.get('four')
        five = self.cleaned_data.get('five')
        six = self.cleaned_data.get('six')
        if not first.strip() or not second.strip() or not third.strip() or not four.strip() or not five.strip() or not six.strip():
            self.add_error('first', 'Please enter valid OTP code')
        return cleaned_data