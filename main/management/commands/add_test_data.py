from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from main.models import UserProfile, Event, Space, SpaceBooking, UserEvent
from django.utils import timezone

class Command(BaseCommand):
    help = 'Add test data including users, events, spaces, and bookings'

    def handle(self, *args, **kwargs):
        # Create test users
        test_users = [
            {
                'username': 'student1',
                'email': 'student1@example.com',
                'password': 'testpass123',
                'role': 'Student',
                'major': 'Computer Science'
            },
            {
                'username': 'student2',
                'email': 'student2@example.com',
                'password': 'testpass123',
                'role': 'Student',
                'major': 'Engineering'
            },
            {
                'username': 'teacher1',
                'email': 'teacher1@example.com',
                'password': 'testpass123',
                'role': 'Teacher',
                'major': 'Computer Science'
            }
        ]

        for user_data in test_users:
            user, created = User.objects.get_or_create(
                username=user_data['username'],
                email=user_data['email']
            )
            if created:
                user.set_password(user_data['password'])
                user.save()
                UserProfile.objects.create(
                    user=user,
                    role=user_data['role'],
                    major=user_data['major']
                )
                self.stdout.write(f"Created user: {user.username}")

        # Create test events
        events = [
            {'name': 'Tech Conference 2024', 'points': 10},
            {'name': 'Hackathon Spring', 'points': 15},
            {'name': 'AI Workshop', 'points': 8},
            {'name': 'Career Fair', 'points': 5},
            {'name': 'Programming Contest', 'points': 12}
        ]

        for event_data in events:
            event, created = Event.objects.get_or_create(
                name=event_data['name'],
                defaults={'points': event_data['points']}
            )
            if created:
                self.stdout.write(f"Created event: {event.name}")

        # Create test spaces
        spaces = [
            'Main Auditorium',
            'Conference Room A',
            'Study Hall',
            'Computer Lab',
            'Workshop Space'
        ]

        for space_name in spaces:
            space, created = Space.objects.get_or_create(name=space_name)
            if created:
                self.stdout.write(f"Created space: {space_name}")

        # Add some test user event attendance
        student1 = User.objects.get(username='student1')
        student2 = User.objects.get(username='student2')
        
        for event in Event.objects.all()[:3]:  # First 3 events for student1
            UserEvent.objects.get_or_create(
                user=student1,
                event=event,
                defaults={'attended_at': timezone.now()}
            )
            self.stdout.write(f"Added {student1.username} to event: {event.name}")

        for event in Event.objects.all()[2:]:  # Last 3 events for student2
            UserEvent.objects.get_or_create(
                user=student2,
                event=event,
                defaults={'attended_at': timezone.now()}
            )
            self.stdout.write(f"Added {student2.username} to event: {event.name}")

        # Add some test space bookings
        spaces = Space.objects.all()
        for i, space in enumerate(spaces[:2]):  # Book first 2 spaces for student1
            SpaceBooking.objects.get_or_create(
                user=student1,
                space=space,
                defaults={'booked_at': timezone.now()}
            )
            self.stdout.write(f"Added booking for {student1.username}: {space.name}")

        for i, space in enumerate(spaces[2:4]):  # Book next 2 spaces for student2
            SpaceBooking.objects.get_or_create(
                user=student2,
                space=space,
                defaults={'booked_at': timezone.now()}
            )
            self.stdout.write(f"Added booking for {student2.username}: {space.name}")

        self.stdout.write(self.style.SUCCESS('Successfully added all test data')) 