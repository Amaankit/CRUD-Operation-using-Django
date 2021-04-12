from django import forms
from .models import User

class StudentRegistration(forms.ModelForm):
    class Meta:
        model=User
        fields=['id','name','email','password']
        widgets={'name':forms.TextInput(attrs={'class':'form-control'}),
        'email':forms.TextInput(attrs={'class':'form-control'}),
        'password':forms.PasswordInput(render_value=True, attrs={'class':'form-control'}) #When render_value is set to true the password field is visible on update module.
        }