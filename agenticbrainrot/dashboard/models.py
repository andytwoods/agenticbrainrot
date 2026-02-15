from django.conf import settings
from django.db import models


class DatasetAccessGrant(models.Model):
    """Grants a user early access to dataset downloads during embargo period."""

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="dataset_access_grants",
    )
    email = models.EmailField(
        blank=True,
        help_text="For external researchers without an account.",
    )
    granted_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name="dataset_grants_given",
    )
    granted_at = models.DateTimeField(auto_now_add=True)
    reason = models.TextField(blank=True)

    class Meta:
        ordering = ["-granted_at"]

    def __str__(self) -> str:
        target = self.user.email if self.user else self.email
        return f"Dataset access for {target}"
