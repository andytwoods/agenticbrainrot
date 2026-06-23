from allauth.account.forms import ResetPasswordForm, ResetPasswordKeyForm, SignupForm
from allauth.account.forms import PasswordField
from allauth.socialaccount.forms import SignupForm as SocialSignupForm
from captcha.fields import CaptchaField
from django.contrib.auth import forms as admin_forms
from django.forms import EmailField

from .models import User


class UserAdminChangeForm(admin_forms.UserChangeForm):
    class Meta(admin_forms.UserChangeForm.Meta):  # type: ignore[name-defined]
        model = User
        field_classes = {"email": EmailField}


class UserAdminCreationForm(admin_forms.AdminUserCreationForm):
    """
    Form for User Creation in the Admin Area.
    To change user signup, see UserSignupForm and UserSocialSignupForm.
    """

    class Meta(admin_forms.UserCreationForm.Meta):  # type: ignore[name-defined]
        model = User
        fields = ("email",)
        field_classes = {"email": EmailField}
        error_messages = {
            "email": {"unique": "This email has already been taken."},
        }


class ResetPasswordKeyFormFixed(ResetPasswordKeyForm):
    password2 = PasswordField(label="New Password (again)", autocomplete="new-password")


class ResetPasswordFormWithCaptcha(ResetPasswordForm):
    """
    Password-reset request form. Like signup, this endpoint emails the address
    on every submission, so it is an email-bombing / abuse vector and needs the
    same self-hosted CAPTCHA. (The key-based form above sets the new password
    after the emailed link is followed and sends no mail, so it needs none.)
    """

    captcha = CaptchaField()


class UserSignupForm(SignupForm):
    """
    Form that will be rendered on a user sign up section/screen.
    Default fields will be added automatically.
    Check UserSocialSignupForm for accounts created from social.

    A self-hosted CAPTCHA (django-simple-captcha) guards this form against
    automated abuse. The public signup endpoint sends an email-confirmation
    message for every submission, so without a challenge a bot can use it as
    an email cannon (list-bombing), burning SMTP credits and harming sender
    reputation. The CAPTCHA needs no third-party keys and renders from 'self'.
    """

    captcha = CaptchaField()


class UserSocialSignupForm(SocialSignupForm):
    """
    Renders the form when user has signed up using social accounts.
    Default fields will be added automatically.
    See UserSignupForm otherwise.
    """
