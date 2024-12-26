from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User

# 회원가입을 위한 form클래스
class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'profile_image', 'password1', 'password2']

# 프로필 수정을 위한 form클래스
class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'profile_image']