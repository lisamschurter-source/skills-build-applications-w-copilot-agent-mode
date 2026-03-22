from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth import get_user_model
from .models import Team, Activity, Workout, LeaderboardEntry

User = get_user_model()

class UserTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.force_authenticate(user=self.user)

    def test_user_list(self):
        response = self.client.get(reverse('user-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class TeamTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.force_authenticate(user=self.user)

    def test_create_team(self):
        response = self.client.post(reverse('team-list'), {'name': 'Team A'})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class ActivityTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.force_authenticate(user=self.user)

    def test_create_activity(self):
        data = {
            'activity_type': 'Running',
            'duration': 30,
            'date': '2023-01-01'
        }
        response = self.client.post(reverse('activity-list'), data)
        self.assertIn(response.status_code, [status.HTTP_201_CREATED, status.HTTP_400_BAD_REQUEST])

class WorkoutTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.force_authenticate(user=self.user)

    def test_create_workout(self):
        data = {
            'name': 'Morning Workout',
            'date': '2023-01-01'
        }
        response = self.client.post(reverse('workout-list'), data)
        self.assertIn(response.status_code, [status.HTTP_201_CREATED, status.HTTP_400_BAD_REQUEST])

class LeaderboardEntryTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.force_authenticate(user=self.user)

    def test_leaderboard_list(self):
        response = self.client.get(reverse('leaderboardentry-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
