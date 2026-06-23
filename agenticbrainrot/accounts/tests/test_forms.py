"""Module for all Form Tests."""

import pytest
from captcha.models import CaptchaStore
from django.core import mail
from django.urls import reverse

from agenticbrainrot.accounts.forms import (
    ResetPasswordFormWithCaptcha,
    UserAdminCreationForm,
    UserSignupForm,
)
from agenticbrainrot.accounts.models import User


class TestUserAdminCreationForm:
    """
    Test class for all tests related to the UserAdminCreationForm
    """

    def test_username_validation_error_msg(self, user: User):
        """
        Tests UserAdminCreation Form's unique validator functions correctly by testing:
            1) A new user with an existing username cannot be added.
            2) Only 1 error is raised by the UserCreation Form
            3) The desired error message is raised
        """

        # The user already exists,
        # hence cannot be created.
        form = UserAdminCreationForm(
            {
                "email": user.email,
                "password1": user.password,
                "password2": user.password,
            },
        )

        assert not form.is_valid()
        assert len(form.errors) == 1
        assert "email" in form.errors
        assert form.errors["email"][0] == "This email has already been taken."


class TestUserSignupFormCaptcha:
    """The public signup form must require a CAPTCHA so the email-confirmation
    endpoint cannot be abused as an email cannon (list-bombing)."""

    def test_form_has_captcha_field(self):
        assert "captcha" in UserSignupForm().fields

    def test_submission_without_captcha_is_invalid(self, db):
        form = UserSignupForm(
            {
                "email": "bot@example.com",
                "password1": "Sup3rSecret!!",
                "password2": "Sup3rSecret!!",
            },
        )
        assert not form.is_valid()
        assert "captcha" in form.errors

    @pytest.mark.django_db
    def test_signup_endpoint_blocks_bot_and_sends_no_email(self, client, settings):
        settings.ACCOUNT_ALLOW_REGISTRATION = True
        mail.outbox.clear()
        resp = client.post(
            reverse("account_signup"),
            {
                "email": "bot@example.com",
                "password1": "Sup3rSecret!!",
                "password2": "Sup3rSecret!!",
            },
        )
        # Form redisplayed (200), no redirect to verification, no email sent.
        assert resp.status_code == 200
        assert len(mail.outbox) == 0

    @pytest.mark.django_db
    def test_signup_endpoint_accepts_valid_captcha(self, client, settings):
        settings.ACCOUNT_ALLOW_REGISTRATION = True
        mail.outbox.clear()
        key = CaptchaStore.generate_key()
        resp = client.post(
            reverse("account_signup"),
            {
                "email": "human@example.com",
                "password1": "Sup3rSecret!!",
                "password2": "Sup3rSecret!!",
                "captcha_0": key,
                "captcha_1": "PASSED",  # CAPTCHA_TEST_MODE answer
            },
        )
        assert resp.status_code == 302
        assert len(mail.outbox) == 1


class TestResetPasswordFormCaptcha:
    """The password-reset request endpoint emails the address on every
    submission, so it needs the same CAPTCHA as signup."""

    def test_form_has_captcha_field(self):
        assert "captcha" in ResetPasswordFormWithCaptcha().fields

    @pytest.mark.django_db
    def test_reset_blocks_bot_and_sends_no_email(self, client, user):
        mail.outbox.clear()
        resp = client.post(reverse("account_reset_password"), {"email": user.email})
        assert resp.status_code == 200  # redisplayed, not redirected
        assert len(mail.outbox) == 0

    @pytest.mark.django_db
    def test_reset_accepts_valid_captcha(self, client, user):
        mail.outbox.clear()
        key = CaptchaStore.generate_key()
        resp = client.post(
            reverse("account_reset_password"),
            {"email": user.email, "captcha_0": key, "captcha_1": "PASSED"},
        )
        assert resp.status_code == 302
        assert len(mail.outbox) == 1
