from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django.contrib.auth.forms import AuthenticationForm

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'peso', 'birthday','gender', 'goal']
        widgets = {
            'birthday': forms.DateInput(attrs={'type': 'date'}),
            'gender': forms.RadioSelect(choices=CustomUser.GENDER_CHOICES),
        }

# forms.py en tu aplicación

class CustomUserEditForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email', 'peso', 'foto_perfil', 'birthday','gender', 'goal']

        # def __init__(self, *args, **kwargs):
        #     super().__init__(*args, **kwargs)
        #     # Eliminamos la opción predeterminada ("---------") del campo 'gender'
        #     self.fields['gender'].empty_label = None
    # widgets = {
    #     'username': forms.TextInput(attrs={'class': 'input--style-4'}),
    #     'first_name': forms.TextInput(attrs={'class': 'input--style-4'}),
    #     'last_name': forms.TextInput(attrs={'class': 'input--style-4'}),
    #     'email': forms.EmailInput(attrs={'class': 'input--style-4'}),
    #     'password1': forms.PasswordInput(attrs={'class': 'input--style-4'}),
    #     'password2': forms.PasswordInput(attrs={'class': 'input--style-4'}),
    #     'peso': forms.TextInput(attrs={'class': 'input--style-4'}),
    #     'foto_perfil': forms.FileInput(attrs={'class': 'input--style-4'}),
    # }
