from django import forms
from .models import BugReport, AuthenticationForm, AccountRequest, MaintTicket

class BugReportForm(forms.ModelForm):
    class Meta:
        model = BugReport
        fields = ['name', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter your name'}),
            'email': forms.EmailInput(attrs={
                'placeholder': 'Enter your email',
                'class': 'email-field'
            }),
            'message': forms.Textarea(attrs={
                'placeholder': 'Please provide a brief description of the issue',
                'rows': 4
            })
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].label = ''
        self.fields['email'].label = ''
        self.fields['message'].label = ''

class AuthenticationForm(forms.ModelForm):
    class Meta:
        model = AuthenticationForm
        fields = ['username', 'password']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'})
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = ''
        self.fields['password'].label = ''

class SearchForm(forms.Form):
    query = forms.CharField(label='Search', max_length=100)

class AccountRequestForm(forms.ModelForm):
    class Meta:
        model = AccountRequest
        fields = ['firstname', 'lastname', 'email']
        widgets = {
            'firstname': forms.TextInput(attrs={'placeholder': 'First Name'}),
            'lastname': forms.TextInput(attrs={'placeholder': 'Last Name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['firstname'].label = ''
        self.fields['lastname'].label = ''
        self.fields['email'].label = ''

class UploadFilesForm(forms.Form):
    files = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': False}))

class SubmitTicket(forms.ModelForm):
    class Meta:
        model = MaintTicket
        fields = ['platform', 'description']
        widgets = {
            'platform': forms.TextInput(attrs={'placeholder': 'Platform'}),
            'description': forms.Textarea(attrs={'placeholder': 'Please Provide a Description of the Issue', 'rows': 5})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['platform'].label = ''
        self.fields['description'].label = ''
