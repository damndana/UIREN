from django.core.management.base import BaseCommand
from main.models import Event, Space

class Command(BaseCommand):
    help = 'Add sample events and spaces to the database'

    def handle(self, *args, **kwargs):
        # Add sample events
        events = [
            {'name': 'A-concert', 'points': 5},
            {'name': 'Football Match', 'points': 3},
            {'name': 'Art Club Therapy Night', 'points': 7},
        ]
        
        for event_data in events:
            Event.objects.get_or_create(
                name=event_data['name'],
                defaults={'points': event_data['points']}
            )
            self.stdout.write(f"Added event: {event_data['name']}")

        # Add sample spaces
        spaces = ['Red Hall', 'Blue Hall', 'Green Room', 'Study Space']
        
        for space_name in spaces:
            Space.objects.get_or_create(name=space_name)
            self.stdout.write(f"Added space: {space_name}")

        self.stdout.write(self.style.SUCCESS('Successfully added sample data')) 