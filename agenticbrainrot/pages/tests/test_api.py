import json

from django.test import TestCase
from django.urls import reverse

from agenticbrainrot.accounts.models import Participant
from agenticbrainrot.accounts.models import User


class TestStatsSummaryAPI(TestCase):
    def test_returns_json(self):
        response = self.client.get(reverse("api_stats_summary"))

        assert response.status_code == 200
        data = json.loads(response.content)
        assert "total_participants" in data
        assert "total_sessions" in data
        assert "total_challenges_solved" in data

    def test_excludes_staff(self):
        staff_user = User.objects.create_user(
            email="staff@example.com",
            password="testpass123",
            is_staff=True,
        )
        staff_participant, _ = Participant.objects.get_or_create(
            user=staff_user,
        )
        staff_participant.has_active_consent = True
        staff_participant.save()

        response = self.client.get(reverse("api_stats_summary"))
        data = json.loads(response.content)

        assert data["total_participants"] == 0


class TestAccuracyOverTimeAPI(TestCase):
    def test_returns_json(self):
        response = self.client.get(
            reverse("api_stats_accuracy_over_time"),
        )

        assert response.status_code == 200
        data = json.loads(response.content)
        assert "months" in data
        assert "accuracy" in data

    def test_empty_with_no_data(self):
        response = self.client.get(
            reverse("api_stats_accuracy_over_time"),
        )
        data = json.loads(response.content)

        assert data["months"] == []
        assert data["accuracy"] == []


class TestAccuracyByVibeCodingAPI(TestCase):
    def test_returns_json(self):
        response = self.client.get(
            reverse("api_stats_accuracy_by_vibe_coding"),
        )

        assert response.status_code == 200
        data = json.loads(response.content)
        assert "groups" in data

    def test_empty_groups_with_no_data(self):
        response = self.client.get(
            reverse("api_stats_accuracy_by_vibe_coding"),
        )
        data = json.loads(response.content)

        assert data["groups"] == {}
