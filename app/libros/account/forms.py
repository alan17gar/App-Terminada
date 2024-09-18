from django import forms
from django.contrib.auth.models import User
  
  #Clase para el inicio de sesion
class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)
    
    #Clase para el regisro de usuario
class UserRegistrationForm(forms.ModelForm):
    
    password= forms.CharField(label='Contraseña',
                              widget=forms.PasswordInput)
    password2=forms.CharField(label='Repite Contraseña',
                              widget=forms.PasswordInput)
    
    class Meta:
        model= User
        fields=['username','first_name','email']

    def clean_password2(self):
        cd=self.cleaned_data
        if cd['password'] != cd['password2']:
            return forms.ValidationError('las contraseñas no son iguales')
        return cd['password2']