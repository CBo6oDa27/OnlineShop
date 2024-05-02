from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordResetForm
from users.models import User
from django import forms
from catalog.forms import StyleMixin


class UserRegisterForm(StyleMixin, UserCreationForm):

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')


class UserProfileForm(StyleMixin, UserChangeForm):

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'avatar', 'country')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['password'].widget = forms.HiddenInput()


class PasswordRecoveryForm(StyleMixin, PasswordResetForm):

    class Meta:
        model = User
        fields ='__all__'
