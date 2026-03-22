from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, LeaderboardEntry, Workout
from datetime import date

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Delete existing data
        LeaderboardEntry.objects.all().delete()
        Activity.objects.all().delete()
        Workout.objects.all().delete()
        teams = list(Team.objects.all())
        for team in teams:
            team.members.clear()
        for user in User.objects.all():
            user.delete()
        for team in teams:
            team.delete()

        # Create Teams
        marvel = Team.objects.create(id=1, name='Team Marvel')
        dc = Team.objects.create(id=2, name='Team DC')

        # Create Users (Superheroes) and assign teams via ForeignKey
        users = [
            User.objects.create_user(id=1, email='tony@stark.com', username='IronMan', password='password123', team=marvel),
            User.objects.create_user(id=2, email='steve@rogers.com', username='CaptainAmerica', password='password123', team=marvel),
            User.objects.create_user(id=3, email='bruce@wayne.com', username='Batman', password='password123', team=dc),
            User.objects.create_user(id=4, email='clark@kent.com', username='Superman', password='password123', team=dc),
        ]

        # Create Workouts
        workouts = [
            Workout.objects.create(user=users[0], name='Push Ups', description='Upper body workout', date=date.today()),
            Workout.objects.create(user=users[1], name='Running', description='Cardio workout', date=date.today()),
            Workout.objects.create(user=users[2], name='Sit Ups', description='Core workout', date=date.today()),
            Workout.objects.create(user=users[3], name='Swimming', description='Full body workout', date=date.today()),
        ]

        # Create Activities
        Activity.objects.create(user=users[0], activity_type='Push Ups', duration=30, distance=None, calories=200, date=date.today())
        Activity.objects.create(user=users[1], activity_type='Running', duration=45, distance=5.0, calories=350, date=date.today())
        Activity.objects.create(user=users[2], activity_type='Sit Ups', duration=20, distance=None, calories=150, date=date.today())
        Activity.objects.create(user=users[3], activity_type='Swimming', duration=60, distance=2.0, calories=500, date=date.today())

        # Create Leaderboard
        LeaderboardEntry.objects.create(user=users[0], team=marvel, score=200, rank=2)
        LeaderboardEntry.objects.create(user=users[1], team=marvel, score=350, rank=3)
        LeaderboardEntry.objects.create(user=users[2], team=dc, score=150, rank=4)
        LeaderboardEntry.objects.create(user=users[3], team=dc, score=500, rank=1)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data.'))
